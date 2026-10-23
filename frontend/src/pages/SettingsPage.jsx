import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useAuth } from '../context/AuthContext';
import { ConfirmModal } from '../components/ConfirmModal';
import {
  Settings,
  User,
  Mail,
  Sliders,
  Shield,
  Trash2,
  CheckCircle2,
  AlertCircle,
  LogOut,
  Save
} from 'lucide-react';

export const SettingsPage = () => {
  const { user, updateProfile, deleteAccount, logout } = useAuth();
  const navigate = useNavigate();

  const [name, setName] = useState(
    `${user?.first_name || ''} ${user?.last_name || ''}`.trim()
  );
  const [preferredMode, setPreferredMode] = useState(
    user?.profile?.preferred_mode || 'text'
  );
  const [defaultExperience, setDefaultExperience] = useState(
    user?.profile?.default_experience_level || 'entry'
  );
  const [targetRole, setTargetRole] = useState(
    user?.profile?.target_role || ''
  );

  const [isLoading, setIsLoading] = useState(false);
  const [successMsg, setSuccessMsg] = useState(null);
  const [errorMsg, setErrorMsg] = useState(null);

  // Delete modal state
  const [deleteModalOpen, setDeleteModalOpen] = useState(false);
  const [isDeleting, setIsDeleting] = useState(false);

  const handleSave = async (e) => {
    e.preventDefault();
    setIsLoading(true);
    setSuccessMsg(null);
    setErrorMsg(null);

    try {
      await updateProfile({
        name,
        preferred_mode: preferredMode,
        default_experience_level: defaultExperience,
        target_role: targetRole,
      });
      setSuccessMsg('Profile and preferences updated successfully.');
      setTimeout(() => setSuccessMsg(null), 4000);
    } catch (err) {
      console.error('Failed to update profile:', err);
      setErrorMsg(err.message || 'Could not save settings.');
    } finally {
      setIsLoading(false);
    }
  };

  const handleDeleteAccount = async () => {
    setIsDeleting(true);
    try {
      await deleteAccount();
      navigate('/');
    } catch (err) {
      console.error('Failed to delete account:', err);
      setErrorMsg('Failed to delete account.');
    } finally {
      setIsDeleting(false);
      setDeleteModalOpen(false);
    }
  };

  return (
    <div className="container" style={{ padding: '2.5rem 1.5rem', maxWidth: '780px', position: 'relative' }}>
      <div className="bg-glow-orb orb-primary" style={{ top: 0, left: '30%' }} />

      <div style={{ marginBottom: '2rem', position: 'relative', zIndex: 1 }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', color: '#818cf8', marginBottom: '0.25rem' }}>
          <Settings size={18} />
          <span style={{ fontSize: '0.8rem', fontWeight: 700, textTransform: 'uppercase', letterSpacing: '0.05em' }}>
            Account & Preferences
          </span>
        </div>
        <h1 className="heading-1">User Settings</h1>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.9rem', marginTop: '0.2rem' }}>
          Manage your personal details, default interview mode, and account security
        </p>
      </div>

      {successMsg && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.85rem 1.25rem',
          borderRadius: 'var(--radius-md)',
          background: 'rgba(16, 185, 129, 0.15)',
          border: '1px solid rgba(16, 185, 129, 0.3)',
          color: '#6ee7b7',
          fontSize: '0.9rem',
          marginBottom: '1.5rem',
          position: 'relative',
          zIndex: 1
        }}>
          <CheckCircle2 size={18} style={{ flexShrink: 0 }} />
          <span>{successMsg}</span>
        </div>
      )}

      {errorMsg && (
        <div style={{
          display: 'flex',
          alignItems: 'center',
          gap: '0.5rem',
          padding: '0.85rem 1.25rem',
          borderRadius: 'var(--radius-md)',
          background: 'rgba(244, 63, 94, 0.15)',
          border: '1px solid rgba(244, 63, 94, 0.3)',
          color: '#fb7185',
          fontSize: '0.9rem',
          marginBottom: '1.5rem',
          position: 'relative',
          zIndex: 1
        }}>
          <AlertCircle size={18} style={{ flexShrink: 0 }} />
          <span>{errorMsg}</span>
        </div>
      )}

      <form onSubmit={handleSave} style={{ position: 'relative', zIndex: 1 }}>
        {/* Profile Card */}
        <div className="glass-panel" style={{ padding: '2rem', marginBottom: '1.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
            <User size={18} color="#818cf8" />
            <h3 className="heading-3">Profile Details</h3>
          </div>

          <div className="input-group">
            <label className="input-label" htmlFor="settings-name">Full Name</label>
            <input
              id="settings-name"
              type="text"
              className="input-field"
              value={name}
              onChange={(e) => setName(e.target.value)}
              placeholder="Your Name"
            />
          </div>

          <div className="input-group">
            <label className="input-label" htmlFor="settings-email">Email Address</label>
            <input
              id="settings-email"
              type="email"
              className="input-field"
              value={user?.email || ''}
              disabled
              style={{ opacity: 0.6, cursor: 'not-allowed' }}
            />
            <span style={{ fontSize: '0.75rem', color: 'var(--text-muted)' }}>
              Email address cannot be changed directly.
            </span>
          </div>

          <div className="input-group" style={{ marginBottom: 0 }}>
            <label className="input-label" htmlFor="settings-target-role">Default Target Role (Optional)</label>
            <input
              id="settings-target-role"
              type="text"
              className="input-field"
              value={targetRole}
              onChange={(e) => setTargetRole(e.target.value)}
              placeholder="e.g. Full-Stack Developer, Data Analyst..."
            />
          </div>
        </div>

        {/* Preferences Card */}
        <div className="glass-panel" style={{ padding: '2rem', marginBottom: '1.75rem' }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.6rem', marginBottom: '1.25rem' }}>
            <Sliders size={18} color="#818cf8" />
            <h3 className="heading-3">Interview Defaults</h3>
          </div>

          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(240px, 1fr))', gap: '1.25rem' }}>
            <div className="input-group" style={{ marginBottom: 0 }}>
              <label className="input-label">Preferred Interview Mode</label>
              <select
                className="input-field"
                value={preferredMode}
                onChange={(e) => setPreferredMode(e.target.value)}
              >
                <option value="text">Text Interview (Type responses)</option>
                <option value="voice">Voice Interview (Speak & Listen)</option>
              </select>
            </div>

            <div className="input-group" style={{ marginBottom: 0 }}>
              <label className="input-label">Default Experience Level</label>
              <select
                className="input-field"
                value={defaultExperience}
                onChange={(e) => setDefaultExperience(e.target.value)}
              >
                <option value="fresher">Fresher</option>
                <option value="entry">Entry-level</option>
                <option value="experienced">Experienced</option>
              </select>
            </div>
          </div>
        </div>

        <button
          type="submit"
          className="btn btn-primary"
          disabled={isLoading}
          id="save-settings-btn"
          style={{ marginBottom: '2.5rem' }}
        >
          <Save size={16} /> {isLoading ? 'Saving...' : 'Save Changes'}
        </button>
      </form>

      {/* Danger Zone */}
      <div className="glass-panel" style={{ padding: '2rem', border: '1px solid rgba(244, 63, 94, 0.3)', position: 'relative', zIndex: 1 }}>
        <h3 className="heading-3" style={{ color: '#fb7185', marginBottom: '0.5rem' }}>
          Danger Zone
        </h3>
        <p style={{ color: 'var(--text-secondary)', fontSize: '0.875rem', lineHeight: 1.5, marginBottom: '1.25rem' }}>
          Permanently delete your user account and all associated interview sessions, answers, and evaluation reports. This action cannot be undone.
        </p>

        <button
          type="button"
          onClick={() => setDeleteModalOpen(true)}
          className="btn btn-danger btn-sm"
          id="delete-account-btn"
        >
          <Trash2 size={16} /> Delete Account Permanently
        </button>
      </div>

      {/* Delete Account Confirm Modal */}
      <ConfirmModal
        isOpen={deleteModalOpen}
        title="Permanently Delete Account?"
        message="Are you completely sure? This will immediately remove all your interview sessions, scores, and personal records from HireReady AI."
        confirmText="Yes, Delete My Account"
        cancelText="Keep Account"
        isDanger={true}
        isLoading={isDeleting}
        onConfirm={handleDeleteAccount}
        onCancel={() => setDeleteModalOpen(false)}
      />
    </div>
  );
};
