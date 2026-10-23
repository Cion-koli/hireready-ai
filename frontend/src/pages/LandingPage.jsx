import React from 'react';
import { Link } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import {
  Sparkles,
  ArrowRight,
  Mic,
  MessageSquareText,
  BarChart3,
  CheckCircle2,
  Briefcase,
  ShieldCheck,
  Award,
  Zap
} from 'lucide-react';

export const LandingPage = () => {
  const { isAuthenticated } = useAuth();

  const SAMPLE_ROLES = [
    'Python Developer',
    'Frontend Developer',
    'Data Analyst',
    'Full-Stack Developer',
    'HR Executive',
    'Digital Marketing Executive',
    'Software Engineer',
    'Product Manager',
    'Customer Support Lead'
  ];

  return (
    <div style={{ position: 'relative', overflow: 'hidden' }}>
      {/* Background Glow Orbs */}
      <div className="bg-glow-orb orb-primary" />
      <div className="bg-glow-orb orb-purple" />

      {/* Hero Section */}
      <section style={{ padding: '4.5rem 0 3.5rem 0', position: 'relative', zIndex: 1 }}>
        <div className="container" style={{ textAlign: 'center', maxWidth: '880px' }}>
          {/* Badge */}
          <div style={{
            display: 'inline-flex',
            alignItems: 'center',
            gap: '0.5rem',
            padding: '0.4rem 1rem',
            borderRadius: 'var(--radius-full)',
            background: 'rgba(99, 102, 241, 0.12)',
            border: '1px solid rgba(99, 102, 241, 0.25)',
            marginBottom: '1.75rem'
          }}>
            <Sparkles size={16} color="#818cf8" />
            <span style={{ fontSize: '0.85rem', fontWeight: 600, color: '#a5b4fc', letterSpacing: '0.02em' }}>
              Specialized for HR & Behavioral Rounds Only
            </span>
          </div>

          <h1 className="heading-hero" style={{ marginBottom: '1.5rem' }}>
            Ace Your HR Interview For <span className="text-gradient-purple">Any Role</span> You Want
          </h1>

          <p style={{
            fontSize: '1.15rem',
            color: 'var(--text-secondary)',
            lineHeight: 1.6,
            marginBottom: '2.5rem',
            maxWidth: '720px',
            margin: '0 auto 2.5rem auto'
          }}>
            Type your dream job title and practice personalized HR-round questions in real-time.
            Master behavioral challenges, teamwork scenarios, and STAR methodology—with zero coding stress.
          </p>

          <div style={{
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            gap: '1rem',
            flexWrap: 'wrap'
          }}>
            <Link
              to={isAuthenticated ? "/interview/setup" : "/register"}
              className="btn btn-primary btn-lg"
              id="hero-start-btn"
            >
              Start Practising Free <ArrowRight size={18} />
            </Link>
            {!isAuthenticated && (
              <Link to="/login" className="btn btn-secondary btn-lg" id="hero-signin-btn">
                Sign In
              </Link>
            )}
          </div>

          {/* Any Role Interactive Showcase */}
          <div style={{ marginTop: '3.5rem' }}>
            <span style={{ fontSize: '0.825rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.08em', fontWeight: 600 }}>
              Practice for custom roles like:
            </span>
            <div style={{
              display: 'flex',
              flexWrap: 'wrap',
              justifyContent: 'center',
              gap: '0.65rem',
              marginTop: '1rem'
            }}>
              {SAMPLE_ROLES.map((role) => (
                <Link
                  key={role}
                  to={isAuthenticated ? `/interview/setup?role=${encodeURIComponent(role)}` : `/register?role=${encodeURIComponent(role)}`}
                  className="chip"
                  style={{ textDecoration: 'none' }}
                >
                  <Briefcase size={13} style={{ marginRight: '6px', color: '#818cf8' }} />
                  {role}
                </Link>
              ))}
              <span className="chip" style={{ background: 'rgba(99, 102, 241, 0.15)', borderColor: '#6366f1' }}>
                + Any Custom Role You Type!
              </span>
            </div>
          </div>
        </div>
      </section>

      {/* Strict HR Scope Explanation Banner */}
      <section style={{ padding: '2.5rem 0', position: 'relative', zIndex: 1 }}>
        <div className="container">
          <div className="glass-panel" style={{
            padding: '2rem',
            border: '1px solid rgba(99, 102, 241, 0.3)',
            background: 'linear-gradient(135deg, rgba(17, 28, 53, 0.9) 0%, rgba(13, 21, 39, 0.9) 100%)'
          }}>
            <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(280px, 1fr))', gap: '2rem', alignItems: 'center' }}>
              <div>
                <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#818cf8', marginBottom: '0.5rem' }}>
                  <ShieldCheck size={20} />
                  <span style={{ fontWeight: 700, fontSize: '0.9rem', textTransform: 'uppercase', letterSpacing: '0.05em' }}>
                    100% HR & Behavioral Focus
                  </span>
                </div>
                <h3 className="heading-2" style={{ marginBottom: '0.75rem' }}>
                  No coding exams. No syntax quizzes.
                </h3>
                <p style={{ color: 'var(--text-secondary)', fontSize: '0.925rem', lineHeight: 1.6 }}>
                  Technical candidates often fail HR rounds because of behavioral communication, conflict handling, or answering under pressure. HireReady AI focuses exclusively on your workplace presence, teamwork, handling feedback, and motivation.
                </p>
              </div>

              <div style={{ display: 'flex', flexDirection: 'column', gap: '0.75rem' }}>
                <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
                  <CheckCircle2 size={18} color="#10b981" style={{ flexShrink: 0, marginTop: '2px' }} />
                  <span style={{ fontSize: '0.875rem', color: 'var(--text-primary)' }}>
                    <strong>Python Developer:</strong> Project collaboration, sprint deadlines, and receiving manager feedback.
                  </span>
                </div>
                <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
                  <CheckCircle2 size={18} color="#10b981" style={{ flexShrink: 0, marginTop: '2px' }} />
                  <span style={{ fontSize: '0.875rem', color: 'var(--text-primary)' }}>
                    <strong>Data Analyst:</strong> Presenting insights to non-technical leaders and resolving stakeholder disputes.
                  </span>
                </div>
                <div style={{ display: 'flex', alignItems: 'flex-start', gap: '0.75rem' }}>
                  <CheckCircle2 size={18} color="#10b981" style={{ flexShrink: 0, marginTop: '2px' }} />
                  <span style={{ fontSize: '0.875rem', color: 'var(--text-primary)' }}>
                    <strong>Any Custom Role:</strong> Workplace scenarios, leadership initiative, and career aspirations.
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </section>

      {/* Feature Cards Grid */}
      <section style={{ padding: '3.5rem 0', position: 'relative', zIndex: 1 }}>
        <div className="container">
          <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
            <h2 className="heading-1" style={{ marginBottom: '0.75rem' }}>
              Engineered For Modern Interview Readiness
            </h2>
            <p style={{ color: 'var(--text-secondary)', maxWidth: '580px', margin: '0 auto' }}>
              Simulate actual conversational HR interviews with intelligent follow-up questions and multi-criterion feedback.
            </p>
          </div>

          <div className="grid-3">
            <div className="glass-panel" style={{ padding: '2rem' }}>
              <div style={{
                width: '46px',
                height: '46px',
                borderRadius: '12px',
                background: 'rgba(99, 102, 241, 0.15)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#818cf8',
                marginBottom: '1.25rem'
              }}>
                <Briefcase size={22} />
              </div>
              <h3 className="heading-3" style={{ marginBottom: '0.5rem' }}>
                Any Custom Role
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6 }}>
                Not confined to rigid dropdowns. Type your exact target job title—from entry-level to senior management—and receive tailored questions.
              </p>
            </div>

            <div className="glass-panel" style={{ padding: '2rem' }}>
              <div style={{
                width: '46px',
                height: '46px',
                borderRadius: '12px',
                background: 'rgba(139, 92, 246, 0.15)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#a78bfa',
                marginBottom: '1.25rem'
              }}>
                <Mic size={22} />
              </div>
              <h3 className="heading-3" style={{ marginBottom: '0.5rem' }}>
                Voice & Text Interaction
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6 }}>
                Speak your responses using browser speech recognition while hearing AI questions spoken aloud. Full text fallback is always accessible.
              </p>
            </div>

            <div className="glass-panel" style={{ padding: '2rem' }}>
              <div style={{
                width: '46px',
                height: '46px',
                borderRadius: '12px',
                background: 'rgba(6, 182, 212, 0.15)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                color: '#22d3ee',
                marginBottom: '1.25rem'
              }}>
                <BarChart3 size={22} />
              </div>
              <h3 className="heading-3" style={{ marginBottom: '0.5rem' }}>
                Weighted HR Scoring
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6 }}>
                Evaluated against 4 professional criteria: Relevance (30%), Structure (25%), STAR Details (25%), and Communication (20%).
              </p>
            </div>
          </div>
        </div>
      </section>

      {/* How It Works Section */}
      <section style={{ padding: '3.5rem 0 5rem 0', position: 'relative', zIndex: 1 }}>
        <div className="container">
          <div style={{ textAlign: 'center', marginBottom: '3rem' }}>
            <span style={{ fontSize: '0.8rem', fontWeight: 700, color: '#818cf8', textTransform: 'uppercase', letterSpacing: '0.08em' }}>
              Simple 3-Step Process
            </span>
            <h2 className="heading-1" style={{ marginTop: '0.5rem' }}>
              How HireReady AI Works
            </h2>
          </div>

          <div className="grid-3">
            <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{
                width: '40px',
                height: '40px',
                borderRadius: '50%',
                background: 'var(--accent-primary)',
                color: '#ffffff',
                fontWeight: 800,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1.25rem auto'
              }}>
                1
              </div>
              <h3 className="heading-3" style={{ marginBottom: '0.5rem' }}>
                Set Your Target Role
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6 }}>
                Type your role, select your experience level (Fresher, Entry, Experienced), and choose voice or text mode.
              </p>
            </div>

            <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{
                width: '40px',
                height: '40px',
                borderRadius: '50%',
                background: 'var(--accent-secondary)',
                color: '#ffffff',
                fontWeight: 800,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1.25rem auto'
              }}>
                2
              </div>
              <h3 className="heading-3" style={{ marginBottom: '0.5rem' }}>
                Take The Live Interview
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6 }}>
                Answer dynamic HR questions one by one. The AI listens and generates contextual follow-ups from your previous answers.
              </p>
            </div>

            <div className="glass-panel" style={{ padding: '2rem', textAlign: 'center' }}>
              <div style={{
                width: '40px',
                height: '40px',
                borderRadius: '50%',
                background: 'var(--accent-emerald)',
                color: '#ffffff',
                fontWeight: 800,
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1.25rem auto'
              }}>
                3
              </div>
              <h3 className="heading-3" style={{ marginBottom: '0.5rem' }}>
                Review Detailed Report
              </h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.6 }}>
                Get an instant breakdown with criteria scores, strengths, improvement areas, and model STAR answers you can review or print.
              </p>
            </div>
          </div>

          {/* Bottom CTA */}
          <div style={{ marginTop: '4rem', textAlign: 'center' }}>
            <Link
              to={isAuthenticated ? "/interview/setup" : "/register"}
              className="btn btn-primary btn-lg"
              id="cta-start-practice"
            >
              Start Your First HR Interview Now <ArrowRight size={18} />
            </Link>
          </div>
        </div>
      </section>
    </div>
  );
};
