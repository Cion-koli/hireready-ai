import React from 'react';

export const ScoreGauge = ({ score = 0, size = 180, strokeWidth = 14, label = "Practice Score" }) => {
  const safeScore = Math.max(0, Math.min(100, Math.round(score || 0)));
  const radius = (size - strokeWidth) / 2;
  const circumference = 2 * Math.PI * radius;
  const strokeDashoffset = circumference - (safeScore / 100) * circumference;

  let color = '#10b981'; // Green (80+)
  let grade = 'Excellent';
  if (safeScore < 50) {
    color = '#f43f5e';
    grade = 'Needs Practice';
  } else if (safeScore < 70) {
    color = '#f59e0b';
    grade = 'Developing';
  } else if (safeScore < 85) {
    color = '#6366f1';
    grade = 'Proficient';
  }

  return (
    <div style={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      justifyContent: 'center',
      position: 'relative'
    }}>
      <svg width={size} height={size} style={{ transform: 'rotate(-90deg)' }}>
        {/* Background Track */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke="rgba(255, 255, 255, 0.08)"
          strokeWidth={strokeWidth}
          fill="transparent"
        />
        {/* Progress Arc */}
        <circle
          cx={size / 2}
          cy={size / 2}
          r={radius}
          stroke={color}
          strokeWidth={strokeWidth}
          strokeDasharray={circumference}
          strokeDashoffset={strokeDashoffset}
          strokeLinecap="round"
          fill="transparent"
          style={{
            transition: 'stroke-dashoffset 1s ease-in-out, stroke 0.5s ease',
            filter: `drop-shadow(0 0 10px ${color}66)`
          }}
        />
      </svg>

      {/* Inside Content */}
      <div style={{
        position: 'absolute',
        textAlign: 'center',
        display: 'flex',
        flexDirection: 'column',
        alignItems: 'center'
      }}>
        <span style={{
          fontSize: size > 150 ? '2.5rem' : '1.75rem',
          fontWeight: 800,
          color: 'var(--text-primary)',
          lineHeight: 1
        }}>
          {safeScore}%
        </span>
        <span style={{
          fontSize: '0.75rem',
          fontWeight: 700,
          color: color,
          textTransform: 'uppercase',
          letterSpacing: '0.05em',
          marginTop: '0.25rem'
        }}>
          {grade}
        </span>
      </div>

      {label && (
        <span style={{
          fontSize: '0.85rem',
          color: 'var(--text-secondary)',
          fontWeight: 500,
          marginTop: '0.5rem'
        }}>
          {label}
        </span>
      )}
    </div>
  );
};
