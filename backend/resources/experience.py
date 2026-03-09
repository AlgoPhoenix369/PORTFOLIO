"""
Experience API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_experiences, get_experience_by_id, create_experience,
    update_experience, delete_experience
)


class ExperienceListResource(Resource):
    """Resource for listing and creating experiences"""
    
    def get(self):
        """Get all experiences"""
        try:
            experiences = get_all_experiences()
            return make_response(jsonify({'experiences': experiences}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new experience"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('company', type=str, required=True, help='Company is required')
            parser.add_argument('position', type=str, required=True, help='Position is required')
            parser.add_argument('location', type=str)
            parser.add_argument('start_date', type=str, required=True, help='Start date is required')
            parser.add_argument('end_date', type=str)
            parser.add_argument('is_current', type=bool, default=False)
            parser.add_argument('description', type=str)
            parser.add_argument('responsibilities', type=list, location='json', default=[])
            
            data = parser.parse_args()
            experience = create_experience(data)
            
            if experience:
                return make_response(jsonify(experience), 201)
            else:
                return make_response(jsonify({'error': 'Failed to create experience'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class ExperienceResource(Resource):
    """Resource for single experience operations"""
    
    def get(self, id=None):
        """Get experience by ID"""
        try:
            if id:
                experience = get_experience_by_id(id)
                if not experience:
                    return make_response(jsonify({'error': 'Experience not found'}), 404)
                return make_response(jsonify(experience), 200)
            else:
                experiences = get_all_experiences()
                return make_response(jsonify({'experiences': experiences}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update experience"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('company', type=str)
            parser.add_argument('position', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('start_date', type=str)
            parser.add_argument('end_date', type=str)
            parser.add_argument('is_current', type=bool)
            parser.add_argument('description', type=str)
            parser.add_argument('responsibilities', type=list, location='json')
            
            data = parser.parse_args()
            update_data = {k: v for k, v in data.items() if v is not None}
            
            experience = update_experience(id, update_data)
            
            if experience:
                return make_response(jsonify(experience), 200)
            else:
                return make_response(jsonify({'error': 'Experience not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete experience"""
        try:
            if delete_experience(id):
                return make_response(jsonify({'message': 'Experience deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': 'Experience not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
