"""
Test configuration and fixtures
"""

import pytest
import os
import sys

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app import create_app
from models import db


@pytest.fixture
def app():
    """Create application for testing"""
    app = create_app()
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['WTF_CSRF_ENABLED'] = False
    app.config['SECRET_KEY'] = 'test-secret-key'
    
    with app.app_context():
        db.create_all()
        yield app
        db.session.remove()
        db.drop_all()


@pytest.fixture
def client(app):
    """Create test client"""
    return app.test_client()


@pytest.fixture
def runner(app):
    """Create test CLI runner"""
    return app.test_cli_runner()


@pytest.fixture
def sample_profile_data():
    """Sample profile data for testing"""
    return {
        'name': 'Test User',
        'title': 'Software Engineer',
        'location': 'Test City, Test Country',
        'email': 'test@example.com',
        'phone': '+1234567890',
        'summary': 'Test summary',
        'github_url': 'https://github.com/testuser',
        'linkedin_url': 'https://linkedin.com/in/testuser',
        'portfolio_url': 'https://testuser.com'
    }


@pytest.fixture
def sample_experience_data():
    """Sample experience data for testing"""
    return {
        'company': 'Test Company',
        'position': 'Software Engineer',
        'location': 'Remote',
        'start_date': 'Jan 2023',
        'end_date': 'Present',
        'is_current': True,
        'description': 'Test description',
        'responsibilities': ['Responsibility 1', 'Responsibility 2']
    }


@pytest.fixture
def sample_skill_data():
    """Sample skill data for testing"""
    return {
        'name': 'Python',
        'category': 'Languages & Frameworks',
        'proficiency_level': 95,
        'years_of_experience': 5
    }


@pytest.fixture
def sample_project_data():
    """Sample project data for testing"""
    return {
        'title': 'Test Project',
        'description': 'Test project description',
        'technologies': ['Python', 'Flask', 'React'],
        'duration': '3 months',
        'role': 'Lead Developer',
        'features': ['Feature 1', 'Feature 2'],
        'github_url': 'https://github.com/testuser/test-project'
    }
