import { api } from './client';

export const interviewsApi = {
  create: (data) => api.post('/interviews/', data),
  list: (params = {}) => {
    const query = new URLSearchParams(params).toString();
    return api.get(`/interviews/${query ? `?${query}` : ''}`);
  },
  get: (id) => api.get(`/interviews/${id}/`),
  delete: (id) => api.delete(`/interviews/${id}/`),
  start: (id) => api.post(`/interviews/${id}/start/`, {}),
  getNextQuestion: (id) => api.get(`/interviews/${id}/questions/next/`),
  submitAnswer: (id, questionId, answerText, isVoice = false) =>
    api.post(`/interviews/${id}/answers/`, {
      question_id: questionId,
      answer_text: answerText,
      is_voice_transcribed: isVoice,
    }),
  endEarly: (id) => api.post(`/interviews/${id}/end/`, {}),
  complete: (id) => api.post(`/interviews/${id}/complete/`, {}),
};
