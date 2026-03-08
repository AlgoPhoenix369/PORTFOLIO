import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import Navbar from '../components/Navbar';

describe('Navbar', () => {
  it('renders the logo', () => {
    render(<Navbar />);
    expect(screen.getByText('BS')).toBeInTheDocument();
  });

  it('renders navigation links', () => {
    render(<Navbar />);
    expect(screen.getByText('Home')).toBeInTheDocument();
    expect(screen.getByText('About')).toBeInTheDocument();
    expect(screen.getByText('Experience')).toBeInTheDocument();
    expect(screen.getByText('Skills')).toBeInTheDocument();
    expect(screen.getByText('Projects')).toBeInTheDocument();
    expect(screen.getByText('Education')).toBeInTheDocument();
    expect(screen.getByText('Contact')).toBeInTheDocument();
  });

  it('renders social links', () => {
    render(<Navbar />);
    // GitHub link
    const githubLink = screen.getByRole('link', { name: /github/i });
    expect(githubLink).toHaveAttribute('href', 'https://github.com/PhoenixAlgo369');
  });
});
