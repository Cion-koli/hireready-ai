import React, { useState, useEffect } from 'react';
import { useNavigate, useSearchParams } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { interviewsApi } from '../api/interviews';
import {
  Briefcase,
  Layers,
  Gauge,
  Mic,
  MessageSquare,
  HelpCircle,
  FileText,
  FileCode,
  Sparkles,
  ArrowRight,
  AlertCircle,
  CheckCircle,
  Sliders,
  Code2,
  Users,
  Compass,
  CheckSquare
} from 'lucide-react';

const SUGGESTED_ROLES = [
  'Software Engineer',
  'Python Developer',
  'Frontend Developer',
  'Backend Developer',
  'Full-Stack Developer',
  'Data Analyst',
  'Java Developer',
  'React Developer',
  'SQL Developer',
  'QA / Software Tester',
  'DevOps Engineer',
  'Cybersecurity Analyst',
  'HR Executive',
  'Digital Marketing Executive',
  'Other / Custom Role'
];

const SE_TECHNOLOGIES = [
  { id: 'python', label: 'Python', desc: 'OOP, generators, decorators, memory' },
  { id: 'html', label: 'HTML', desc: 'DOM, semantics, accessibility, forms' },
  { id: 'css', label: 'CSS', desc: 'Flexbox, Grid, responsive, box model' },
  { id: 'javascript', label: 'JavaScript', desc: 'Closures, async/await, ES6, events' },
  { id: 'sql', label: 'SQL', desc: 'Joins, window functions, CTEs, indexing' },
];

export const InterviewSetupPage = () => {
  const navigate = useNavigate();
  const [searchParams] = useSearchParams();
  const { user } = useAuth();

  // Form State
  const [interviewType, setInterviewType] = useState('technical');
  const [customRole, setCustomRole] = useState(
    searchParams.get('role') || user?.profile?.target_role || 'Software Engineer'
  );
  const [selectedTechnologies, setSelectedTechnologies] = useState([
    'python', 'html', 'css', 'javascript', 'sql'
  ]);
  const [experienceLevel, setExperienceLevel] = useState(
    user?.profile?.default_experience_level || 'entry'
  );
  const [difficulty, setDifficulty] = useState('medium');
  const [interviewMode, setInterviewMode] = useState(
    user?.profile?.preferred_mode || 'text'
  );
  const [questionCount, setQuestionCount] = useState(5);

  // Optional Context
  const [jobDescription, setJobDescription] = useState('');
  const [resumeText, setResumeText] = useState('');
  const [interviewFocus, setInterviewFocus] = useState('');
  const [showOptional, setShowOptional] = useState(false);

  const [isLoading, setIsLoading] = useState(false);
  const [error, setError] = useState(null);

  const isSoftwareEngineer = customRole.trim().toLowerCase() === 'software engineer';
  const showTechSelector = isSoftwareEngineer && interviewType !== 'hr';

  const handleTechToggle = (techId) => {
    if (selectedTechnologies.includes(techId)) {
      if (selectedTechnologies.length === 1) {
        return; // Keep at least one technology selected
      }
      setSelectedTechnologies(selectedTechnologies.filter((t) => t !== techId));
    } else {
      setSelectedTechnologies([...selectedTechnologies, techId]);
    }
  };

  const handleSelectAllTech = () => {
    setSelectedTechnologies(['python', 'html', 'css', 'javascript', 'sql']);
  };

  const handleSelectSingleTech = (techId) => {
    setSelectedTechnologies([techId]);
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    setError(null);

    const trimmedRole = customRole.trim();
    if (!trimmedRole || trimmedRole.length < 2) {
      setError('Please enter a valid job title (at least 2 characters).');
      return;
    }

    setIsLoading(true);
    try {
      const payload = {
        interview_type: interviewType,
        custom_job_role: trimmedRole,
        selected_technologies: showTechSelector ? selectedTechnologies : [],
        experience_level: experienceLevel,
        difficulty: difficulty,
        interview_mode: interviewMode,
        question_count: questionCount,
        job_description: jobDescription.trim(),
        resume_text: resumeText.trim(),
        interview_focus: interviewFocus.trim(),
      };

      const interview = await interviewsApi.create(payload);

      // Start the interview session
      await interviewsApi.start(interview.id);

      navigate(`/interview/${interview.id}`);
    } catch (err) {
      console.error('Failed to create interview session:', err);
      setError(err.message || 'Could not start interview session. Please try again.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container" style={{ padding: '2.5rem 1.5rem', maxWidth: '960px', position: 'relative' }}>
      <div className="bg-glow-orb orb-primary" style={{ top: '5%', right: '15%' }} />

      {/* Header */}
      <div style={{ textAlign: 'center', marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
        <div style={{
          display: 'inline-flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.35rem 0.85rem',
          borderRadius: 'var(--radius-full)',
          background: 'rgba(99, 102, 241, 0.12)',
          border: '1px solid rgba(99, 102, 241, 0.25)',
          marginBottom: '0.75rem',
          color: '#818cf8',
          fontSize: '0.8rem',
          fontWeight: 600
        }}>
          <Sliders size={14} /> AI Interview Configuration
        </div>
        <h1 className="heading-1">Configure Your Practice Session</h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginTop: '0.35rem' }}>
          Choose your interview type, customize your role, and practice with role-specific AI intelligence
        </p>
      </div>

      {error && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.9rem 1.25rem',
          borderRadius: 'var(--radius-md)',
          background: 'rgba(244, 63, 94, 0.15)',
          border: '1px solid rgba(244, 63, 94, 0.3)',
          color: '#fb7185',
          fontSize: '0.9rem',
          marginBottom: '2rem'
        }}>
          <AlertCircle size={20} style={{ flexShrink: 0 }} />
          <span>{error}</span>
        </div>
      )}

      <form onSubmit={handleSubmit} style={{ position: 'relative', zIndex: 1 }}>
        {/* Step 1: Interview Type Selection (NEW) */}
        <div className="glass-panel" style={{ padding: '2rem', marginBottom: '1.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem', marginBottom: '1.25rem' }}>
            <div style={{
              width: '32px',
              height: '32px',
              borderRadius: '8px',
              background: 'rgba(99, 102, 241, 0.2)',
              color: '#818cf8',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}>
              <Compass size={18} />
            </div>
            <div>
              <h3 className="heading-3">1. Select Interview Type <span style={{ color: '#f43f5e' }}>*</span></h3>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                Target the exact competency round you want to practice.
              </p>
            </div>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(260px, 1fr))', gap: '1rem' }}>
            {[
              {
                id: 'hr',
                label: 'HR Interview',
                badge: 'Behavioral & Culture',
                icon: Users,
                desc: '100% HR and behavioral questions (STAR method, teamwork, conflict resolution, deadlines).'
              },
              {
                id: 'technical',
                label: 'Technical Interview',
                badge: 'Deep Tech & Coding',
                icon: Code2,
                desc: '100% technical questions related directly to your selected role, architecture, and coding.'
              },
              {
                id: 'combined',
                label: 'Combined Interview',
                badge: 'Balanced 30% HR + 70% Tech',
                icon: Sparkles,
                desc: 'Full interview simulation with ~30% behavioral questions and ~70% technical questions.'
              }
            ].map((type) => {
              const Icon = type.icon;
              const isSelected = interviewType === type.id;
              return (
                <div
                  key={type.id}
                  onClick={() => setInterviewType(type.id)}
                  style={{
                    padding: '1.25rem',
                    borderRadius: 'var(--radius-md)',
                    background: isSelected ? 'rgba(99, 102, 241, 0.15)' : 'rgba(13, 21, 39, 0.5)',
                    border: `1.5px solid ${isSelected ? '#6366f1' : 'var(--border-subtle)'}`,
                    cursor: 'pointer',
                    transition: 'all var(--transition-fast)',
                    position: 'relative',
                    display: 'flex',
                    flexDirection: 'column',
                    justifyContent: 'space-between'
                  }}
                >
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
                      <div style={{
                        width: '36px',
                        height: '36px',
                        borderRadius: '8px',
                        background: isSelected ? 'rgba(99, 102, 241, 0.3)' : 'rgba(255, 255, 255, 0.05)',
                        color: isSelected ? '#a5b4fc' : 'var(--text-muted)',
                        display: 'flex',
                        alignItems: 'center',
                        justifyContent: 'center'
                      }}>
                        <Icon size={20} />
                      </div>
                      <span style={{
                        fontSize: '0.7rem',
                        fontWeight: 600,
                        padding: '0.2rem 0.5rem',
                        borderRadius: 'var(--radius-full)',
                        background: isSelected ? 'rgba(99, 102, 241, 0.25)' : 'rgba(255, 255, 255, 0.05)',
                        color: isSelected ? '#c7d2fe' : 'var(--text-muted)'
                      }}>
                        {type.badge}
                      </span>
                    </div>
                    <div style={{ fontWeight: 700, fontSize: '1rem', color: 'var(--text-primary)', marginBottom: '0.35rem' }}>
                      {type.label}
                    </div>
                    <div style={{ fontSize: '0.8rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
                      {type.desc}
                    </div>
                  </div>

                  <div style={{ marginTop: '1rem', display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    <div style={{
                      width: '18px',
                      height: '18px',
                      borderRadius: '50%',
                      border: `2px solid ${isSelected ? '#6366f1' : 'var(--border-subtle)'}`,
                      display: 'flex',
                      alignItems: 'center',
                      justifyContent: 'center',
                      background: isSelected ? '#6366f1' : 'transparent'
                    }}>
                      {isSelected && <div style={{ width: '6px', height: '6px', borderRadius: '50%', background: '#fff' }} />}
                    </div>
                    <span style={{ fontSize: '0.75rem', fontWeight: 600, color: isSelected ? '#a5b4fc' : 'var(--text-muted)' }}>
                      {isSelected ? 'Selected' : 'Click to select'}
                    </span>
                  </div>
                </div>
              );
            })}
          </div>
        </div>

        {/* Step 2: Target Job Role (Required) */}
        <div className="glass-panel" style={{ padding: '2rem', marginBottom: '1.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem', marginBottom: '1rem' }}>
            <div style={{
              width: '32px',
              height: '32px',
              borderRadius: '8px',
              background: 'rgba(99, 102, 241, 0.2)',
              color: '#818cf8',
              display: 'flex',
              alignItems: 'center',
              justifyContent: 'center'
            }}>
              <Briefcase size={18} />
            </div>
            <div>
              <h3 className="heading-3">2. Target Job Role <span style={{ color: '#f43f5e' }}>*</span></h3>
              <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                Choose a predefined role or type any custom role title.
              </p>
            </div>
          </div>

          <div className="input-group" style={{ marginBottom: '1.25rem' }}>
            <input
              id="custom-job-role-input"
              type="text"
              className="input-field"
              placeholder="e.g. Software Engineer, Python Developer, Frontend Developer, Data Analyst..."
              value={customRole}
              onChange={(e) => setCustomRole(e.target.value)}
              style={{ fontSize: '1.05rem', padding: '1rem 1.25rem' }}
              required
            />
          </div>

          {/* Role Suggestion Chips */}
          <div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em', fontWeight: 600 }}>
              Predefined & Suggestion Roles (or type your own above):
            </span>
            <div style={{ display: 'flex', flexWrap: 'wrap', gap: '0.5rem', marginTop: '0.6rem' }}>
              {SUGGESTED_ROLES.map((role) => (
                <button
                  key={role}
                  type="button"
                  onClick={() => setCustomRole(role === 'Other / Custom Role' ? '' : role)}
                  className="chip"
                  style={{
                    background: customRole.toLowerCase() === role.toLowerCase() ? 'rgba(99, 102, 241, 0.25)' : 'rgba(255, 255, 255, 0.04)',
                    borderColor: customRole.toLowerCase() === role.toLowerCase() ? '#6366f1' : 'var(--border-subtle)',
                    color: customRole.toLowerCase() === role.toLowerCase() ? '#ffffff' : 'var(--text-secondary)',
                    fontWeight: customRole.toLowerCase() === role.toLowerCase() ? 700 : 500
                  }}
                >
                  {role === 'Software Engineer' && <span style={{ marginRight: '0.35rem', color: '#38bdf8' }}>★</span>}
                  {role}
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Dedicated Software Engineer Technology Selector */}
        {showTechSelector && (
          <div className="glass-panel" style={{
            padding: '2rem',
            marginBottom: '1.75rem',
            border: '1.5px solid rgba(56, 189, 248, 0.35)',
            background: 'linear-gradient(135deg, rgba(14, 165, 233, 0.08) 0%, rgba(99, 102, 241, 0.06) 100%)'
          }}>
            <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', flexWrap: 'wrap', gap: '1rem', marginBottom: '1.25rem' }}>
              <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
                <div style={{
                  width: '32px',
                  height: '32px',
                  borderRadius: '8px',
                  background: 'rgba(56, 189, 248, 0.2)',
                  color: '#38bdf8',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'center'
                }}>
                  <Code2 size={18} />
                </div>
                <div>
                  <h3 className="heading-3" style={{ color: '#38bdf8' }}>
                    Software Engineer Technology Coverage (125+ Verified Questions)
                  </h3>
                  <p style={{ fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    Choose All 5 technologies for a full-stack interview, or select a focused subset.
                  </p>
                </div>
              </div>

              <div style={{ display: 'flex', gap: '0.5rem' }}>
                <button
                  type="button"
                  onClick={handleSelectAllTech}
                  className="btn btn-secondary btn-sm"
                  style={{
                    fontSize: '0.75rem',
                    background: selectedTechnologies.length === 5 ? 'rgba(56, 189, 248, 0.25)' : 'rgba(255, 255, 255, 0.05)',
                    borderColor: selectedTechnologies.length === 5 ? '#38bdf8' : 'var(--border-subtle)',
                    color: selectedTechnologies.length === 5 ? '#38bdf8' : 'var(--text-secondary)'
                  }}
                >
                  All 5 Technologies
                </button>
              </div>
            </div>

            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(170px, 1fr))', gap: '0.75rem' }}>
              {SE_TECHNOLOGIES.map((tech) => {
                const isChecked = selectedTechnologies.includes(tech.id);
                return (
                  <label
                    key={tech.id}
                    style={{
                      display: 'flex',
                      flexDirection: 'column',
                      padding: '0.9rem',
                      borderRadius: 'var(--radius-md)',
                      background: isChecked ? 'rgba(56, 189, 248, 0.15)' : 'rgba(13, 21, 39, 0.4)',
                      border: `1px solid ${isChecked ? '#38bdf8' : 'var(--border-subtle)'}`,
                      cursor: 'pointer',
                      transition: 'all var(--transition-fast)'
                    }}
                  >
                    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.4rem' }}>
                      <span style={{ fontWeight: 700, fontSize: '0.95rem', color: isChecked ? '#ffffff' : 'var(--text-secondary)' }}>
                        {tech.label}
                      </span>
                      <input
                        type="checkbox"
                        checked={isChecked}
                        onChange={() => handleTechToggle(tech.id)}
                        style={{ accentColor: '#38bdf8', width: '16px', height: '16px' }}
                      />
                    </div>
                    <span style={{ fontSize: '0.725rem', color: 'var(--text-muted)' }}>
                      {tech.desc}
                    </span>
                    <button
                      type="button"
                      onClick={(e) => {
                        e.preventDefault();
                        handleSelectSingleTech(tech.id);
                      }}
                      style={{
                        marginTop: '0.6rem',
                        fontSize: '0.675rem',
                        background: 'none',
                        border: 'none',
                        color: '#38bdf8',
                        cursor: 'pointer',
                        padding: 0,
                        textAlign: 'left',
                        textDecoration: 'underline'
                      }}
                    >
                      {tech.label} only
                    </button>
                  </label>
                );
              })}
            </div>
          </div>
        )}

        {/* Step 3: Experience & Difficulty */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.75rem', marginBottom: '1.75rem' }}>
          {/* Experience Level */}
          <div className="glass-panel" style={{ padding: '1.75rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1rem' }}>
              <Layers size={18} color="#818cf8" />
              <h3 className="heading-3">Experience Level</h3>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
              {[
                { id: 'fresher', label: 'Fresher', desc: 'Recent graduate / entry transitions' },
                { id: 'entry', label: 'Entry-level', desc: '1–2 years professional experience' },
                { id: 'experienced', label: 'Experienced', desc: '3+ years / senior career track' },
              ].map((opt) => (
                <label
                  key={opt.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '0.85rem 1rem',
                    borderRadius: 'var(--radius-md)',
                    background: experienceLevel === opt.id ? 'rgba(99, 102, 241, 0.15)' : 'rgba(13, 21, 39, 0.5)',
                    border: `1px solid ${experienceLevel === opt.id ? '#6366f1' : 'var(--border-subtle)'}`,
                    cursor: 'pointer',
                    transition: 'all var(--transition-fast)'
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 600, fontSize: '0.925rem', color: 'var(--text-primary)' }}>
                      {opt.label}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                      {opt.desc}
                    </div>
                  </div>
                  <input
                    type="radio"
                    name="experienceLevel"
                    value={opt.id}
                    checked={experienceLevel === opt.id}
                    onChange={() => setExperienceLevel(opt.id)}
                    style={{ accentColor: '#6366f1', width: '18px', height: '18px' }}
                  />
                </label>
              ))}
            </div>
          </div>

          {/* Difficulty */}
          <div className="glass-panel" style={{ padding: '1.75rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1rem' }}>
              <Gauge size={18} color="#818cf8" />
              <h3 className="heading-3">Difficulty</h3>
            </div>

            <div style={{ display: 'flex', flexDirection: 'column', gap: '0.65rem' }}>
              {[
                { id: 'easy', label: 'Easy', desc: 'Core fundamentals and standard concepts' },
                { id: 'medium', label: 'Medium', desc: 'Real-world problem solving & scenarios' },
                { id: 'hard', label: 'Hard', desc: 'Architecture, edge cases, deep internals' },
              ].map((opt) => (
                <label
                  key={opt.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '0.85rem 1rem',
                    borderRadius: 'var(--radius-md)',
                    background: difficulty === opt.id ? 'rgba(99, 102, 241, 0.15)' : 'rgba(13, 21, 39, 0.5)',
                    border: `1px solid ${difficulty === opt.id ? '#6366f1' : 'var(--border-subtle)'}`,
                    cursor: 'pointer',
                    transition: 'all var(--transition-fast)'
                  }}
                >
                  <div>
                    <div style={{ fontWeight: 600, fontSize: '0.925rem', color: 'var(--text-primary)' }}>
                      {opt.label}
                    </div>
                    <div style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                      {opt.desc}
                    </div>
                  </div>
                  <input
                    type="radio"
                    name="difficulty"
                    value={opt.id}
                    checked={difficulty === opt.id}
                    onChange={() => setDifficulty(opt.id)}
                    style={{ accentColor: '#6366f1', width: '18px', height: '18px' }}
                  />
                </label>
              ))}
            </div>
          </div>
        </div>

        {/* Step 4: Mode & Question Count */}
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '1.75rem', marginBottom: '1.75rem' }}>
          {/* Mode */}
          <div className="glass-panel" style={{ padding: '1.75rem' }}>
            <h3 className="heading-3" style={{ marginBottom: '1rem' }}>Interview Mode</h3>
            <div style={{ display: 'grid', gridTemplateColumns: '1fr 1fr', gap: '0.75rem' }}>
              <label
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '1.25rem 0.75rem',
                  borderRadius: 'var(--radius-md)',
                  background: interviewMode === 'voice' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(13, 21, 39, 0.5)',
                  border: `1px solid ${interviewMode === 'voice' ? '#6366f1' : 'var(--border-subtle)'}`,
                  cursor: 'pointer',
                  textAlign: 'center',
                  gap: '0.5rem'
                }}
              >
                <Mic size={24} color={interviewMode === 'voice' ? '#818cf8' : 'var(--text-muted)'} />
                <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Voice Mode</span>
                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Speak & Listen</span>
                <input
                  type="radio"
                  name="interviewMode"
                  value="voice"
                  checked={interviewMode === 'voice'}
                  onChange={() => setInterviewMode('voice')}
                  style={{ display: 'none' }}
                />
              </label>

              <label
                style={{
                  display: 'flex',
                  flexDirection: 'column',
                  alignItems: 'center',
                  justifyContent: 'center',
                  padding: '1.25rem 0.75rem',
                  borderRadius: 'var(--radius-md)',
                  background: interviewMode === 'text' ? 'rgba(99, 102, 241, 0.15)' : 'rgba(13, 21, 39, 0.5)',
                  border: `1px solid ${interviewMode === 'text' ? '#6366f1' : 'var(--border-subtle)'}`,
                  cursor: 'pointer',
                  textAlign: 'center',
                  gap: '0.5rem'
                }}
              >
                <MessageSquare size={24} color={interviewMode === 'text' ? '#818cf8' : 'var(--text-muted)'} />
                <span style={{ fontWeight: 600, fontSize: '0.9rem' }}>Text Mode</span>
                <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Type responses & code</span>
                <input
                  type="radio"
                  name="interviewMode"
                  value="text"
                  checked={interviewMode === 'text'}
                  onChange={() => setInterviewMode('text')}
                  style={{ display: 'none' }}
                />
              </label>
            </div>
          </div>

          {/* Question Count */}
          <div className="glass-panel" style={{ padding: '1.75rem' }}>
            <h3 className="heading-3" style={{ marginBottom: '1rem' }}>Number of Questions</h3>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(3, 1fr)', gap: '0.75rem' }}>
              {[5, 10, 15].map((count) => (
                <button
                  key={count}
                  type="button"
                  onClick={() => setQuestionCount(count)}
                  style={{
                    padding: '1.25rem 0.5rem',
                    borderRadius: 'var(--radius-md)',
                    background: questionCount === count ? 'rgba(99, 102, 241, 0.2)' : 'rgba(13, 21, 39, 0.5)',
                    border: `1px solid ${questionCount === count ? '#6366f1' : 'var(--border-subtle)'}`,
                    color: questionCount === count ? '#ffffff' : 'var(--text-secondary)',
                    fontWeight: 700,
                    cursor: 'pointer',
                    display: 'flex',
                    flexDirection: 'column',
                    alignItems: 'center',
                    gap: '0.25rem',
                    transition: 'all var(--transition-fast)'
                  }}
                >
                  <span style={{ fontSize: '1.5rem', lineHeight: 1 }}>{count}</span>
                  <span style={{ fontSize: '0.7rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>Questions</span>
                </button>
              ))}
            </div>
          </div>
        </div>

        {/* Step 5: Optional Context */}
        <div className="glass-panel" style={{ padding: '1.75rem', marginBottom: '2rem' }}>
          <button
            type="button"
            onClick={() => setShowOptional(!showOptional)}
            style={{
              background: 'none',
              border: 'none',
              color: '#818cf8',
              fontSize: '0.95rem',
              fontWeight: 600,
              cursor: 'pointer',
              display: 'flex',
              alignItems: 'center',
              gap: '0.5rem'
            }}
          >
            <Sparkles size={16} />
            {showOptional ? 'Hide Optional Context' : 'Add Optional Job Description or Resume Context (Recommended)'}
          </button>

          {showOptional && (
            <div style={{ marginTop: '1.5rem', display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
              <div className="input-group" style={{ marginBottom: 0 }}>
                <label className="input-label" htmlFor="interview-focus">
                  Interview Focus (Optional)
                </label>
                <input
                  id="interview-focus"
                  type="text"
                  className="input-field"
                  placeholder="e.g. Distributed Systems, React Hooks, Database Tuning, REST APIs..."
                  value={interviewFocus}
                  onChange={(e) => setInterviewFocus(e.target.value)}
                />
              </div>

              <div className="input-group" style={{ marginBottom: 0 }}>
                <label className="input-label" htmlFor="job-description">
                  Job Description Text (Optional)
                </label>
                <textarea
                  id="job-description"
                  className="input-field"
                  placeholder="Paste relevant job description requirements to tailor technical or behavioral questions..."
                  value={jobDescription}
                  onChange={(e) => setJobDescription(e.target.value)}
                  rows={3}
                />
              </div>

              <div className="input-group" style={{ marginBottom: 0 }}>
                <label className="input-label" htmlFor="resume-text">
                  Your Resume / Skills Summary (Optional)
                </label>
                <textarea
                  id="resume-text"
                  className="input-field"
                  placeholder="Paste your past experience or skill highlights to tailor the depth of the questions..."
                  value={resumeText}
                  onChange={(e) => setResumeText(e.target.value)}
                  rows={3}
                />
              </div>
            </div>
          )}
        </div>

        {/* Submit Action */}
        <button
          type="submit"
          className="btn btn-primary"
          disabled={isLoading}
          style={{
            width: '100%',
            padding: '1.1rem',
            fontSize: '1.05rem',
            fontWeight: 700,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '0.75rem',
            boxShadow: '0 8px 24px -4px rgba(99, 102, 241, 0.45)'
          }}
        >
          {isLoading ? (
            'Preparing Your Interview Session...'
          ) : (
            <>
              Launch {interviewType === 'hr' ? 'HR' : (interviewType === 'technical' ? 'Technical' : 'Combined')} Interview
              <ArrowRight size={20} />
            </>
          )}
        </button>
      </form>
    </div>
  );
};
export default InterviewSetupPage;
