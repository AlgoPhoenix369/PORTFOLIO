"""
Profile API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_profiles, get_profile_by_id, create_profile, 
    update_profile, delete_profile
)


class ProfileListResource(Resource):
    """Resource for listing and creating profiles"""
    
    def get(self):
        """Get all profiles"""
        try:
            profiles = get_all_profiles()
            return make_response(jsonify({'profiles': profiles}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new profile"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True, help='Name is required')
            parser.add_argument('title', type=str, required=True, help='Title is required')
            parser.add_argument('location', type=str)
            parser.add_argument('email', type=str, required=True, help='Email is required')
            parser.add_argument('phone', type=str)
            parser.add_argument('summary', type=str)
            parser.add_argument('github_url', type=str)
            parser.add_argument('linkedin_url', type=str)
            parser.add_argument('portfolio_url', type=str)
            
            data = parser.parse_args()
            
            # Check for duplicate email
            existing = get_all_profiles()
            if any(p['email'] == data['email'] for p in existing):
                return make_response(jsonify({'error': 'Email already exists'}), 400)
            
            profile = create_profile(data)
            
            if profile:
                return make_response(jsonify(profile), 201)
            else:
                return make_response(jsonify({'error': 'Failed to create profile'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class ProfileResource(Resource):
    """Resource for single profile operations"""
    
    def get(self, id=None):
        """Get profile by ID or get main profile"""
        try:
            if id:
                profile = get_profile_by_id(id)
            else:
                profiles = get_all_profiles()
                profile = profiles[0] if profiles else None
            
            if not profile:
                return make_response(jsonify({'error': 'Profile not found'}), 404)
            
            return make_response(jsonify(profile), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update profile"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('title', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('email', type=str)
            parser.add_argument('phone', type=str)
            parser.add_argument('summary', type=str)
            parser.add_argument('github_url', type=str)
            parser.add_argument('linkedin_url', type=str)
            parser.add_argument('portfolio_url', type=str)
            
            data = parser.parse_args()
            # Remove None values
            update_data = {k: v for k, v in data.items() if v is not None}
            
            profile = update_profile(id, update_data)
            
            if profile:
                return make_response(jsonify(profile), 200)
            else:
                return make_response(jsonify({'error': 'Profile not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete profile"""
        try:
            if delete_profile(id):
                return make_response(jsonify({'message': 'Profile deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': 'Profile not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
