import { api } from './client';

export const authApi = {
  login: (username, password) => api.post('/auth/login/', { username, password }),
  register: (userData) => api.post('/auth/register/', userData),
  getProfile: () => api.get('/auth/profile/'),
  updateProfile: (profileData) => api.patch('/auth/profile/', profileData),
  deleteAccount: () => api.delete('/auth/delete-account/'),
};
