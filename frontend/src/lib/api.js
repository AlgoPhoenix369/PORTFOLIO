import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || 'http://localhost:5000/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

// Request interceptor
api.interceptors.request.use(
  (config) => {
    const token = localStorage.getItem('token');
    if (token) {
      config.headers.Authorization = `Bearer ${token}`;
    }
    return config;
  },
  (error) => {
    return Promise.reject(error);
  }
);

// Response interceptor
api.interceptors.response.use(
  (response) => response,
  (error) => {
    if (error.response?.status === 401) {
      localStorage.removeItem('token');
      window.location.href = '/login';
    }
    return Promise.reject(error);
  }
);

// Portfolio API endpoints
export const portfolioAPI = {
  // Profile
  getProfile: () => api.get('/profile'),
  
  // Experience
  getExperience: () => api.get('/experience'),
  getExperienceById: (id) => api.get(`/experience/${id}`),
  
  // Education
  getEducation: () => api.get('/education'),
  
  // Skills
  getSkills: () => api.get('/skills'),
  
  // Projects
  getProjects: () => api.get('/projects'),
  getProjectById: (id) => api.get(`/projects/${id}`),
  
  // Certifications
  getCertifications: () => api.get('/certifications'),
  
  // Awards
  getAwards: () => api.get('/awards'),
  
  // Contact form
  submitContactForm: (data) => api.post('/contact', data),
};

export default api;
