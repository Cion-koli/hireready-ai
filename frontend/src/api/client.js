/**
 * HTTP Client with automatic JWT handling and error handling.
 */

const BASE_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000/api';

class ApiClient {
  getTokens() {
    try {
      const stored = localStorage.getItem('hireready_auth');
      return stored ? JSON.parse(stored) : null;
    } catch (e) {
      return null;
    }
  }

  setAuthData(data) {
    if (data) {
      localStorage.setItem('hireready_auth', JSON.stringify(data));
    } else {
      localStorage.removeItem('hireready_auth');
    }
  }

  async request(endpoint, options = {}) {
    const url = `${BASE_URL}${endpoint}`;
    const headers = {
      'Content-Type': 'application/json',
      ...options.headers,
    };

    const auth = this.getTokens();
    if (auth && auth.tokens && auth.tokens.access) {
      headers['Authorization'] = `Bearer ${auth.tokens.access}`;
    }

    const config = {
      ...options,
      headers,
    };

    try {
      const response = await fetch(url, config);

      // Handle 401 unauthorized (try refresh token if available)
      if (response.status === 401 && auth && auth.tokens && auth.tokens.refresh && !options._retry) {
        options._retry = true;
        const refreshed = await this.refreshToken(auth.tokens.refresh);
        if (refreshed) {
          headers['Authorization'] = `Bearer ${refreshed.access}`;
          return fetch(url, { ...options, headers });
        } else {
          this.setAuthData(null);
          window.location.href = '/login';
          throw new Error('Session expired. Please log in again.');
        }
      }

      if (response.status === 204) {
        return null;
      }

      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        const errorMsg = data.error || (data.detail) || (typeof data === 'object' ? Object.values(data).flat().join(' ') : 'Request failed');
        const err = new Error(errorMsg);
        err.status = response.status;
        err.data = data;
        throw err;
      }

      return data;
    } catch (error) {
      throw error;
    }
  }

  async refreshToken(refresh) {
    try {
      const response = await fetch(`${BASE_URL}/auth/token/refresh/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ refresh }),
      });
      if (response.ok) {
        const data = await response.json();
        const auth = this.getTokens();
        if (auth) {
          auth.tokens.access = data.access;
          this.setAuthData(auth);
        }
        return data;
      }
      return null;
    } catch {
      return null;
    }
  }

  get(endpoint, options = {}) {
    return this.request(endpoint, { ...options, method: 'GET' });
  }

  post(endpoint, body, options = {}) {
    return this.request(endpoint, { ...options, method: 'POST', body: JSON.stringify(body) });
  }

  patch(endpoint, body, options = {}) {
    return this.request(endpoint, { ...options, method: 'PATCH', body: JSON.stringify(body) });
  }

  delete(endpoint, options = {}) {
    return this.request(endpoint, { ...options, method: 'DELETE' });
  }
}

export const api = new ApiClient();
