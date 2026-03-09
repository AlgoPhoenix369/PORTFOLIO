"""
Skills API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_skills, get_skill_by_id, create_skill,
    update_skill, delete_skill
)


class SkillListResource(Resource):
    """Resource for listing and creating skills"""
    
    def get(self):
        """Get all skills, optionally filtered by category"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('category', type=str, location='args')
            args = parser.parse_args()
            
            skills = get_all_skills(args.get('category'))
            return make_response(jsonify({'skills': skills}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new skill"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True, help='Skill name is required')
            parser.add_argument('category', type=str, required=True, help='Category is required')
            parser.add_argument('proficiency_level', type=int)
            parser.add_argument('years_of_experience', type=int)
            
            data = parser.parse_args()
            skill = create_skill(data)
            
            if skill:
                return make_response(jsonify(skill), 201)
            else:
                return make_response(jsonify({'error': 'Failed to create skill'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class SkillResource(Resource):
    """Resource for single skill operations"""
    
    def get(self, id=None):
        """Get skill by ID"""
        try:
            if id:
                skill = get_skill_by_id(id)
                if not skill:
                    return make_response(jsonify({'error': 'Skill not found'}), 404)
                return make_response(jsonify(skill), 200)
            else:
                skills = get_all_skills()
                return make_response(jsonify({'skills': skills}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update skill"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('category', type=str)
            parser.add_argument('proficiency_level', type=int)
            parser.add_argument('years_of_experience', type=int)
            
            data = parser.parse_args()
            update_data = {k: v for k, v in data.items() if v is not None}
            
            skill = update_skill(id, update_data)
            
            if skill:
                return make_response(jsonify(skill), 200)
            else:
                return make_response(jsonify({'error': 'Skill not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete skill"""
        try:
            if delete_skill(id):
                return make_response(jsonify({'message': 'Skill deleted successfully'}), 200)
            else:
                return make_response(jsonify({'error': 'Skill not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
