"""
Tests for Marshmallow Schemas
"""

import pytest
from schemas import (
    ProfileSchema, ExperienceSchema, EducationSchema, 
    SkillSchema, ProjectSchema, CertificationSchema, 
    AwardSchema, ContactMessageSchema
)


class TestProfileSchema:
    """Test Profile Schema validation"""
    
    def test_valid_profile(self):
        """Test valid profile data"""
        schema = ProfileSchema()
        data = {
            'name': 'Test User',
            'title': 'Engineer',
            'email': 'test@example.com'
        }
        result = schema.load(data)
        assert result['name'] == 'Test User'
    
    def test_invalid_email(self):
        """Test invalid email validation"""
        schema = ProfileSchema()
        data = {
            'name': 'Test User',
            'title': 'Engineer',
            'email': 'invalid-email'
        }
        with pytest.raises(Exception):
            schema.load(data)
    
    def test_missing_required_fields(self):
        """Test missing required fields"""
        schema = ProfileSchema()
        data = {'name': 'Test'}  # Missing title and email
        with pytest.raises(Exception):
            schema.load(data)
    
    def test_name_length_validation(self):
        """Test name length validation"""
        schema = ProfileSchema()
        data = {
            'name': 'A' * 101,  # Exceeds max length
            'title': 'Engineer',
            'email': 'test@example.com'
        }
        with pytest.raises(Exception):
            schema.load(data)


class TestExperienceSchema:
    """Test Experience Schema validation"""
    
    def test_valid_experience(self):
        """Test valid experience data"""
        schema = ExperienceSchema()
        data = {
            'company': 'Test Corp',
            'position': 'Developer',
            'start_date': 'Jan 2023',
            'is_current': True
        }
        result = schema.load(data)
        assert result['company'] == 'Test Corp'
    
    def test_end_date_required(self):
        """Test end_date required when not current"""
        schema = ExperienceSchema()
        data = {
            'company': 'Test Corp',
            'position': 'Developer',
            'start_date': 'Jan 2023',
            'is_current': False
        }
        with pytest.raises(Exception):
            schema.load(data)


class TestSkillSchema:
    """Test Skill Schema validation"""
    
    def test_valid_skill(self):
        """Test valid skill data"""
        schema = SkillSchema()
        data = {
            'name': 'Python',
            'category': 'Languages',
            'proficiency_level': 90
        }
        result = schema.load(data)
        assert result['proficiency_level'] == 90
    
    def test_proficiency_range(self):
        """Test proficiency level range"""
        schema = SkillSchema()
        
        # Test too high
        data = {'name': 'Test', 'category': 'Test', 'proficiency_level': 101}
        with pytest.raises(Exception):
            schema.load(data)
        
        # Test too low
        data = {'name': 'Test', 'category': 'Test', 'proficiency_level': 0}
        with pytest.raises(Exception):
            schema.load(data)


class TestProjectSchema:
    """Test Project Schema validation"""
    
    def test_valid_project(self):
        """Test valid project data"""
        schema = ProjectSchema()
        data = {
            'title': 'Test Project',
            'technologies': ['Python', 'Flask'],
            'features': ['Feature 1', 'Feature 2']
        }
        result = schema.load(data)
        assert isinstance(result['technologies'], list)
    
    def test_title_required(self):
        """Test title is required"""
        schema = ProjectSchema()
        data = {'description': 'Test'}
        with pytest.raises(Exception):
            schema.load(data)


class TestCertificationSchema:
    """Test Certification Schema validation"""
    
    def test_valid_certification(self):
        """Test valid certification data"""
        schema = CertificationSchema()
        data = {
            'name': 'AWS Certified',
            'issuer': 'Amazon Web Services',
            'issue_date': '2024'
        }
        result = schema.load(data)
        assert result['name'] == 'AWS Certified'
    
    def test_required_fields(self):
        """Test required fields"""
        schema = CertificationSchema()
        data = {'name': 'Test'}  # Missing issuer
        with pytest.raises(Exception):
            schema.load(data)


class TestAwardSchema:
    """Test Award Schema validation"""
    
    def test_valid_award(self):
        """Test valid award data"""
        schema = AwardSchema()
        data = {
            'title': 'Best Employee',
            'organization': 'Test Corp',
            'year': '2024'
        }
        result = schema.load(data)
        assert result['title'] == 'Best Employee'


class TestContactMessageSchema:
    """Test Contact Message Schema validation"""
    
    def test_valid_message(self):
        """Test valid contact message"""
        schema = ContactMessageSchema()
        data = {
            'name': 'Test User',
            'email': 'test@example.com',
            'message': 'Hello!'
        }
        result = schema.load(data)
        assert result['name'] == 'Test User'
    
    def test_invalid_email(self):
        """Test invalid email in contact message"""
        schema = ContactMessageSchema()
        data = {
            'name': 'Test User',
            'email': 'invalid',
            'message': 'Hello!'
        }
        with pytest.raises(Exception):
            schema.load(data)
    
    def test_message_required(self):
        """Test message is required"""
        schema = ContactMessageSchema()
        data = {
            'name': 'Test User',
            'email': 'test@example.com'
        }
        with pytest.raises(Exception):
            schema.load(data)
