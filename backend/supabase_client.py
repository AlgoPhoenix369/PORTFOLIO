"""
Supabase Client Configuration
"""

import os
from supabase import create_client, Client

# Supabase configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')


def get_supabase_client() -> Client:
    """Create and return a Supabase client"""
    if not SUPABASE_URL or not SUPABASE_KEY:
        raise ValueError("Supabase URL and Key must be set in environment variables")
    
    return create_client(SUPABASE_URL, SUPABASE_KEY)


# Initialize client
supabase = get_supabase_client() if SUPABASE_URL and SUPABASE_KEY else None


def get_profile():
    """Get profile data from Supabase"""
    if supabase:
        response = supabase.table('profiles').select('*').execute()
        return response.data
    return None


def get_experiences():
    """Get all experiences from Supabase"""
    if supabase:
        response = supabase.table('experiences').select('*').order_by('start_date', desc=True).execute()
        return response.data
    return None


def get_educations():
    """Get all educations from Supabase"""
    if supabase:
        response = supabase.table('educations').select('*').order_by('end_date', desc=True).execute()
        return response.data
    return None


def get_skills(category=None):
    """Get skills from Supabase, optionally filtered by category"""
    if supabase:
        query = supabase.table('skills').select('*')
        if category:
            query = query.eq('category', category)
        response = query.order_by('category', 'proficiency_level').execute()
        return response.data
    return None


def get_projects():
    """Get all projects from Supabase"""
    if supabase:
        response = supabase.table('projects').select('*').order_by('created_at', desc=True).execute()
        return response.data
    return None


def get_certifications():
    """Get all certifications from Supabase"""
    if supabase:
        response = supabase.table('certifications').select('*').order_by('issue_date', desc=True).execute()
        return response.data
    return None


def get_awards():
    """Get all awards from Supabase"""
    if supabase:
        response = supabase.table('awards').select('*').order_by('year', desc=True).execute()
        return response.data
    return None


def submit_contact_message(name, email, subject, message):
    """Submit a contact message to Supabase"""
    if supabase:
        data = {
            'name': name,
            'email': email,
            'subject': subject,
            'message': message,
        }
        response = supabase.table('contact_messages').insert(data).execute()
        return response.data
    return None
