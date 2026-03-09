"""
Supabase Database Client for Flask Backend
Connects Flask to Supabase PostgreSQL database
Lazy initialization to handle missing credentials gracefully
"""

import os
from supabase import create_client, Client
from dotenv import load_dotenv

load_dotenv()

# Supabase Configuration
SUPABASE_URL = os.getenv('SUPABASE_URL')
SUPABASE_KEY = os.getenv('SUPABASE_KEY')

# Lazy initialization
_supabase_client = None

def get_supabase_client() -> Client:
    """Create and return a Supabase client (lazy initialization)"""
    global _supabase_client
    
    if _supabase_client is not None:
        return _supabase_client
    
    if not SUPABASE_URL or not SUPABASE_KEY:
        print("Warning: Supabase credentials not configured. Set SUPABASE_URL and SUPABASE_KEY")
        return None
    
    try:
        _supabase_client = create_client(SUPABASE_URL, SUPABASE_KEY)
        return _supabase_client
    except Exception as e:
        print(f"Error creating Supabase client: {e}")
        return None

# Get client instance
supabase = get_supabase_client()


def check_connection():
    """Check if Supabase connection is available"""
    return supabase is not None


# ============== Profile Functions ==============

def get_all_profiles():
    """Get all profiles from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('profiles').select('*').execute()
        return response.data
    except Exception as e:
        print(f"Error fetching profiles: {e}")
        return []

def get_profile_by_id(profile_id):
    """Get profile by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('profiles').select('*').eq('id', profile_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching profile: {e}")
        return None

def create_profile(data):
    """Create new profile"""
    if not supabase:
        return None
    try:
        response = supabase.table('profiles').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating profile: {e}")
        return None

def update_profile(profile_id, data):
    """Update profile"""
    if not supabase:
        return None
    try:
        response = supabase.table('profiles').update(data).eq('id', profile_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating profile: {e}")
        return None

def delete_profile(profile_id):
    """Delete profile"""
    if not supabase:
        return False
    try:
        response = supabase.table('profiles').delete().eq('id', profile_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting profile: {e}")
        return False


# ============== Experience Functions ==============

def get_all_experiences():
    """Get all experiences from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('experiences').select('*').order('start_date', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching experiences: {e}")
        return []

def get_experience_by_id(exp_id):
    """Get experience by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('experiences').select('*').eq('id', exp_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching experience: {e}")
        return None

def create_experience(data):
    """Create new experience"""
    if not supabase:
        return None
    try:
        response = supabase.table('experiences').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating experience: {e}")
        return None

def update_experience(exp_id, data):
    """Update experience"""
    if not supabase:
        return None
    try:
        response = supabase.table('experiences').update(data).eq('id', exp_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating experience: {e}")
        return None

def delete_experience(exp_id):
    """Delete experience"""
    if not supabase:
        return False
    try:
        response = supabase.table('experiences').delete().eq('id', exp_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting experience: {e}")
        return False


# ============== Education Functions ==============

def get_all_educations():
    """Get all educations from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('educations').select('*').order('end_date', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching educations: {e}")
        return []

def get_education_by_id(edu_id):
    """Get education by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('educations').select('*').eq('id', edu_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching education: {e}")
        return None

def create_education(data):
    """Create new education"""
    if not supabase:
        return None
    try:
        response = supabase.table('educations').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating education: {e}")
        return None

def update_education(edu_id, data):
    """Update education"""
    if not supabase:
        return None
    try:
        response = supabase.table('educations').update(data).eq('id', edu_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating education: {e}")
        return None

def delete_education(edu_id):
    """Delete education"""
    if not supabase:
        return False
    try:
        response = supabase.table('educations').delete().eq('id', edu_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting education: {e}")
        return False


# ============== Skills Functions ==============

def get_all_skills(category=None):
    """Get all skills from Supabase"""
    if not supabase:
        return []
    try:
        query = supabase.table('skills').select('*')
        if category:
            query = query.eq('category', category)
        response = query.order('category', 'proficiency_level', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching skills: {e}")
        return []

def get_skill_by_id(skill_id):
    """Get skill by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('skills').select('*').eq('id', skill_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching skill: {e}")
        return None

def create_skill(data):
    """Create new skill"""
    if not supabase:
        return None
    try:
        response = supabase.table('skills').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating skill: {e}")
        return None

def update_skill(skill_id, data):
    """Update skill"""
    if not supabase:
        return None
    try:
        response = supabase.table('skills').update(data).eq('id', skill_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating skill: {e}")
        return None

def delete_skill(skill_id):
    """Delete skill"""
    if not supabase:
        return False
    try:
        response = supabase.table('skills').delete().eq('id', skill_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting skill: {e}")
        return False


# ============== Projects Functions ==============

def get_all_projects():
    """Get all projects from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('projects').select('*').order('created_at', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching projects: {e}")
        return []

def get_project_by_id(project_id):
    """Get project by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('projects').select('*').eq('id', project_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching project: {e}")
        return None

def create_project(data):
    """Create new project"""
    if not supabase:
        return None
    try:
        response = supabase.table('projects').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating project: {e}")
        return None

def update_project(project_id, data):
    """Update project"""
    if not supabase:
        return None
    try:
        response = supabase.table('projects').update(data).eq('id', project_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating project: {e}")
        return None

def delete_project(project_id):
    """Delete project"""
    if not supabase:
        return False
    try:
        response = supabase.table('projects').delete().eq('id', project_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting project: {e}")
        return False


# ============== Certifications Functions ==============

def get_all_certifications():
    """Get all certifications from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('certifications').select('*').order('issue_date', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching certifications: {e}")
        return []

def get_certification_by_id(cert_id):
    """Get certification by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('certifications').select('*').eq('id', cert_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching certification: {e}")
        return None

def create_certification(data):
    """Create new certification"""
    if not supabase:
        return None
    try:
        response = supabase.table('certifications').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating certification: {e}")
        return None

def update_certification(cert_id, data):
    """Update certification"""
    if not supabase:
        return None
    try:
        response = supabase.table('certifications').update(data).eq('id', cert_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating certification: {e}")
        return None

def delete_certification(cert_id):
    """Delete certification"""
    if not supabase:
        return False
    try:
        response = supabase.table('certifications').delete().eq('id', cert_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting certification: {e}")
        return False


# ============== Awards Functions ==============

def get_all_awards():
    """Get all awards from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('awards').select('*').order('year', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching awards: {e}")
        return []

def get_award_by_id(award_id):
    """Get award by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('awards').select('*').eq('id', award_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching award: {e}")
        return None

def create_award(data):
    """Create new award"""
    if not supabase:
        return None
    try:
        response = supabase.table('awards').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating award: {e}")
        return None

def update_award(award_id, data):
    """Update award"""
    if not supabase:
        return None
    try:
        response = supabase.table('awards').update(data).eq('id', award_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating award: {e}")
        return None

def delete_award(award_id):
    """Delete award"""
    if not supabase:
        return False
    try:
        response = supabase.table('awards').delete().eq('id', award_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting award: {e}")
        return False


# ============== Contact Message Functions ==============

def get_all_messages():
    """Get all contact messages from Supabase"""
    if not supabase:
        return []
    try:
        response = supabase.table('contact_messages').select('*').order('created_at', desc=True).execute()
        return response.data
    except Exception as e:
        print(f"Error fetching messages: {e}")
        return []

def get_message_by_id(msg_id):
    """Get message by ID"""
    if not supabase:
        return None
    try:
        response = supabase.table('contact_messages').select('*').eq('id', msg_id).execute()
        return response.data[0] if response.data else None
    except Exception as e:
        print(f"Error fetching message: {e}")
        return None

def create_message(data):
    """Create new contact message"""
    if not supabase:
        return None
    try:
        response = supabase.table('contact_messages').insert(data).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error creating message: {e}")
        return None

def update_message(msg_id, data):
    """Update message"""
    if not supabase:
        return None
    try:
        response = supabase.table('contact_messages').update(data).eq('id', msg_id).execute()
        return response.data[0]
    except Exception as e:
        print(f"Error updating message: {e}")
        return None

def delete_message(msg_id):
    """Delete message"""
    if not supabase:
        return False
    try:
        response = supabase.table('contact_messages').delete().eq('id', msg_id).execute()
        return True
    except Exception as e:
        print(f"Error deleting message: {e}")
        return False
