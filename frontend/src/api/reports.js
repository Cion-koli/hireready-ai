import { api } from './client';

export const reportsApi = {
  getReport: (id) => api.get(`/reports/${id}/`),
  listUserReports: () => api.get('/reports/'),
  getDashboardStats: () => api.get('/stats/dashboard/'),
};
