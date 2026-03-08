import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import About from '../components/About';

describe('About', () => {
  it('renders the about section heading', () => {
    render(<About />);
    expect(screen.getByText('About Me')).toBeInTheDocument();
  });

  it('renders the name', () => {
    render(<About />);
    expect(screen.getByText('Hi, I\'m Babajide Salami')).toBeInTheDocument();
  });

  it('renders key skills mentioned', () => {
    render(<About />);
    expect(screen.getByText(/RLHF/i)).toBeInTheDocument();
    expect(screen.getByText(/LLM evaluation/i)).toBeInTheDocument();
    expect(screen.getByText(/data annotation/i)).toBeInTheDocument();
  });

  it('renders languages', () => {
    render(<About />);
    expect(screen.getByText('English • Native')).toBeInTheDocument();
    expect(screen.getByText('Yoruba • Fluent')).toBeInTheDocument();
    expect(screen.getByText('French • Conversational')).toBeInTheDocument();
  });

  it('renders stats', () => {
    render(<About />);
    expect(screen.getByText('5+')).toBeInTheDocument();
    expect(screen.getByText('10+')).toBeInTheDocument();
    expect(screen.getByText('8+')).toBeInTheDocument();
    expect(screen.getByText('20+')).toBeInTheDocument();
  });
});
