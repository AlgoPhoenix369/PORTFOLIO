"""
Profile API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Profile
from schemas import ProfileSchema, ProfileListSchema

profile_schema = ProfileSchema()
profile_list_schema = ProfileListSchema()


class ProfileListResource(Resource):
    """Resource for listing and creating profiles"""
    
    def get(self):
        """Get all profiles"""
        try:
            profiles = Profile.query.all()
            result = profile_list_schema.dump({'profiles': profiles})
            return make_response(jsonify(result), 200)
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
            
            # Validate email uniqueness
            existing = Profile.query.filter_by(email=data['email']).first()
            if existing:
                return make_response(jsonify({'error': 'Email already exists'}), 400)
            
            profile = Profile(**data)
            db.session.add(profile)
            db.session.commit()
            
            result = profile_schema.dump(profile)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class ProfileResource(Resource):
    """Resource for single profile operations"""
    
    def get(self, id=None):
        """Get profile by ID or get main profile"""
        try:
            if id:
                profile = Profile.query.get_or_404(id)
            else:
                profile = Profile.query.first()
            
            if not profile:
                return make_response(jsonify({'error': 'Profile not found'}), 404)
            
            result = profile_schema.dump(profile)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update profile"""
        try:
            profile = Profile.query.get_or_404(id)
            
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
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(profile, key, value)
            
            db.session.commit()
            
            result = profile_schema.dump(profile)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete profile"""
        try:
            profile = Profile.query.get_or_404(id)
            db.session.delete(profile)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Profile deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
