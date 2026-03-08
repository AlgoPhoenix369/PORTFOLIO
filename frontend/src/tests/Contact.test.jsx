import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import Contact from '../components/Contact';

describe('Contact', () => {
  it('renders the contact section heading', () => {
    render(<Contact />);
    expect(screen.getByText('Get In Touch')).toBeInTheDocument();
  });

  it('renders contact information', () => {
    render(<Contact />);
    expect(screen.getByText('Email')).toBeInTheDocument();
    expect(screen.getByText('Location')).toBeInTheDocument();
    expect(screen.getByText('Phone')).toBeInTheDocument();
  });

  it('renders email address', () => {
    render(<Contact />);
    expect(screen.getByText('babajide.salami@email.com')).toBeInTheDocument();
  });

  it('renders location', () => {
    render(<Contact />);
    expect(screen.getByText('Croydon, England, United Kingdom')).toBeInTheDocument();
  });

  it('renders availability information', () => {
    render(<Contact />);
    expect(screen.getByText('Availability')).toBeInTheDocument();
    expect(screen.getByText('Location Preference')).toBeInTheDocument();
    expect(screen.getByText('Work Type')).toBeInTheDocument();
  });

  it('renders contact form', () => {
    render(<Contact />);
    expect(screen.getByLabelText('Name')).toBeInTheDocument();
    expect(screen.getByLabelText('Email')).toBeInTheDocument();
    expect(screen.getByLabelText('Subject')).toBeInTheDocument();
    expect(screen.getByLabelText('Message')).toBeInTheDocument();
    expect(screen.getByText('Send Message')).toBeInTheDocument();
  });
});
