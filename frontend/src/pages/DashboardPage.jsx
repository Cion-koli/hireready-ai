import React, { useState, useEffect } from 'react';
import { Link, useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { reportsApi } from '../api/reports';
import { ScoreGauge } from '../components/ScoreGauge';
import {
  Sparkles,
  PlusCircle,
  Briefcase,
  TrendingUp,
  Award,
  History,
  ArrowRight,
  Clock,
  PlayCircle,
  FileText
} from 'lucide-react';

export const DashboardPage = () => {
  const { user } = useAuth();
  const navigate = useNavigate();

  const [stats, setStats] = useState({
    total_interviews: 0,
    completed_interviews: 0,
    average_score: 0,
    recent_sessions: [],
    score_trend: [],
  });
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    fetchStats();
  }, []);

  const fetchStats = async () => {
    setIsLoading(true);
    try {
      const data = await reportsApi.getDashboardStats();
      setStats(data);
    } catch (err) {
      console.error('Failed to load dashboard stats:', err);
      setError('Unable to load latest interview statistics.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="container" style={{ padding: '2.5rem 1.5rem', position: 'relative' }}>
      <div className="bg-glow-orb orb-primary" style={{ top: 0, left: '20%' }} />

      {/* Header Banner */}
      <div style={{
        display: 'flex',
        flexWrap: 'wrap',
        alignItems: 'center',
        justifyContent: 'space-between',
        gap: '1.5rem',
        marginBottom: '2.5rem',
        position: 'relative',
        zIndex: 1
      }}>
        <div>
          <span style={{ fontSize: '0.85rem', color: '#818cf8', fontWeight: 600, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Candidate Overview
          </span>
          <h1 className="heading-1" style={{ marginTop: '0.25rem' }}>
            Welcome back, {user?.first_name || user?.username}!
          </h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.95rem', marginTop: '0.35rem' }}>
            Ready to sharpen your HR behavioral responses?
          </p>
        </div>

        <Link
          to="/interview/setup"
          className="btn btn-primary btn-lg"
          id="dashboard-start-new-btn"
        >
          <PlusCircle size={20} /> Start New HR Interview
        </Link>
      </div>

      {/* Analytics Metric Cards */}
      <div className="grid-3" style={{ marginBottom: '2.5rem', position: 'relative', zIndex: 1 }}>
        {/* Metric 1 */}
        <div className="glass-panel" style={{ padding: '1.75rem', display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div style={{
            width: '52px',
            height: '52px',
            borderRadius: '14px',
            background: 'rgba(99, 102, 241, 0.15)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#818cf8'
          }}>
            <Briefcase size={26} />
          </div>
          <div>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em', fontWeight: 600 }}>
              Completed Sessions
            </span>
            <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text-primary)', lineHeight: 1.1, marginTop: '0.2rem' }}>
              {stats.completed_interviews}
            </div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>
              out of {stats.total_interviews} initiated
            </span>
          </div>
        </div>

        {/* Metric 2 */}
        <div className="glass-panel" style={{ padding: '1.75rem', display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div style={{
            width: '52px',
            height: '52px',
            borderRadius: '14px',
            background: 'rgba(16, 185, 129, 0.15)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#10b981'
          }}>
            <Award size={26} />
          </div>
          <div>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em', fontWeight: 600 }}>
              Average Practice Score
            </span>
            <div style={{ fontSize: '2rem', fontWeight: 800, color: 'var(--text-primary)', lineHeight: 1.1, marginTop: '0.2rem' }}>
              {stats.average_score > 0 ? `${stats.average_score}%` : '—'}
            </div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>
              Across completed evaluations
            </span>
          </div>
        </div>

        {/* Metric 3 */}
        <div className="glass-panel" style={{ padding: '1.75rem', display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
          <div style={{
            width: '52px',
            height: '52px',
            borderRadius: '14px',
            background: 'rgba(139, 92, 246, 0.15)',
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: '#a78bfa'
          }}>
            <TrendingUp size={26} />
          </div>
          <div>
            <span style={{ fontSize: '0.8rem', color: 'var(--text-muted)', textTransform: 'uppercase', letterSpacing: '0.05em', fontWeight: 600 }}>
              HR Readiness Status
            </span>
            <div style={{ fontSize: '1.35rem', fontWeight: 700, color: '#818cf8', lineHeight: 1.2, marginTop: '0.3rem' }}>
              {stats.completed_interviews >= 3 ? 'Actively Preparing' : stats.completed_interviews > 0 ? 'Getting Started' : 'Ready for First Role'}
            </div>
            <span style={{ fontSize: '0.75rem', color: 'var(--text-secondary)' }}>
              Behavioral & STAR focus
            </span>
          </div>
        </div>
      </div>

      {/* Main Content Layout: Recent Interviews & Progress Progression */}
      <div style={{ display: 'grid', gridTemplateColumns: '1.6fr 1fr', gap: '2rem', position: 'relative', zIndex: 1 }} className="dashboard-grid">
        {/* Recent Interviews Card */}
        <div className="glass-panel" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
            <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem' }}>
              <Clock size={20} color="#818cf8" />
              <h2 className="heading-2" style={{ fontSize: '1.25rem' }}>Recent Interviews</h2>
            </div>
            <Link to="/history" style={{ color: '#818cf8', fontSize: '0.85rem', textDecoration: 'none', fontWeight: 600 }}>
              View All History &rarr;
            </Link>
          </div>

          {stats.recent_sessions && stats.recent_sessions.length > 0 ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
              {stats.recent_sessions.map((item) => (
                <div
                  key={item.id}
                  style={{
                    display: 'flex',
                    alignItems: 'center',
                    justifyContent: 'space-between',
                    padding: '1.1rem',
                    background: 'rgba(13, 21, 39, 0.6)',
                    borderRadius: 'var(--radius-md)',
                    border: '1px solid var(--border-subtle)',
                    flexWrap: 'wrap',
                    gap: '1rem'
                  }}
                >
                  <div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '0.25rem' }}>
                      <span style={{ fontWeight: 700, fontSize: '1rem', color: 'var(--text-primary)' }}>
                        {item.custom_job_role}
                      </span>
                      {item.is_demo && (
                        <span className="badge badge-demo" style={{ fontSize: '0.65rem' }}>Demo Mode</span>
                      )}
                    </div>
                    <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem', fontSize: '0.75rem', color: 'var(--text-muted)' }}>
                      <span>{new Date(item.created_at).toLocaleDateString()}</span>
                      <span>&bull;</span>
                      <span style={{ textTransform: 'capitalize' }}>{item.experience_level}</span>
                      <span>&bull;</span>
                      <span style={{ textTransform: 'capitalize' }}>{item.interview_mode} mode</span>
                    </div>
                  </div>

                  <div style={{ display: 'flex', alignItems: 'center', gap: '1rem' }}>
                    {item.overall_score !== null && (
                      <div style={{ textAlign: 'right' }}>
                        <div style={{ fontSize: '1.2rem', fontWeight: 700, color: '#10b981' }}>
                          {item.overall_score}%
                        </div>
                        <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Score</span>
                      </div>
                    )}

                    {item.status === 'completed' || item.report_id ? (
                      <Link
                        to={`/reports/${item.report_id || item.id}`}
                        className="btn btn-secondary btn-sm"
                      >
                        <FileText size={15} /> View Report
                      </Link>
                    ) : (
                      <Link
                        to={`/interview/${item.id}`}
                        className="btn btn-primary btn-sm"
                      >
                        <PlayCircle size={15} /> Resume
                      </Link>
                    )}
                  </div>
                </div>
              ))}
            </div>
          ) : (
            <div style={{ textAlign: 'center', padding: '3.5rem 1rem' }}>
              <div style={{
                width: '64px',
                height: '64px',
                borderRadius: '50%',
                background: 'rgba(99, 102, 241, 0.1)',
                display: 'flex',
                alignItems: 'center',
                justifyContent: 'center',
                margin: '0 auto 1rem auto',
                color: '#818cf8'
              }}>
                <Briefcase size={28} />
              </div>
              <h3 style={{ fontSize: '1.1rem', fontWeight: 600, marginBottom: '0.5rem' }}>No HR interviews yet</h3>
              <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', maxWidth: '360px', margin: '0 auto 1.5rem auto' }}>
                Type your desired job role and begin your first mock session.
              </p>
              <Link to="/interview/setup" className="btn btn-primary btn-sm">
                Start First HR Interview
              </Link>
            </div>
          )}
        </div>

        {/* Progress & Trends Card */}
        <div className="glass-panel" style={{ padding: '2rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.5rem' }}>
            <TrendingUp size={20} color="#818cf8" />
            <h2 className="heading-2" style={{ fontSize: '1.25rem' }}>Performance Trend</h2>
          </div>

          {stats.score_trend && stats.score_trend.length > 0 ? (
            <div style={{ display: 'flex', flexDirection: 'column', gap: '1.25rem' }}>
              <p style={{ fontSize: '0.85rem', color: 'var(--text-secondary)' }}>
                Track your scores across consecutive HR sessions:
              </p>
              {stats.score_trend.map((trend, idx) => (
                <div key={idx} style={{ display: 'flex', flexDirection: 'column', gap: '0.35rem' }}>
                  <div style={{ display: 'flex', justifyContent: 'space-between', fontSize: '0.825rem' }}>
                    <span style={{ fontWeight: 600, color: 'var(--text-primary)' }}>{trend.role}</span>
                    <span style={{ color: '#818cf8', fontWeight: 700 }}>{trend.score}%</span>
                  </div>
                  <div style={{ height: '6px', background: 'rgba(255, 255, 255, 0.08)', borderRadius: '3px', overflow: 'hidden' }}>
                    <div style={{
                      height: '100%',
                      width: `${Math.min(100, trend.score)}%`,
                      background: trend.score >= 80 ? '#10b981' : trend.score >= 60 ? '#6366f1' : '#f59e0b',
                      borderRadius: '3px'
                    }} />
                  </div>
                  <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>{trend.date}</span>
                </div>
              ))}
            </div>
          ) : (
            <div style={{ textAlign: 'center', padding: '2.5rem 1rem' }}>
              <ScoreGauge score={stats.average_score} size={150} />
              <p style={{ fontSize: '0.825rem', color: 'var(--text-muted)', marginTop: '1rem' }}>
                Complete at least 1 interview session to generate personalized trend analytics.
              </p>
            </div>
          )}
        </div>
      </div>

      <style>{`
        @media (max-width: 900px) {
          .dashboard-grid { grid-template-columns: 1fr !important; }
        }
      `}</style>
    </div>
  );
};
