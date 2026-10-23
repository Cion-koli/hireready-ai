import React, { useState, useEffect, useRef } from 'react';
import { useParams, useNavigate } from 'react-router-dom';
import { interviewsApi } from '../api/interviews';
import { useSpeechRecognition } from '../hooks/useSpeechRecognition';
import { useSpeechSynthesis } from '../hooks/useSpeechSynthesis';
import { ConfirmModal } from '../components/ConfirmModal';
import {
  Sparkles,
  Mic,
  MicOff,
  Volume2,
  VolumeX,
  Send,
  Flag,
  RotateCcw,
  AlertCircle,
  CheckCircle,
  HelpCircle,
  Loader2,
  Keyboard,
  ShieldAlert,
  Code2,
  Users,
  Copy,
  Check,
  Terminal,
  FileCode
} from 'lucide-react';

export const InterviewRoomPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  // Interview state
  const [interview, setInterview] = useState(null);
  const [currentQuestion, setCurrentQuestion] = useState(null);
  const [currentNumber, setCurrentNumber] = useState(1);
  const [totalQuestions, setTotalQuestions] = useState(5);
  const [answerText, setAnswerText] = useState('');
  const [isSubmitting, setIsSubmitting] = useState(false);
  const [isLoadingQuestion, setIsLoadingQuestion] = useState(true);
  const [errorMessage, setErrorMessage] = useState(null);
  const [isEndingEarly, setIsEndingEarly] = useState(false);
  const [endModalOpen, setEndModalOpen] = useState(false);
  const [activeMode, setActiveMode] = useState('text'); // 'voice' or 'text'
  const [isCodeFormat, setIsCodeFormat] = useState(false);
  const [copiedSnippet, setCopiedSnippet] = useState(false);

  // Voice Hooks
  const {
    isListening,
    transcript,
    error: speechError,
    isSupported: isSpeechRecSupported,
    startListening,
    stopListening,
    resetTranscript,
    setTranscript
  } = useSpeechRecognition();

  const {
    isSpeaking,
    isSupported: isSynthSupported,
    speak,
    cancel: cancelSpeech
  } = useSpeechSynthesis();

  // Sync speech recognition transcript into answerText
  useEffect(() => {
    if (transcript) {
      setAnswerText(transcript);
    }
  }, [transcript]);

  // Initial load
  useEffect(() => {
    loadInterviewAndQuestion();
    return () => {
      cancelSpeech();
      stopListening();
    };
  }, [id]);

  const loadInterviewAndQuestion = async () => {
    setIsLoadingQuestion(true);
    setErrorMessage(null);
    try {
      const interviewData = await interviewsApi.get(id);
      setInterview(interviewData);
      setTotalQuestions(interviewData.question_count);
      setActiveMode(interviewData.interview_mode || 'text');

      if (interviewData.status === 'completed') {
        navigate(`/reports/${interviewData.report_id || interviewData.id}`);
        return;
      }

      await fetchNextQuestion();
    } catch (err) {
      console.error('Failed to load interview room:', err);
      setErrorMessage(err.message || 'Could not load interview session.');
      setIsLoadingQuestion(false);
    }
  };

  const fetchNextQuestion = async () => {
    setIsLoadingQuestion(true);
    setErrorMessage(null);
    resetTranscript();
    setAnswerText('');

    try {
      const response = await interviewsApi.getNextQuestion(id);

      if (response.is_completed) {
        // Complete interview and evaluate
        await finishAndEvaluate();
        return;
      }

      setCurrentQuestion(response.question);
      setCurrentNumber(response.current_number);

      // Auto enable code formatting mode if technical with code snippet
      if (response.question?.is_technical && response.question?.code_snippet) {
        setIsCodeFormat(true);
      }

      setIsLoadingQuestion(false);

      // Auto-read question if voice mode
      if (interview?.interview_mode === 'voice' || activeMode === 'voice') {
        setTimeout(() => {
          speak(response.question.question_text);
        }, 400);
      }
    } catch (err) {
      console.error('Failed to fetch next question:', err);
      setErrorMessage(err.message || 'Could not load the next interview question.');
      setIsLoadingQuestion(false);
    }
  };

  const handleSubmitAnswer = async () => {
    const trimmed = answerText.trim();
    if (!trimmed) {
      setErrorMessage('Please provide an answer before submitting.');
      return;
    }

    cancelSpeech();
    stopListening();
    setIsSubmitting(true);
    setErrorMessage(null);

    try {
      const res = await interviewsApi.submitAnswer(
        id,
        currentQuestion.id,
        trimmed,
        activeMode === 'voice'
      );

      if (res.is_finished) {
        await finishAndEvaluate();
      } else {
        await fetchNextQuestion();
      }
    } catch (err) {
      console.error('Failed to submit answer:', err);
      setErrorMessage(err.message || 'Failed to submit response. Please try again.');
    } finally {
      setIsSubmitting(false);
    }
  };

  const finishAndEvaluate = async () => {
    setIsSubmitting(true);
    try {
      const report = await interviewsApi.complete(id);
      navigate(`/reports/${report.id || id}`);
    } catch (err) {
      console.error('Failed to generate report:', err);
      setErrorMessage('Failed to generate interview report. Redirecting to reports...');
      setTimeout(() => navigate('/history'), 2000);
    }
  };

  const handleEndEarly = async () => {
    setIsEndingEarly(true);
    cancelSpeech();
    stopListening();
    try {
      const res = await interviewsApi.endEarly(id);
      if (res.report_id) {
        navigate(`/reports/${res.report_id}`);
      } else {
        navigate('/history');
      }
    } catch (err) {
      console.error('Failed to end interview early:', err);
      setErrorMessage('Error ending interview.');
      setIsEndingEarly(false);
      setEndModalOpen(false);
    }
  };

  const toggleVoiceInput = () => {
    if (isListening) {
      stopListening();
    } else {
      cancelSpeech();
      startListening();
    }
  };

  const repeatQuestion = () => {
    if (currentQuestion) {
      speak(currentQuestion.question_text);
    }
  };

  const handleCopyCode = () => {
    if (currentQuestion?.code_snippet) {
      navigator.clipboard.writeText(currentQuestion.code_snippet);
      setCopiedSnippet(true);
      setTimeout(() => setCopiedSnippet(false), 2000);
    }
  };

  const progressPercent = Math.round(((currentNumber - 1) / totalQuestions) * 100);

  const getInterviewTypeBadge = () => {
    const type = interview?.interview_type || 'technical';
    if (type === 'hr') {
      return {
        label: 'HR Interview',
        color: '#818cf8',
        bg: 'rgba(99, 102, 241, 0.15)',
        border: 'rgba(99, 102, 241, 0.3)',
        icon: Users
      };
    } else if (type === 'combined') {
      return {
        label: 'Combined (HR + Tech)',
        color: '#c084fc',
        bg: 'rgba(192, 132, 252, 0.15)',
        border: 'rgba(192, 132, 252, 0.3)',
        icon: Sparkles
      };
    } else {
      return {
        label: 'Technical Interview',
        color: '#38bdf8',
        bg: 'rgba(56, 189, 248, 0.15)',
        border: 'rgba(56, 189, 248, 0.3)',
        icon: Code2
      };
    }
  };

  const typeBadge = getInterviewTypeBadge();
  const TypeIcon = typeBadge.icon;

  return (
    <div className="container" style={{ padding: '2rem 1.5rem', maxWidth: '900px', position: 'relative' }}>
      <div className="bg-glow-orb orb-primary" style={{ top: '10%', left: '20%' }} />

      {/* Top Bar: Role badge, progress, end interview button */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '1rem',
        marginBottom: '1.5rem',
        position: 'relative',
        zIndex: 1
      }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', flexWrap: 'wrap' }}>
            <span style={{
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.35rem',
              padding: '0.35rem 0.75rem',
              borderRadius: 'var(--radius-full)',
              background: typeBadge.bg,
              border: `1px solid ${typeBadge.border}`,
              color: typeBadge.color,
              fontSize: '0.8rem',
              fontWeight: 600
            }}>
              <TypeIcon size={14} />
              {typeBadge.label}
            </span>

            {interview?.is_demo && (
              <span className="badge badge-demo" style={{ padding: '0.35rem 0.75rem' }}>
                Practice Bank Mode
              </span>
            )}
          </div>
          <h2 style={{ fontSize: '1.45rem', fontWeight: 800, marginTop: '0.35rem', color: '#ffffff' }}>
            {interview?.custom_job_role || 'Target Role'}
          </h2>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
          {/* Mode Switcher */}
          <button
            type="button"
            onClick={() => setActiveMode(activeMode === 'voice' ? 'text' : 'voice')}
            className="btn btn-secondary btn-sm"
            title="Switch between Voice and Text mode"
          >
            {activeMode === 'voice' ? <Keyboard size={15} /> : <Mic size={15} />}
            {activeMode === 'voice' ? 'Switch to Text' : 'Switch to Voice'}
          </button>

          {/* End Interview Early Button */}
          <button
            type="button"
            onClick={() => setEndModalOpen(true)}
            className="btn btn-danger btn-sm"
            id="end-interview-early-btn"
          >
            <Flag size={15} /> End Interview
          </button>
        </div>
      </div>

      {/* Progress Bar & Question Counter */}
      <div className="glass-panel" style={{ padding: '1rem 1.5rem', marginBottom: '1.75rem', position: 'relative', zIndex: 1 }}>
        <div style={{ display: 'flex', justifyContent: 'space-between', alignItems: 'center', marginBottom: '0.5rem', fontSize: '0.85rem' }}>
          <span style={{ fontWeight: 600, color: 'var(--text-secondary)' }}>
            Question {currentNumber} of {totalQuestions}
          </span>
          <span style={{ fontWeight: 700, color: '#818cf8' }}>
            {progressPercent}% Complete
          </span>
        </div>
        <div style={{ height: '6px', width: '100%', background: 'rgba(255, 255, 255, 0.08)', borderRadius: '3px', overflow: 'hidden' }}>
          <div style={{
            height: '100%',
            width: `${Math.max(8, progressPercent)}%`,
            background: 'linear-gradient(90deg, #6366f1 0%, #38bdf8 100%)',
            borderRadius: '3px',
            transition: 'width 0.5s ease'
          }} />
        </div>
      </div>

      {/* Error or Alert Banner */}
      {(errorMessage || speechError) && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          justifyContent: 'space-between',
          padding: '0.85rem 1.25rem',
          borderRadius: 'var(--radius-md)',
          background: 'rgba(244, 63, 94, 0.15)',
          border: '1px solid rgba(244, 63, 94, 0.3)',
          color: '#fb7185',
          fontSize: '0.875rem',
          marginBottom: '1.5rem',
          position: 'relative',
          zIndex: 1
        }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
            <AlertCircle size={18} style={{ flexShrink: 0 }} />
            <span>{errorMessage || speechError}</span>
          </div>
          {errorMessage && (
            <button
              onClick={fetchNextQuestion}
              className="btn btn-secondary btn-sm"
              style={{ padding: '0.25rem 0.6rem', fontSize: '0.75rem' }}
            >
              Retry
            </button>
          )}
        </div>
      )}

      {/* Main Interview Box */}
      <div className="glass-panel" style={{ padding: '2.25rem', marginBottom: '1.75rem', position: 'relative', zIndex: 1 }}>
        {isLoadingQuestion ? (
          <div style={{ textAlign: 'center', padding: '3.5rem 1rem' }}>
            <Loader2 size={36} color="#818cf8" style={{ animation: 'spin 1s linear infinite', margin: '0 auto 1rem auto' }} />
            <h3 style={{ fontSize: '1.15rem', fontWeight: 600 }}>Formulating Next Question...</h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.85rem', marginTop: '0.35rem' }}>
              Retrieving verified questions tailored to {interview?.custom_job_role || 'your role'}
            </p>
            <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
          </div>
        ) : (
          <div>
            {/* AI Question Section */}
            <div style={{ marginBottom: '2rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem', flexWrap: 'wrap', gap: '0.5rem' }}>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  <div style={{
                    width: '26px',
                    height: '26px',
                    borderRadius: '50%',
                    background: currentQuestion?.is_technical ? 'linear-gradient(135deg, #0284c7 0%, #38bdf8 100%)' : 'linear-gradient(135deg, #6366f1 0%, #a855f7 100%)',
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'center'
                  }}>
                    {currentQuestion?.is_technical ? <Code2 size={13} color="#ffffff" /> : <Sparkles size={13} color="#ffffff" />}
                  </div>
                  <span style={{
                    fontSize: '0.8rem',
                    fontWeight: 700,
                    color: currentQuestion?.is_technical ? '#38bdf8' : '#a5b4fc',
                    textTransform: 'uppercase',
                    letterSpacing: '0.05em'
                  }}>
                    {currentQuestion?.is_technical ? 'Technical Question' : 'HR Behavioral Question'}
                    {currentQuestion?.is_follow_up ? ' (Follow-Up)' : ''}
                  </span>
                </div>

                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                  {/* Topic badge */}
                  {currentQuestion?.topic && (
                    <span style={{
                      fontSize: '0.75rem',
                      fontWeight: 600,
                      padding: '0.2rem 0.55rem',
                      borderRadius: 'var(--radius-sm)',
                      background: 'rgba(255, 255, 255, 0.06)',
                      border: '1px solid var(--border-subtle)',
                      color: 'var(--text-secondary)'
                    }}>
                      {currentQuestion.topic}
                    </span>
                  )}

                  {/* Difficulty badge */}
                  {currentQuestion?.difficulty && (
                    <span style={{
                      fontSize: '0.75rem',
                      fontWeight: 600,
                      padding: '0.2rem 0.55rem',
                      borderRadius: 'var(--radius-sm)',
                      background: currentQuestion.difficulty === 'hard' ? 'rgba(244, 63, 94, 0.15)' : 'rgba(99, 102, 241, 0.15)',
                      color: currentQuestion.difficulty === 'hard' ? '#fb7185' : '#818cf8',
                      textTransform: 'capitalize'
                    }}>
                      {currentQuestion.difficulty}
                    </span>
                  )}

                  {/* Speak / Repeat Voice Controls */}
                  <button
                    type="button"
                    onClick={repeatQuestion}
                    className="btn btn-secondary btn-sm"
                    title="Read question aloud"
                    style={{ padding: '0.3rem 0.65rem', fontSize: '0.75rem' }}
                  >
                    {isSpeaking ? <VolumeX size={14} color="#f43f5e" /> : <Volume2 size={14} color="#818cf8" />}
                    {isSpeaking ? 'Stop Audio' : 'Hear Question'}
                  </button>
                </div>
              </div>

              {/* Question Text */}
              <div style={{
                fontSize: '1.25rem',
                fontWeight: 600,
                lineHeight: 1.5,
                color: 'var(--text-primary)',
                background: 'rgba(13, 21, 39, 0.4)',
                padding: '1.25rem 1.5rem',
                borderRadius: 'var(--radius-md)',
                borderLeft: `4px solid ${currentQuestion?.is_technical ? '#38bdf8' : '#6366f1'}`
              }} id="ai-question-text">
                {currentQuestion?.question_text}
              </div>

              {/* Code Snippet Block (If technical question has code) */}
              {currentQuestion?.code_snippet && (
                <div style={{
                  marginTop: '1rem',
                  borderRadius: 'var(--radius-md)',
                  background: '#0a0f1d',
                  border: '1px solid rgba(56, 189, 248, 0.25)',
                  overflow: 'hidden'
                }}>
                  <div style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '0.5rem 1rem',
                    background: 'rgba(255, 255, 255, 0.03)',
                    borderBottom: '1px solid rgba(255, 255, 255, 0.06)'
                  }}>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', fontSize: '0.75rem', color: '#38bdf8', fontWeight: 600 }}>
                      <Terminal size={14} /> Code Reference / Example
                    </div>
                    <button
                      type="button"
                      onClick={handleCopyCode}
                      className="btn btn-secondary btn-sm"
                      style={{ padding: '0.2rem 0.5rem', fontSize: '0.7rem' }}
                    >
                      {copiedSnippet ? <Check size={12} color="#10b981" /> : <Copy size={12} />}
                      {copiedSnippet ? 'Copied' : 'Copy'}
                    </button>
                  </div>
                  <pre style={{
                    margin: 0,
                    padding: '1rem',
                    fontFamily: 'Consolas, Monaco, "Courier New", monospace',
                    fontSize: '0.875rem',
                    color: '#e2e8f0',
                    lineHeight: 1.5,
                    overflowX: 'auto',
                    whiteSpace: 'pre-wrap'
                  }}>
                    <code>{currentQuestion.code_snippet}</code>
                  </pre>
                </div>
              )}
            </div>

            {/* Answer Input Section */}
            <div>
              <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.65rem' }}>
                <label className="input-label" htmlFor="interview-answer-input" style={{ marginBottom: 0 }}>
                  {currentQuestion?.is_technical ? 'Your Technical Explanation / Code Solution' : 'Your Response (STAR Method: Situation, Task, Action, Result)'}
                </label>

                <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
                  {/* Monospace Code Toggle */}
                  <button
                    type="button"
                    onClick={() => setIsCodeFormat(!isCodeFormat)}
                    style={{
                      background: 'none',
                      border: 'none',
                      color: isCodeFormat ? '#38bdf8' : 'var(--text-muted)',
                      fontSize: '0.75rem',
                      cursor: 'pointer',
                      display: 'flex',
                      alignItems: 'center',
                      gap: '0.3rem',
                      fontWeight: 600
                    }}
                    title="Toggle code / monospace font"
                  >
                    <FileCode size={13} />
                    {isCodeFormat ? 'Code View: ON' : 'Code View: OFF'}
                  </button>

                  {activeMode === 'voice' && isListening && (
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.4rem', color: '#f43f5e', fontSize: '0.75rem', fontWeight: 700 }}>
                      <div style={{ width: '8px', height: '8px', borderRadius: '50%', background: '#f43f5e', animation: 'pulse 1s infinite' }} />
                      Listening...
                    </div>
                  )}
                </div>
              </div>

              <textarea
                id="interview-answer-input"
                className="input-field"
                placeholder={
                  activeMode === 'voice'
                    ? "Click 'Start Speaking' below to dictate, or type your answer here directly..."
                    : (currentQuestion?.is_technical
                        ? "Explain the mechanism, approach, syntax, time complexity, and practical edge cases..."
                        : "Type your detailed response here. Use the STAR framework: Situation, Task, Action, and Result...")
                }
                value={answerText}
                onChange={(e) => setAnswerText(e.target.value)}
                rows={isCodeFormat ? 8 : 6}
                disabled={isSubmitting}
                style={{
                  fontSize: '1rem',
                  lineHeight: 1.6,
                  fontFamily: isCodeFormat ? 'Consolas, Monaco, "Courier New", monospace' : 'inherit'
                }}
              />

              {/* Action Controls */}
              <div style={{
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'space-between',
                flexWrap: 'wrap',
                gap: '1rem',
                marginTop: '1.25rem'
              }}>
                {/* Voice Record Toggle */}
                {activeMode === 'voice' ? (
                  <button
                    type="button"
                    onClick={toggleVoiceInput}
                    className={`btn ${isListening ? 'btn-danger mic-recording' : 'btn-secondary'}`}
                    id="mic-toggle-btn"
                  >
                    {isListening ? <MicOff size={18} /> : <Mic size={18} />}
                    {isListening ? 'Stop Recording' : 'Start Speaking'}
                  </button>
                ) : (
                  <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                    {currentQuestion?.is_technical ? (
                      'Tip: Code snippets and SQL syntax are evaluated for logic, correctness, and edge cases.'
                    ) : (
                      'Tip: Use the STAR framework: Situation, Task, Action, and Result.'
                    )}
                  </div>
                )}

                {/* Submit Response Button */}
                <button
                  type="button"
                  onClick={handleSubmitAnswer}
                  className="btn btn-primary"
                  disabled={isSubmitting || !answerText.trim()}
                  id="submit-answer-btn"
                  style={{ minWidth: '160px' }}
                >
                  {isSubmitting ? (
                    <>
                      <Loader2 size={18} style={{ animation: 'spin 1s linear infinite' }} /> Submitting...
                    </>
                  ) : (
                    <>
                      <Send size={18} /> Submit Answer
                    </>
                  )}
                </button>
              </div>
            </div>
          </div>
        )}
      </div>

      {/* Confirmation Modal for Ending Early */}
      <ConfirmModal
        isOpen={endModalOpen}
        title="End Interview Early?"
        message="Are you sure you want to end this interview? All answers submitted so far will be evaluated and an interim report will be prepared for you."
        confirmText="Yes, End Interview"
        cancelText="Continue Practicing"
        isDanger={true}
        isLoading={isEndingEarly}
        onConfirm={handleEndEarly}
        onCancel={() => setEndModalOpen(false)}
      />
    </div>
  );
};
export default InterviewRoomPage;
