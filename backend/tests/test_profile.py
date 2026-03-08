"""
Tests for Profile API endpoints
"""

import pytest
import json
from models import Profile


class TestProfileResource:
    """Test Profile API endpoints"""
    
    def test_get_profiles_empty(self, client):
        """Test getting profiles when database is empty"""
        response = client.get('/api/profiles')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'profiles' in data
        assert len(data['profiles']) == 0
    
    def test_create_profile(self, client, sample_profile_data):
        """Test creating a new profile"""
        response = client.post(
            '/api/profiles',
            json=sample_profile_data,
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == sample_profile_data['name']
        assert data['email'] == sample_profile_data['email']
        assert 'id' in data
    
    def test_create_profile_duplicate_email(self, client, sample_profile_data):
        """Test creating profile with duplicate email"""
        # Create first profile
        client.post('/api/profiles', json=sample_profile_data)
        
        # Try to create another with same email
        response = client.post(
            '/api/profiles',
            json=sample_profile_data,
            content_type='application/json'
        )
        assert response.status_code == 400
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_create_profile_missing_required_fields(self, client):
        """Test creating profile with missing required fields"""
        response = client.post(
            '/api/profiles',
            json={'name': 'Test'},  # Missing required fields
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_get_profile_by_id(self, client, sample_profile_data):
        """Test getting profile by ID"""
        # Create profile
        create_response = client.post('/api/profiles', json=sample_profile_data)
        profile_id = json.loads(create_response.data)['id']
        
        # Get profile
        response = client.get(f'/api/profile/{profile_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == profile_id
        assert data['name'] == sample_profile_data['name']
    
    def test_get_profile_not_found(self, client):
        """Test getting non-existent profile"""
        response = client.get('/api/profile/999')
        assert response.status_code == 404
    
    def test_update_profile(self, client, sample_profile_data):
        """Test updating a profile"""
        # Create profile
        create_response = client.post('/api/profiles', json=sample_profile_data)
        profile_id = json.loads(create_response.data)['id']
        
        # Update profile
        update_data = {'title': 'Senior Software Engineer'}
        response = client.put(
            f'/api/profile/{profile_id}',
            json=update_data,
            content_type='application/json'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['title'] == 'Senior Software Engineer'
    
    def test_delete_profile(self, client, sample_profile_data):
        """Test deleting a profile"""
        # Create profile
        create_response = client.post('/api/profiles', json=sample_profile_data)
        profile_id = json.loads(create_response.data)['id']
        
        # Delete profile
        response = client.delete(f'/api/profile/{profile_id}')
        assert response.status_code == 200
        
        # Verify deletion
        get_response = client.get(f'/api/profile/{profile_id}')
        assert get_response.status_code == 404
    
    def test_get_main_profile(self, client, sample_profile_data):
        """Test getting main profile (without ID)"""
        client.post('/api/profiles', json=sample_profile_data)
        
        response = client.get('/api/profile')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['email'] == sample_profile_data['email']


class TestProfileModel:
    """Test Profile model"""
    
    def test_create_profile(self, app, sample_profile_data):
        """Test creating profile directly with model"""
        with app.app_context():
            profile = Profile(**sample_profile_data)
            db.session.add(profile)
            db.session.commit()
            
            assert profile.id is not None
            assert profile.name == sample_profile_data['name']
    
    def test_profile_to_dict(self, app, sample_profile_data):
        """Test profile to_dict method"""
        with app.app_context():
            profile = Profile(**sample_profile_data)
            db.session.add(profile)
            db.session.commit()
            
            profile_dict = profile.to_dict()
            assert profile_dict['name'] == sample_profile_data['name']
            assert profile_dict['email'] == sample_profile_data['email']
