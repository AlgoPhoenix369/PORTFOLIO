"""
Tests for Experience API endpoints
"""

import pytest
import json
from models import Experience


class TestExperienceResource:
    """Test Experience API endpoints"""
    
    def test_get_experiences_empty(self, client):
        """Test getting experiences when database is empty"""
        response = client.get('/api/experiences')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'experiences' in data
        assert len(data['experiences']) == 0
    
    def test_create_experience(self, client, sample_experience_data):
        """Test creating a new experience"""
        response = client.post(
            '/api/experiences',
            json=sample_experience_data,
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['company'] == sample_experience_data['company']
        assert data['position'] == sample_experience_data['position']
        assert 'id' in data
    
    def test_create_experience_missing_required(self, client):
        """Test creating experience with missing required fields"""
        response = client.post(
            '/api/experiences',
            json={'company': 'Test'},  # Missing position
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_get_experience_by_id(self, client, sample_experience_data):
        """Test getting experience by ID"""
        create_response = client.post('/api/experiences', json=sample_experience_data)
        experience_id = json.loads(create_response.data)['id']
        
        response = client.get(f'/api/experience/{experience_id}')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['id'] == experience_id
    
    def test_update_experience(self, client, sample_experience_data):
        """Test updating an experience"""
        create_response = client.post('/api/experiences', json=sample_experience_data)
        experience_id = json.loads(create_response.data)['id']
        
        update_data = {'position': 'Senior Software Engineer'}
        response = client.put(
            f'/api/experience/{experience_id}',
            json=update_data,
            content_type='application/json'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['position'] == 'Senior Software Engineer'
    
    def test_delete_experience(self, client, sample_experience_data):
        """Test deleting an experience"""
        create_response = client.post('/api/experiences', json=sample_experience_data)
        experience_id = json.loads(create_response.data)['id']
        
        response = client.delete(f'/api/experience/{experience_id}')
        assert response.status_code == 200
        
        get_response = client.get(f'/api/experience/{experience_id}')
        assert get_response.status_code == 404


class TestSkillResource:
    """Test Skill API endpoints"""
    
    def test_get_skills_empty(self, client):
        """Test getting skills when database is empty"""
        response = client.get('/api/skills')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert 'skills' in data
    
    def test_create_skill(self, client, sample_skill_data):
        """Test creating a new skill"""
        response = client.post(
            '/api/skills',
            json=sample_skill_data,
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['name'] == sample_skill_data['name']
        assert data['category'] == sample_skill_data['category']
    
    def test_get_skills_by_category(self, client, sample_skill_data):
        """Test getting skills filtered by category"""
        client.post('/api/skills', json=sample_skill_data)
        
        response = client.get('/api/skills?category=Languages%20%26%20Frameworks')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert len(data['skills']) > 0
    
    def test_invalid_proficiency_level(self, client):
        """Test creating skill with invalid proficiency level"""
        response = client.post(
            '/api/skills',
            json={
                'name': 'Test',
                'category': 'Test',
                'proficiency_level': 150  # Invalid, should be 1-100
            },
            content_type='application/json'
        )
        assert response.status_code == 400


class TestProjectResource:
    """Test Project API endpoints"""
    
    def test_get_projects_empty(self, client):
        """Test getting projects when database is empty"""
        response = client.get('/api/projects')
        assert response.status_code == 200
    
    def test_create_project(self, client, sample_project_data):
        """Test creating a new project"""
        response = client.post(
            '/api/projects',
            json=sample_project_data,
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert data['title'] == sample_project_data['title']
    
    def test_create_project_missing_title(self, client):
        """Test creating project without title"""
        response = client.post(
            '/api/projects',
            json={'description': 'Test'},
            content_type='application/json'
        )
        assert response.status_code == 400
    
    def test_update_project(self, client, sample_project_data):
        """Test updating a project"""
        create_response = client.post('/api/projects', json=sample_project_data)
        project_id = json.loads(create_response.data)['id']
        
        update_data = {'title': 'Updated Project Title'}
        response = client.put(
            f'/api/project/{project_id}',
            json=update_data,
            content_type='application/json'
        )
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['title'] == 'Updated Project Title'


class TestHealthCheck:
    """Test health check endpoint"""
    
    def test_health_check(self, client):
        """Test health check endpoint"""
        response = client.get('/api/health')
        assert response.status_code == 200
        data = json.loads(response.data)
        assert data['status'] == 'healthy'


class TestErrorHandlers:
    """Test error handlers"""
    
    def test_404_error(self, client):
        """Test 404 error handler"""
        response = client.get('/api/nonexistent')
        assert response.status_code == 404
        data = json.loads(response.data)
        assert 'error' in data
    
    def test_contact_form(self, client):
        """Test contact form submission"""
        response = client.post(
            '/api/contact',
            json={
                'name': 'Test User',
                'email': 'test@example.com',
                'subject': 'Test Subject',
                'message': 'Test Message'
            },
            content_type='application/json'
        )
        assert response.status_code == 201
        data = json.loads(response.data)
        assert 'message' in data
        assert data['message'] == 'Contact message sent successfully'
