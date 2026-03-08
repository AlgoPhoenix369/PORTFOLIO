"""
Skill API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Skill
from schemas import SkillSchema, SkillListSchema

skill_schema = SkillSchema()
skill_list_schema = SkillListSchema()


class SkillListResource(Resource):
    """Resource for listing and creating skills"""
    
    def get(self):
        """Get all skills, optionally filtered by category"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('category', type=str, location='args')
            args = parser.parse_args()
            
            if args.get('category'):
                skills = Skill.query.filter_by(category=args['category']).all()
            else:
                skills = Skill.query.order_by(Skill.category, Skill.proficiency_level.desc()).all()
            
            result = skill_list_schema.dump({'skills': skills})
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new skill"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True, help='Skill name is required')
            parser.add_argument('category', type=str, required=True, help='Category is required')
            parser.add_argument('proficiency_level', type=int, validate=lambda x: 1 <= x <= 100)
            parser.add_argument('years_of_experience', type=int)
            
            data = parser.parse_args()
            
            skill = Skill(**data)
            db.session.add(skill)
            db.session.commit()
            
            result = skill_schema.dump(skill)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class SkillResource(Resource):
    """Resource for single skill operations"""
    
    def get(self, id=None):
        """Get skill by ID"""
        try:
            if id:
                skill = Skill.query.get_or_404(id)
            else:
                skills = Skill.query.all()
                result = skill_list_schema.dump({'skills': skills})
                return make_response(jsonify(result), 200)
            
            result = skill_schema.dump(skill)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update skill"""
        try:
            skill = Skill.query.get_or_404(id)
            
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('category', type=str)
            parser.add_argument('proficiency_level', type=int)
            parser.add_argument('years_of_experience', type=int)
            
            data = parser.parse_args()
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(skill, key, value)
            
            db.session.commit()
            
            result = skill_schema.dump(skill)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete skill"""
        try:
            skill = Skill.query.get_or_404(id)
            db.session.delete(skill)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Skill deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
