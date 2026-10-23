import React, { createContext, useContext, useState, useEffect } from 'react';
import { authApi } from '../api/auth';
import { api } from '../api/client';

const AuthContext = createContext(null);

export const AuthProvider = ({ children }) => {
  const [user, setUser] = useState(null);
  const [tokens, setTokens] = useState(null);
  const [isLoading, setIsLoading] = useState(true);

  useEffect(() => {
    // Check localStorage on mount
    const saved = api.getTokens();
    if (saved && saved.tokens && saved.user) {
      setUser(saved.user);
      setTokens(saved.tokens);
      // Fetch fresh profile in background
      authApi.getProfile()
        .then((freshUser) => {
          setUser(freshUser);
          api.setAuthData({ tokens: saved.tokens, user: freshUser });
        })
        .catch(() => {
          // Token may be invalid
        })
        .finally(() => setIsLoading(false));
    } else {
      setIsLoading(false);
    }
  }, []);

  const login = async (username, password) => {
    const res = await authApi.login(username, password);
    setUser(res.user);
    setTokens(res.tokens);
    api.setAuthData(res);
    return res;
  };

  const register = async (userData) => {
    const res = await authApi.register(userData);
    setUser(res.user);
    setTokens(res.tokens);
    api.setAuthData(res);
    return res;
  };

  const logout = () => {
    setUser(null);
    setTokens(null);
    api.setAuthData(null);
  };

  const updateProfile = async (profileData) => {
    const updated = await authApi.updateProfile(profileData);
    setUser(updated);
    const saved = api.getTokens() || {};
    api.setAuthData({ ...saved, user: updated });
    return updated;
  };

  const deleteAccount = async () => {
    await authApi.deleteAccount();
    logout();
  };

  return (
    <AuthContext.Provider
      value={{
        user,
        tokens,
        isAuthenticated: !!user,
        isLoading,
        login,
        register,
        logout,
        updateProfile,
        deleteAccount,
      }}
    >
      {children}
    </AuthContext.Provider>
  );
};

export const useAuth = () => {
  const context = useContext(AuthContext);
  if (!context) {
    throw new Error('useAuth must be used within an AuthProvider');
  }
  return context;
};
