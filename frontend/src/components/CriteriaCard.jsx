import React from 'react';
import { Target, AlignLeft, Sparkles, MessageSquare } from 'lucide-react';

const CRITERIA_CONFIG = {
  relevance: {
    title: 'Question Relevance',
    weight: '30% Weight',
    icon: Target,
    color: '#6366f1',
    description: 'Direct alignment with prompt, addressing the core HR inquiry without drifting.'
  },
  clarity: {
    title: 'Clarity & Structure',
    weight: '25% Weight',
    icon: AlignLeft,
    color: '#8b5cf6',
    description: 'Logical flow, clear articulation, coherent beginning and conclusion.'
  },
  examples: {
    title: 'STAR & Supporting Examples',
    weight: '25% Weight',
    icon: Sparkles,
    color: '#06b6d4',
    description: 'Use of concrete Situation, Task, Action, and tangible Results.'
  },
  communication: {
    title: 'Professional Communication',
    weight: '20% Weight',
    icon: MessageSquare,
    color: '#10b981',
    description: 'Professional tone, workplace emotional intelligence, and poise.'
  }
};

export const CriteriaCard = ({ type, score = 0 }) => {
  const config = CRITERIA_CONFIG[type] || CRITERIA_CONFIG.relevance;
  const Icon = config.icon;
  const safeScore = Math.max(0, Math.min(100, Math.round(score || 0)));

  return (
    <div className="glass-panel" style={{ padding: '1.25rem' }}>
      <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'space-between', marginBottom: '0.75rem' }}>
        <div style={{ display: 'flex', alignItems: 'center', gap: '0.65rem' }}>
          <div style={{
            width: '34px',
            height: '34px',
            borderRadius: '8px',
            background: `${config.color}22`,
            display: 'flex',
            alignItems: 'center',
            justifyContent: 'center',
            color: config.color
          }}>
            <Icon size={18} />
          </div>
          <div>
            <h4 style={{ fontSize: '0.95rem', fontWeight: 600, color: 'var(--text-primary)' }}>
              {config.title}
            </h4>
            <span style={{ fontSize: '0.725rem', color: 'var(--text-muted)' }}>
              {config.weight}
            </span>
          </div>
        </div>

        <div style={{ textAlign: 'right' }}>
          <span style={{ fontSize: '1.4rem', fontWeight: 700, color: config.color }}>
            {safeScore}%
          </span>
        </div>
      </div>

      {/* Progress Bar */}
      <div style={{
        height: '6px',
        width: '100%',
        background: 'rgba(255, 255, 255, 0.08)',
        borderRadius: '3px',
        overflow: 'hidden',
        marginBottom: '0.6rem'
      }}>
        <div style={{
          height: '100%',
          width: `${safeScore}%`,
          background: config.color,
          borderRadius: '3px',
          transition: 'width 0.8s ease'
        }} />
      </div>

      <p style={{ fontSize: '0.775rem', color: 'var(--text-secondary)', lineHeight: 1.4 }}>
        {config.description}
      </p>
    </div>
  );
};
