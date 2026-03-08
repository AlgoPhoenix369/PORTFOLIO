import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import Hero from '../components/Hero';

describe('Hero', () => {
  it('renders the welcome message', () => {
    render(<Hero />);
    expect(screen.getByText(/welcome to my portfolio/i)).toBeInTheDocument();
  });

  it('renders the name', () => {
    render(<Hero />);
    expect(screen.getByText('Babajide Salami')).toBeInTheDocument();
  });

  it('renders the title', () => {
    render(<Hero />);
    expect(screen.getByText('AI Training Specialist & Software Engineer')).toBeInTheDocument();
  });

  it('renders the location', () => {
    render(<Hero />);
    expect(screen.getByText(/croydon, england, united kingdom/i)).toBeInTheDocument();
  });

  it('renders CTA buttons', () => {
    render(<Hero />);
    expect(screen.getByText('View My Work')).toBeInTheDocument();
    expect(screen.getByText('Download CV')).toBeInTheDocument();
  });

  it('renders social links', () => {
    render(<Hero />);
    expect(screen.getByText('GitHub')).toBeInTheDocument();
    expect(screen.getByText('LinkedIn')).toBeInTheDocument();
    expect(screen.getByText('Email')).toBeInTheDocument();
  });
});
