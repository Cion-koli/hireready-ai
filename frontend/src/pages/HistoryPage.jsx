import React, { useState, useEffect } from 'react';
import { Link } from 'react-router-dom';
import { interviewsApi } from '../api/interviews';
import { ConfirmModal } from '../components/ConfirmModal';
import {
  History,
  Search,
  Filter,
  FileText,
  PlayCircle,
  Trash2,
  Calendar,
  Layers,
  Award,
  AlertCircle,
  CheckCircle,
  PlusCircle
} from 'lucide-react';

export const HistoryPage = () => {
  const [interviews, setInterviews] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [roleFilter, setRoleFilter] = useState('');
  const [statusFilter, setStatusFilter] = useState('');

  // Delete modal state
  const [selectedToDelete, setSelectedToDelete] = useState(null);
  const [isDeleting, setIsDeleting] = useState(false);

  useEffect(() => {
    fetchInterviews();
  }, [roleFilter, statusFilter]);

  const fetchInterviews = async () => {
    setIsLoading(true);
    try {
      const params = {};
      if (roleFilter.trim()) params.role = roleFilter.trim();
      if (statusFilter) params.status = statusFilter;

      const data = await interviewsApi.list(params);
      setInterviews(data);
    } catch (err) {
      console.error('Failed to load interview history:', err);
    } finally {
      setIsLoading(false);
    }
  };

  const handleDeleteConfirm = async () => {
    if (!selectedToDelete) return;
    setIsDeleting(true);
    try {
      await interviewsApi.delete(selectedToDelete.id);
      setInterviews((prev) => prev.filter((i) => i.id !== selectedToDelete.id));
      setSelectedToDelete(null);
    } catch (err) {
      console.error('Failed to delete interview:', err);
    } finally {
      setIsDeleting(false);
    }
  };

  return (
    <div className="container" style={{ padding: '2.5rem 1.5rem', maxWidth: '1000px', position: 'relative' }}>
      <div className="bg-glow-orb orb-primary" style={{ top: '5%', left: '10%' }} />

      {/* Header */}
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
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#818cf8', marginBottom: '0.25rem' }}>
            <History size={18} />
            <span style={{ fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
              Past Sessions
            </span>
          </div>
          <h1 className="heading-1">Interview History</h1>
          <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginTop: '0.2rem' }}>
            Review past HR practice sessions, open reports, or continue incomplete sessions
          </p>
        </div>

        <Link to="/interview/setup" className="btn btn-primary btn-sm">
          <PlusCircle size={16} /> New HR Interview
        </Link>
      </div>

      {/* Search and Filters Bar */}
      <div className="glass-panel" style={{ padding: '1.25rem 1.5rem', marginBottom: '1.75rem', position: 'relative', zIndex: 1 }}>
        <div style={{ display: 'flex', flexWrap: 'wrap', gap: '1rem', alignItems: 'center' }}>
          {/* Role Search */}
          <div style={{ flex: '1 1 240px', position: 'relative' }}>
            <Search size={16} style={{ position: 'absolute', left: '12px', top: '50%', transform: 'translateY(-50%)', color: 'var(--text-muted)' }} />
            <input
              type="text"
              className="input-field"
              placeholder="Search by custom role title..."
              value={roleFilter}
              onChange={(e) => setRoleFilter(e.target.value)}
              style={{ paddingLeft: '2.4rem', height: '42px', fontSize: '0.875rem' }}
            />
          </div>

          {/* Status Dropdown */}
          <div style={{ width: '180px' }}>
            <select
              className="input-field"
              value={statusFilter}
              onChange={(e) => setStatusFilter(e.target.value)}
              style={{ height: '42px', fontSize: '0.875rem' }}
            >
              <option value="">All Statuses</option>
              <option value="completed">Completed</option>
              <option value="in_progress">In Progress</option>
              <option value="ended_early">Ended Early</option>
              <option value="setup">Setup</option>
            </select>
          </div>
        </div>
      </div>

      {/* Interviews List */}
      <div style={{ position: 'relative', zIndex: 1 }}>
        {isLoading ? (
          <div style={{ textAlign: 'center', padding: '4rem 1rem', color: 'var(--text-secondary)' }}>
            <p>Loading your interview history...</p>
          </div>
        ) : interviews.length > 0 ? (
          <div style={{ display: 'flex', flexDirection: 'column', gap: '1rem' }}>
            {interviews.map((item) => (
              <div
                key={item.id}
                className="glass-panel"
                style={{
                  padding: '1.5rem 1.75rem',
                  display: 'flex',
                  alignItems: 'center',
                  justifyContent: 'space-between',
                  flexWrap: 'wrap',
                  gap: '1.25rem'
                }}
              >
                <div>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem', marginBottom: '0.35rem' }}>
                    <h3 style={{ fontSize: '1.15rem', fontWeight: 700, color: 'var(--text-primary)' }}>
                      {item.custom_job_role}
                    </h3>
                    <span
                      className="badge"
                      style={{
                        background:
                          item.status === 'completed'
                            ? 'rgba(16, 185, 129, 0.15)'
                            : item.status === 'in_progress'
                            ? 'rgba(99, 102, 241, 0.15)'
                            : 'rgba(245, 158, 11, 0.15)',
                        color:
                          item.status === 'completed'
                            ? '#6ee7b7'
                            : item.status === 'in_progress'
                            ? '#a5b4fc'
                            : '#fcd34d',
                        borderColor:
                          item.status === 'completed'
                            ? 'rgba(16, 185, 129, 0.3)'
                            : item.status === 'in_progress'
                            ? 'rgba(99, 102, 241, 0.3)'
                            : 'rgba(245, 158, 11, 0.3)'
                      }}
                    >
                      {item.status.replace('_', ' ')}
                    </span>
                    {item.is_demo && (
                      <span className="badge badge-demo" style={{ fontSize: '0.65rem' }}>Demo</span>
                    )}
                  </div>

                  <div style={{ display: 'flex', flexWrap: 'wrap', alignItems: 'center', gap: '0.75rem', fontSize: '0.8rem', color: 'var(--text-muted)' }}>
                    <span style={{ display: 'flex', alignItems: 'center', gap: '0.3rem' }}>
                      <Calendar size={13} /> {new Date(item.created_at).toLocaleDateString()}
                    </span>
                    <span>&bull;</span>
                    <span style={{ textTransform: 'capitalize' }}>
                      {item.experience_level}
                    </span>
                    <span>&bull;</span>
                    <span style={{ textTransform: 'capitalize' }}>
                      {item.interview_mode} mode
                    </span>
                    <span>&bull;</span>
                    <span>
                      {item.answered_count} of {item.question_count} answered
                    </span>
                  </div>
                </div>

                {/* Score & Actions */}
                <div style={{ display: 'flex', alignItems: 'center', gap: '1.25rem' }}>
                  {item.overall_score !== null && (
                    <div style={{ textAlign: 'right' }}>
                      <div style={{ fontSize: '1.35rem', fontWeight: 800, color: '#10b981' }}>
                        {item.overall_score}%
                      </div>
                      <span style={{ fontSize: '0.7rem', color: 'var(--text-muted)' }}>Score</span>
                    </div>
                  )}

                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
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
                        <PlayCircle size={15} /> Continue
                      </Link>
                    )}

                    <button
                      type="button"
                      onClick={() => setSelectedToDelete(item)}
                      className="btn btn-danger btn-sm"
                      title="Delete interview"
                      style={{ padding: '0.5rem' }}
                    >
                      <Trash2 size={15} />
                    </button>
                  </div>
                </div>
              </div>
            ))}
          </div>
        ) : (
          <div className="glass-panel" style={{ textAlign: 'center', padding: '3.5rem 1rem' }}>
            <History size={40} color="#818cf8" style={{ margin: '0 auto 1rem auto' }} />
            <h3 style={{ fontSize: '1.15rem', fontWeight: 600, marginBottom: '0.5rem' }}>No sessions found</h3>
            <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', maxWidth: '360px', margin: '0 auto 1.5rem auto' }}>
              {roleFilter || statusFilter
                ? 'Try adjusting your search query or status filter.'
                : 'Start practicing by creating your first HR interview.'}
            </p>
            <Link to="/interview/setup" className="btn btn-primary btn-sm">
              Start HR Interview
            </Link>
          </div>
        )}
      </div>

      {/* Delete Confirmation Modal */}
      <ConfirmModal
        isOpen={!!selectedToDelete}
        title="Delete Interview Record?"
        message={`Are you sure you want to delete your ${selectedToDelete?.custom_job_role} interview session? This permanently removes the saved questions, answers, and evaluation report.`}
        confirmText="Yes, Delete Session"
        cancelText="Cancel"
        isDanger={true}
        isLoading={isDeleting}
        onConfirm={handleDeleteConfirm}
        onCancel={() => setSelectedToDelete(null)}
      />
    </div>
  );
};
