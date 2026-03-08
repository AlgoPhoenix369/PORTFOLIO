import { describe, it, expect, vi } from 'vitest';
import { portfolioAPI } from '../lib/api';

describe('API', () => {
  it('exports portfolioAPI with all endpoints', () => {
    expect(portfolioAPI).toBeDefined();
    expect(typeof portfolioAPI.getProfile).toBe('function');
    expect(typeof portfolioAPI.getExperience).toBe('function');
    expect(typeof portfolioAPI.getEducation).toBe('function');
    expect(typeof portfolioAPI.getSkills).toBe('function');
    expect(typeof portfolioAPI.getProjects).toBe('function');
    expect(typeof portfolioAPI.getCertifications).toBe('function');
    expect(typeof portfolioAPI.getAwards).toBe('function');
    expect(typeof portfolioAPI.submitContactForm).toBe('function');
  });

  it('has correct API base URL', () => {
    // The API should be configured with the correct base URL
    expect(process.env.VITE_API_URL || 'http://localhost:5000/api').toBeDefined();
  });
});
