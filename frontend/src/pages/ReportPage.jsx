import React, { useState, useEffect } from 'react';
import { useParams, Link, useNavigate } from 'react-router-dom';
import { reportsApi } from '../api/reports';
import { ScoreGauge } from '../components/ScoreGauge';
import { CriteriaCard } from '../components/CriteriaCard';
import confetti from 'canvas-confetti';
import {
  Sparkles,
  Printer,
  RotateCcw,
  LayoutDashboard,
  CheckCircle2,
  AlertCircle,
  Lightbulb,
  ArrowRight,
  BookOpen,
  MessageSquare,
  Award,
  ChevronDown,
  ChevronUp,
  Briefcase,
  Code2,
  Users,
  Terminal,
  Check,
  XCircle,
  Compass
} from 'lucide-react';

export const ReportPage = () => {
  const { id } = useParams();
  const navigate = useNavigate();

  const [report, setReport] = useState(null);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);
  const [expandedQuestions, setExpandedQuestions] = useState({});

  useEffect(() => {
    fetchReport();
  }, [id]);

  const fetchReport = async () => {
    setIsLoading(true);
    setError(null);
    try {
      const data = await reportsApi.getReport(id);
      setReport(data);

      // Expand first question by default
      if (data.qa_breakdown && data.qa_breakdown.length > 0) {
        setExpandedQuestions({ [data.qa_breakdown[0].id]: true });
      }

      // Confetti celebration if overall score >= 75
      if (data.overall_practice_score >= 75) {
        try {
          confetti({
            particleCount: 80,
            spread: 70,
            origin: { y: 0.6 }
          });
        } catch (e) {
          // ignore
        }
      }
    } catch (err) {
      console.error('Failed to load report:', err);
      setError('Could not load interview report. It may still be processing or was not found.');
    } finally {
      setIsLoading(false);
    }
  };

  const toggleQuestion = (qId) => {
    setExpandedQuestions((prev) => ({
      ...prev,
      [qId]: !prev[qId]
    }));
  };

  const handlePrint = () => {
    window.print();
  };

  if (isLoading) {
    return (
      <div style={{ textAlign: 'center', padding: '6rem 1rem', color: 'var(--text-secondary)' }}>
        <div style={{
          width: '44px',
          height: '44px',
          borderRadius: '50%',
          border: '3px solid rgba(99, 102, 241, 0.2)',
          borderTopColor: '#6366f1',
          animation: 'spin 1s linear infinite',
          margin: '0 auto 1.5rem auto'
        }} />
        <h3 className="heading-3">Synthesizing Evaluation Report...</h3>
        <p style={{ fontSize: '0.875rem', marginTop: '0.5rem' }}>
          Analyzing technical accuracy, problem solving, STAR structure, and behavioral poise
        </p>
        <style>{`@keyframes spin { to { transform: rotate(360deg); } }`}</style>
      </div>
    );
  }

  if (error || !report) {
    return (
      <div className="container" style={{ padding: '4rem 1rem', textAlign: 'center', maxWidth: '540px' }}>
        <div className="glass-panel" style={{ padding: '2.5rem' }}>
          <AlertCircle size={44} color="#fb7185" style={{ margin: '0 auto 1rem auto' }} />
          <h2 className="heading-2" style={{ marginBottom: '0.5rem' }}>Report Unavailable</h2>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginBottom: '1.5rem' }}>
            {error || 'Unable to display report.'}
          </p>
          <Link to="/dashboard" className="btn btn-primary">
            Back to Dashboard
          </Link>
        </div>
      </div>
    );
  }

  const roleTitle = report.custom_job_role || 'Target Role';
  const interviewType = report.interview_type || 'technical';
  const isCombined = interviewType === 'combined';
  const isTechnical = interviewType === 'technical';
  const isHR = interviewType === 'hr';

  return (
    <div className="container" style={{ padding: '2.5rem 1.5rem', maxWidth: '1000px', position: 'relative' }}>
      <div className="bg-glow-orb orb-primary" style={{ top: 0, right: '20%' }} />

      {/* Top Action Bar */}
      <div style={{
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'space-between',
        flexWrap: 'wrap',
        gap: '1rem',
        marginBottom: '2rem',
        position: 'relative',
        zIndex: 1
      }}>
        <div>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '0.35rem', flexWrap: 'wrap' }}>
            <span className="badge badge-emerald">
              {report.is_complete ? 'Complete Session Report' : 'Incomplete / Early Concluded Session'}
            </span>

            <span style={{
              fontSize: '0.75rem',
              fontWeight: 700,
              padding: '0.2rem 0.65rem',
              borderRadius: 'var(--radius-full)',
              background: isTechnical ? 'rgba(56, 189, 248, 0.15)' : (isCombined ? 'rgba(192, 132, 252, 0.15)' : 'rgba(99, 102, 241, 0.15)'),
              border: `1px solid ${isTechnical ? 'rgba(56, 189, 248, 0.3)' : (isCombined ? 'rgba(192, 132, 252, 0.3)' : 'rgba(99, 102, 241, 0.3)')}`,
              color: isTechnical ? '#38bdf8' : (isCombined ? '#c084fc' : '#818cf8'),
              display: 'inline-flex',
              alignItems: 'center',
              gap: '0.35rem'
            }}>
              {isTechnical && <Code2 size={13} />}
              {isCombined && <Sparkles size={13} />}
              {isHR && <Users size={13} />}
              {isCombined ? 'Combined (HR + Technical)' : (isTechnical ? 'Technical Interview' : 'HR Interview')}
            </span>

            {report.is_demo && (
              <span className="badge badge-demo">Practice Bank AI</span>
            )}
          </div>

          <h1 className="heading-1">
            {isCombined ? 'Combined Practice Evaluation' : (isTechnical ? 'Technical Interview Evaluation' : 'HR Performance Evaluation')}
          </h1>

          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', fontSize: '0.85rem', color: 'var(--text-secondary)', marginTop: '0.25rem', flexWrap: 'wrap' }}>
            <span style={{ fontWeight: 600, color: '#ffffff' }}>{roleTitle}</span>
            <span>&bull;</span>
            <span style={{ textTransform: 'capitalize' }}>{report.experience_level}</span>
            <span>&bull;</span>
            <span>{report.total_questions_answered} of {report.total_configured_questions} questions answered</span>
            <span>&bull;</span>
            <span>{report.created_at}</span>
          </div>
        </div>

        <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }} className="no-print">
          <button
            onClick={handlePrint}
            className="btn btn-secondary btn-sm"
            title="Print or export as PDF"
          >
            <Printer size={15} /> Print Report
          </button>
          <Link
            to={`/interview/setup?role=${encodeURIComponent(roleTitle)}`}
            className="btn btn-primary btn-sm"
          >
            <RotateCcw size={15} /> Practise Again
          </Link>
          <Link
            to="/dashboard"
            className="btn btn-secondary btn-sm"
          >
            <LayoutDashboard size={15} /> Dashboard
          </Link>
        </div>
      </div>

      {/* Hero Score Section */}
      <div className="glass-panel" style={{ padding: '2.5rem', marginBottom: '2rem', position: 'relative', zIndex: 1 }}>
        <div style={{
          display: 'grid',
          gridTemplateColumns: isCombined ? 'auto 1fr' : 'auto 1fr',
          gap: '2.5rem',
          alignItems: 'center'
        }} className="report-hero-grid">
          {/* Main Gauges */}
          <div style={{ display: 'flex', flexDirection: 'column', alignItems: 'center', gap: '1.25rem' }}>
            <ScoreGauge
              score={report.overall_practice_score || 0}
              size={175}
              label="Overall Practice Score"
            />

            {/* Separate HR & Technical Sub-Scores for Combined Mode */}
            {isCombined && (
              <div style={{
                display: 'grid',
                gridTemplateColumns: '1fr 1fr',
                gap: '0.75rem',
                width: '100%',
                paddingTop: '0.75rem',
                borderTop: '1px solid var(--border-subtle)'
              }}>
                <div style={{
                  padding: '0.65rem',
                  borderRadius: 'var(--radius-sm)',
                  background: 'rgba(99, 102, 241, 0.1)',
                  border: '1px solid rgba(99, 102, 241, 0.25)',
                  textAlign: 'center'
                }}>
                  <span style={{ fontSize: '0.7rem', color: '#a5b4fc', fontWeight: 600, textTransform: 'uppercase', display: 'block' }}>
                    HR Score
                  </span>
                  <span style={{ fontSize: '1.25rem', fontWeight: 800, color: '#818cf8' }}>
                    {report.hr_score !== null ? `${report.hr_score}%` : 'N/A'}
                  </span>
                </div>

                <div style={{
                  padding: '0.65rem',
                  borderRadius: 'var(--radius-sm)',
                  background: 'rgba(56, 189, 248, 0.1)',
                  border: '1px solid rgba(56, 189, 248, 0.25)',
                  textAlign: 'center'
                }}>
                  <span style={{ fontSize: '0.7rem', color: '#7dd3fc', fontWeight: 600, textTransform: 'uppercase', display: 'block' }}>
                    Technical Score
                  </span>
                  <span style={{ fontSize: '1.25rem', fontWeight: 800, color: '#38bdf8' }}>
                    {report.technical_score !== null ? `${report.technical_score}%` : 'N/A'}
                  </span>
                </div>
              </div>
            )}
          </div>

          <div>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: isTechnical ? '#38bdf8' : '#818cf8', marginBottom: '0.5rem' }}>
              <Award size={18} />
              <span style={{ fontWeight: 700, fontSize: '0.8rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                Performance Assessment
              </span>
            </div>
            <h3 className="heading-3" style={{ marginBottom: '0.75rem', fontSize: '1.35rem' }}>
              {roleTitle} Readiness Summary
            </h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', lineHeight: 1.6 }}>
              {report.summary}
            </p>
            <div style={{ marginTop: '1rem', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              Notice: Practice feedback is calibrated for interview training and skill diagnostic purposes; it does not constitute a guarantee of real-world hiring outcomes.
            </div>
          </div>
        </div>
      </div>

      {/* Criteria Breakdown */}
      <div style={{ marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
        <h3 className="heading-2" style={{ marginBottom: '1.25rem', fontSize: '1.25rem' }}>
          {isTechnical ? 'Technical Rubric Breakdown' : (isCombined ? 'Evaluation Rubric Breakdown' : 'HR Weighted Evaluation Breakdown')}
        </h3>

        {/* Technical or Combined Technical Criteria */}
        {(isTechnical || isCombined) && report.avg_technical_accuracy !== null && (
          <div style={{ marginBottom: '1.5rem' }}>
            <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'block', marginBottom: '0.75rem' }}>
              Technical Criteria
            </span>
            <div className="grid-4">
              <div className="glass-panel" style={{ padding: '1.25rem', textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600 }}>Technical Accuracy (35%)</span>
                <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#38bdf8', marginTop: '0.25rem' }}>
                  {report.avg_technical_accuracy !== null ? `${report.avg_technical_accuracy}%` : 'N/A'}
                </div>
              </div>
              <div className="glass-panel" style={{ padding: '1.25rem', textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600 }}>Technical Depth (30%)</span>
                <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#818cf8', marginTop: '0.25rem' }}>
                  {report.avg_technical_depth !== null ? `${report.avg_technical_depth}%` : 'N/A'}
                </div>
              </div>
              <div className="glass-panel" style={{ padding: '1.25rem', textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600 }}>Problem Solving / Edge Cases (25%)</span>
                <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#a855f7', marginTop: '0.25rem' }}>
                  {report.avg_problem_solving !== null ? `${report.avg_problem_solving}%` : 'N/A'}
                </div>
              </div>
              <div className="glass-panel" style={{ padding: '1.25rem', textAlign: 'center' }}>
                <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', fontWeight: 600 }}>Clarity & Explanation (10%)</span>
                <div style={{ fontSize: '1.6rem', fontWeight: 800, color: '#10b981', marginTop: '0.25rem' }}>
                  {report.avg_clarity_score !== null ? `${report.avg_clarity_score}%` : 'N/A'}
                </div>
              </div>
            </div>
          </div>
        )}

        {/* HR Criteria for HR or Combined */}
        {(isHR || (isCombined && report.avg_relevance_score !== null)) && (
          <div>
            {isCombined && (
              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#818cf8', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'block', marginBottom: '0.75rem' }}>
                HR & Behavioral Criteria
              </span>
            )}
            <div className="grid-4">
              <CriteriaCard type="relevance" score={report.avg_relevance_score} />
              <CriteriaCard type="clarity" score={report.avg_clarity_score} />
              <CriteriaCard type="examples" score={report.avg_examples_score} />
              <CriteriaCard type="communication" score={report.avg_communication_score} />
            </div>
          </div>
        )}
      </div>

      {/* Strengths & Improvement Areas Grid */}
      {isCombined ? (
        <div style={{ display: 'flex', flexDirection: 'column', gap: '1.5rem', marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
          {/* Technical Section */}
          <div className="grid-2">
            <div className="glass-panel" style={{ padding: '2rem', borderLeft: '4px solid #38bdf8' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
                <Code2 size={20} color="#38bdf8" />
                <h3 className="heading-3" style={{ color: '#38bdf8' }}>Technical Strengths</h3>
              </div>
              <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
                {(report.technical_strengths?.length ? report.technical_strengths : report.strengths || []).map((str, idx) => (
                  <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                    <CheckCircle2 size={16} color="#38bdf8" style={{ flexShrink: 0, marginTop: '3px' }} />
                    <span>{str}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="glass-panel" style={{ padding: '2rem', borderLeft: '4px solid #f59e0b' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
                <Terminal size={20} color="#f59e0b" />
                <h3 className="heading-3" style={{ color: '#fcd34d' }}>Technical Areas for Improvement</h3>
              </div>
              <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
                {(report.technical_areas_for_improvement?.length ? report.technical_areas_for_improvement : report.areas_for_improvement || []).map((imp, idx) => (
                  <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                    <Lightbulb size={16} color="#f59e0b" style={{ flexShrink: 0, marginTop: '3px' }} />
                    <span>{imp}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>

          {/* HR Section */}
          <div className="grid-2">
            <div className="glass-panel" style={{ padding: '2rem', borderLeft: '4px solid #818cf8' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
                <Users size={20} color="#818cf8" />
                <h3 className="heading-3" style={{ color: '#a5b4fc' }}>HR Behavioral Strengths</h3>
              </div>
              <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
                {(report.hr_strengths?.length ? report.hr_strengths : report.strengths || []).map((str, idx) => (
                  <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                    <CheckCircle2 size={16} color="#818cf8" style={{ flexShrink: 0, marginTop: '3px' }} />
                    <span>{str}</span>
                  </li>
                ))}
              </ul>
            </div>

            <div className="glass-panel" style={{ padding: '2rem', borderLeft: '4px solid #fb7185' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
                <AlertCircle size={20} color="#fb7185" />
                <h3 className="heading-3" style={{ color: '#fb7185' }}>HR Areas for Improvement</h3>
              </div>
              <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
                {(report.hr_areas_for_improvement?.length ? report.hr_areas_for_improvement : report.areas_for_improvement || []).map((imp, idx) => (
                  <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                    <Lightbulb size={16} color="#fb7185" style={{ flexShrink: 0, marginTop: '3px' }} />
                    <span>{imp}</span>
                  </li>
                ))}
              </ul>
            </div>
          </div>
        </div>
      ) : (
        <div className="grid-2" style={{ marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
          {/* Strengths */}
          <div className="glass-panel" style={{ padding: '2rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
              <div style={{ width: '32px', height: '32px', borderRadius: '8px', background: 'rgba(16, 185, 129, 0.15)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#10b981' }}>
                <CheckCircle2 size={18} />
              </div>
              <h3 className="heading-3" style={{ color: '#6ee7b7' }}>Key Strengths Demonstrated</h3>
            </div>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
              {report.strengths && report.strengths.map((str, idx) => (
                <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                  <CheckCircle2 size={16} color="#10b981" style={{ flexShrink: 0, marginTop: '3px' }} />
                  <span>{str}</span>
                </li>
              ))}
            </ul>
          </div>

          {/* Improvement Areas */}
          <div className="glass-panel" style={{ padding: '2rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
              <div style={{ width: '32px', height: '32px', borderRadius: '8px', background: 'rgba(245, 158, 11, 0.15)', display: 'flex', alignItems: 'center', justifyContent: 'center', color: '#f59e0b' }}>
                <Lightbulb size={18} />
              </div>
              <h3 className="heading-3" style={{ color: '#fcd34d' }}>Primary Areas for Improvement</h3>
            </div>
            <ul style={{ listStyle: 'none', display: 'flex', flexDirection: 'column', gap: '0.85rem' }}>
              {report.areas_for_improvement && report.areas_for_improvement.map((imp, idx) => (
                <li key={idx} style={{ display: 'flex', alignItems: 'flex-start', gap: '0.6rem', fontSize: '0.9rem', color: 'var(--text-secondary)', lineHeight: 1.5 }}>
                  <Lightbulb size={16} color="#f59e0b" style={{ flexShrink: 0, marginTop: '3px' }} />
                  <span>{imp}</span>
                </li>
              ))}
            </ul>
          </div>
        </div>
      )}

      {/* Recommended Topics To Practice Next */}
      {report.recommended_topics && report.recommended_topics.length > 0 && (
        <div className="glass-panel" style={{ padding: '1.75rem', marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1rem' }}>
            <BookOpen size={18} color="#818cf8" />
            <h3 className="heading-3">Recommended Topics to Practise Next</h3>
          </div>
          <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.6rem' }}>
            {report.recommended_topics.map((topic, idx) => (
              <span key={idx} className="chip" style={{
                background: 'rgba(99, 102, 241, 0.12)',
                color: '#c7d2fe',
                borderColor: 'rgba(99, 102, 241, 0.3)'
              }}>
                {topic}
              </span>
            ))}
          </div>
        </div>
      )}

      {/* Question-By-Question Detailed Breakdown */}
      <div style={{ marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
        <h3 className="heading-2" style={{ marginBottom: '1.25rem', fontSize: '1.25rem' }}>
          Question-by-Question Evaluation & Rubric
        </h3>

        {report.qa_breakdown && report.qa_breakdown.length > 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
            {report.qa_breakdown.map((item, idx) => {
              const isExpanded = !!expandedQuestions[item.id];
              const evalObj = item.evaluation;
              const isTechQ = item.is_technical;

              return (
                <div key={item.id} className="glass-panel" style={{ overflow: 'hidden' }}>
                  {/* Collapsible Header */}
                  <div
                    onClick={() => toggleQuestion(item.id)}
                    style={{
                      padding: '1.25rem 1.75rem',
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'space-between',
                      cursor: 'pointer',
                      background: 'rgba(13, 21, 39, 0.5)',
                      flexWrap: 'wrap',
                      gap: '0.75rem'
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', flex: 1, minWidth: '240px' }}>
                      <span style={{
                        width: '28px',
                        height: '28px',
                        borderRadius: '50%',
                        background: isTechQ ? 'rgba(56, 189, 248, 0.2)' : 'rgba(99, 102, 241, 0.2)',
                        color: isTechQ ? '#38bdf8' : '#818cf8',
                        fontWeight: 700,
                        fontSize: '0.85rem',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center',
                        flexShrink: 0
                      }}>
                        {item.question_order}
                      </span>
                      <div>
                        <div style={{ fontWeight: 600, fontSize: '0.95rem', color: 'var(--text-primary)' }}>
                          {item.question_text}
                        </div>
                        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginTop: '0.2rem', flexWrap: 'wrap' }}>
                          <span style={{
                            fontSize: '0.7rem',
                            fontWeight: 700,
                            padding: '0.1rem 0.45rem',
                            borderRadius: '4px',
                            background: isTechQ ? 'rgba(56, 189, 248, 0.15)' : 'rgba(99, 102, 241, 0.15)',
                            color: isTechQ ? '#38bdf8' : '#818cf8'
                          }}>
                            {isTechQ ? 'Technical' : 'HR Behavioral'}
                          </span>
                          {item.topic && (
                            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                              Topic: {item.topic}
                            </span>
                          )}
                          {item.difficulty && (
                            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                              &bull; {item.difficulty}
                            </span>
                          )}
                          {item.is_voice && (
                            <span style={{ fontSize: '0.75rem', color: '#38bdf8' }}>
                              &bull; Voice Answer
                            </span>
                          )}
                        </div>
                      </div>
                    </div>

                    <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                      {evalObj && (
                        <div style={{
                          fontSize: '1.2rem',
                          fontWeight: 800,
                          color: evalObj.overall_score >= 80 ? '#10b981' : evalObj.overall_score >= 60 ? '#6366f1' : '#f59e0b'
                        }}>
                          {evalObj.overall_score}%
                        </div>
                      )}
                      {isExpanded ? <ChevronUp size={20} color="var(--text-muted)" /> : <ChevronDown size={20} color="var(--text-muted)" />}
                    </div>
                  </div>

                  {/* Expanded Content */}
                  {isExpanded && (
                    <div style={{ padding: '1.75rem', borderTop: '1px solid var(--border-subtle)' }}>
                      {/* Code Snippet from question if present */}
                      {item.code_snippet && (
                        <div style={{ marginBottom: '1.5rem' }}>
                          <span style={{ fontSize: '0.75rem', fontWeight: 600, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                            Reference Code / Snippet:
                          </span>
                          <pre style={{
                            marginTop: '0.4rem',
                            padding: '1rem',
                            background: '#0a0f1d',
                            borderRadius: 'var(--radius-md)',
                            fontFamily: 'Consolas, Monaco, monospace',
                            fontSize: '0.85rem',
                            color: '#e2e8f0',
                            overflowX: 'auto',
                            border: '1px solid rgba(56, 189, 248, 0.2)'
                          }}>
                            <code>{item.code_snippet}</code>
                          </pre>
                        </div>
                      )}

                      {/* Candidate Answer */}
                      <div style={{ marginBottom: '1.5rem' }}>
                        <span style={{ fontSize: '0.8rem', fontWeight: 600, color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                          Your Submitted Answer:
                        </span>
                        <div style={{
                          marginTop: '0.4rem',
                          padding: '1rem',
                          background: 'rgba(7, 11, 20, 0.6)',
                          borderRadius: 'var(--radius-md)',
                          fontSize: '0.925rem',
                          color: 'var(--text-primary)',
                          lineHeight: 1.6,
                          borderLeft: `3px solid ${isTechQ ? '#38bdf8' : '#818cf8'}`,
                          whiteSpace: 'pre-wrap',
                          fontFamily: isTechQ ? 'Consolas, Monaco, monospace' : 'inherit'
                        }}>
                          "{item.answer_text}"
                        </div>
                      </div>

                      {/* Criteria Scores for this answer */}
                      {evalObj && (
                        <div style={{ marginBottom: '1.5rem' }}>
                          {isTechQ ? (
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '0.75rem' }} className="grid-4">
                              <div style={{ padding: '0.75rem', background: 'rgba(56, 189, 248, 0.08)', borderRadius: 'var(--radius-sm)', textAlign: 'center', border: '1px solid rgba(56, 189, 248, 0.15)' }}>
                                <span style={{ fontSize: '0.7rem', color: '#7dd3fc' }}>Accuracy (35%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#38bdf8' }}>{evalObj.technical_accuracy_score ?? 'N/A'}%</div>
                              </div>
                              <div style={{ padding: '0.75rem', background: 'rgba(129, 140, 248, 0.08)', borderRadius: 'var(--radius-sm)', textAlign: 'center', border: '1px solid rgba(129, 140, 248, 0.15)' }}>
                                <span style={{ fontSize: '0.7rem', color: '#a5b4fc' }}>Depth (30%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#818cf8' }}>{evalObj.technical_depth_score ?? 'N/A'}%</div>
                              </div>
                              <div style={{ padding: '0.75rem', background: 'rgba(168, 85, 247, 0.08)', borderRadius: 'var(--radius-sm)', textAlign: 'center', border: '1px solid rgba(168, 85, 247, 0.15)' }}>
                                <span style={{ fontSize: '0.7rem', color: '#d8b4fe' }}>Problem Solving (25%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#a855f7' }}>{evalObj.problem_solving_score ?? 'N/A'}%</div>
                              </div>
                              <div style={{ padding: '0.75rem', background: 'rgba(16, 185, 129, 0.08)', borderRadius: 'var(--radius-sm)', textAlign: 'center', border: '1px solid rgba(16, 185, 129, 0.15)' }}>
                                <span style={{ fontSize: '0.7rem', color: '#6ee7b7' }}>Clarity (10%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#10b981' }}>{evalObj.clarity_score ?? 'N/A'}%</div>
                              </div>
                            </div>
                          ) : (
                            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(4, 1fr)', gap: '0.75rem' }} className="grid-4">
                              <div style={{ padding: '0.75rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Relevance (30%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#6366f1' }}>{evalObj.relevance_score}%</div>
                              </div>
                              <div style={{ padding: '0.75rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Clarity (25%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#8b5cf6' }}>{evalObj.clarity_score}%</div>
                              </div>
                              <div style={{ padding: '0.75rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Examples/STAR (25%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#06b6d4' }}>{evalObj.examples_score}%</div>
                              </div>
                              <div style={{ padding: '0.75rem', background: 'rgba(255, 255, 255, 0.03)', borderRadius: 'var(--radius-sm)', textAlign: 'center' }}>
                                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Communication (20%)</span>
                                <div style={{ fontSize: '1.1rem', fontWeight: 700, color: '#10b981' }}>{evalObj.communication_score}%</div>
                              </div>
                            </div>
                          )}
                        </div>
                      )}

                      {/* Technical Correct Points and Missing Points */}
                      {isTechQ && evalObj && (
                        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1rem', marginBottom: '1.25rem' }}>
                          {evalObj.correct_points && evalObj.correct_points.length > 0 && (
                            <div style={{
                              padding: '1rem',
                              borderRadius: 'var(--radius-md)',
                              background: 'rgba(16, 185, 129, 0.08)',
                              border: '1px solid rgba(16, 185, 129, 0.2)'
                            }}>
                              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#10b981', display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.5rem' }}>
                                <Check size={14} /> Correct Key Points Identified:
                              </span>
                              <ul style={{ margin: 0, paddingLeft: '1.2rem', color: 'var(--text-secondary)', fontSize: '0.85rem', lineHeight: 1.5 }}>
                                {evalObj.correct_points.map((pt, i) => (
                                  <li key={i}>{pt}</li>
                                ))}
                              </ul>
                            </div>
                          )}

                          {evalObj.missing_points && evalObj.missing_points.length > 0 && (
                            <div style={{
                              padding: '1rem',
                              borderRadius: 'var(--radius-md)',
                              background: 'rgba(245, 158, 11, 0.08)',
                              border: '1px solid rgba(245, 158, 11, 0.2)'
                            }}>
                              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#f59e0b', display: 'flex', alignItems: 'center', gap: '0.4rem', marginBottom: '0.5rem' }}>
                                <XCircle size={14} /> Missing or Incomplete Nuances:
                              </span>
                              <ul style={{ margin: 0, paddingLeft: '1.2rem', color: 'var(--text-secondary)', fontSize: '0.85rem', lineHeight: 1.5 }}>
                                {evalObj.missing_points.map((pt, i) => (
                                  <li key={i}>{pt}</li>
                                ))}
                              </ul>
                            </div>
                          )}
                        </div>
                      )}

                      {/* Explanation of Correct Solution if present */}
                      {isTechQ && (evalObj?.correct_answer_explanation || item.expected_answer) && (
                        <div style={{
                          marginBottom: '1.25rem',
                          padding: '1rem',
                          borderRadius: 'var(--radius-md)',
                          background: 'rgba(56, 189, 248, 0.06)',
                          border: '1px solid rgba(56, 189, 248, 0.2)'
                        }}>
                          <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#38bdf8', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'block', marginBottom: '0.25rem' }}>
                            Core Answer Rubric & Explanation:
                          </span>
                          <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.5, margin: 0 }}>
                            {evalObj?.correct_answer_explanation || item.expected_answer}
                          </p>
                        </div>
                      )}

                      {/* Feedback & Improvement */}
                      {evalObj && (
                        <div style={{ display: 'flex', flexDirection: 'column', gap: '0.85rem', fontSize: '0.875rem' }}>
                          <div>
                            <strong style={{ color: '#6ee7b7' }}>What went well: </strong>
                            <span style={{ color: 'var(--text-secondary)' }}>{evalObj.what_went_well}</span>
                          </div>

                          <div>
                            <strong style={{ color: '#fcd34d' }}>What could be improved: </strong>
                            <span style={{ color: 'var(--text-secondary)' }}>{evalObj.what_could_improve}</span>
                          </div>

                          <div>
                            <strong style={{ color: '#a5b4fc' }}>Actionable advice: </strong>
                            <span style={{ color: 'var(--text-secondary)' }}>{evalObj.improvement_suggestions}</span>
                          </div>

                          {evalObj.suggested_answer_structure && (
                            <div style={{
                              marginTop: '0.5rem',
                              padding: '1rem',
                              background: 'rgba(99, 102, 241, 0.08)',
                              borderRadius: 'var(--radius-md)',
                              border: '1px dashed rgba(99, 102, 241, 0.3)'
                            }}>
                              <span style={{ fontSize: '0.75rem', fontWeight: 700, color: '#a5b4fc', textTransform: 'uppercase', letterSpacing: '0.05em', display: 'block', marginBottom: '0.25rem' }}>
                                {isTechQ ? 'Improved Sample Code / Architecture Solution:' : 'Model Answer Example / Structure:'}
                              </span>
                              <p style={{ color: 'var(--text-primary)', fontStyle: isTechQ ? 'normal' : 'italic', lineHeight: 1.5, fontFamily: isTechQ ? 'Consolas, Monaco, monospace' : 'inherit' }}>
                                {evalObj.suggested_answer_structure}
                              </p>
                            </div>
                          )}
                        </div>
                      )}
                    </div>
                  )}
                </div>
              );
            })}
          </div>
        ) : (
          <p style={{ color: 'var(--text-muted)' }}>No questions were answered during this session.</p>
        )}
      </div>

      {/* Model Answer from synthesized report if present */}
      {report.sample_improved_answer && report.sample_improved_answer !== 'N/A' && (
        <div className="glass-panel-accent" style={{ padding: '2rem', marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.75rem', color: isTechnical ? '#38bdf8' : '#818cf8' }}>
            <Sparkles size={18} />
            <h3 className="heading-3">
              {isTechnical ? `Model Technical Blueprint for ${roleTitle}` : `Comprehensive Model Example for ${roleTitle}`}
            </h3>
          </div>
          <p style={{ color: 'var(--text-primary)', fontSize: '0.95rem', lineHeight: 1.6, fontStyle: isTechnical ? 'normal' : 'italic' }}>
            {report.sample_improved_answer}
          </p>
        </div>
      )}

      {/* Bottom Practice Again CTA */}
      <div style={{ textAlign: 'center', padding: '2rem 0' }} className="no-print">
        <Link
          to={`/interview/setup?role=${encodeURIComponent(roleTitle)}`}
          className="btn btn-primary btn-lg"
          id="report-practise-again-btn"
        >
          <RotateCcw size={18} /> Practise Another {roleTitle} Round
        </Link>
      </div>

      <style>{`
        @media (max-width: 768px) {
          .report-hero-grid { grid-template-columns: 1fr !important; text-align: center; }
        }
      `}</style>
    </div>
  );
};
export default ReportPage;
