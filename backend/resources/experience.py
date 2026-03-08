"""
Experience API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Experience
from schemas import ExperienceSchema, ExperienceListSchema

experience_schema = ExperienceSchema()
experience_list_schema = ExperienceListSchema()


class ExperienceListResource(Resource):
    """Resource for listing and creating experiences"""
    
    def get(self):
        """Get all experiences"""
        try:
            experiences = Experience.query.order_by(Experience.start_date.desc()).all()
            result = experience_list_schema.dump({'experiences': experiences})
            return make_response(jsonify(result), 200)
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
            
            experience = Experience(**data)
            db.session.add(experience)
            db.session.commit()
            
            result = experience_schema.dump(experience)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class ExperienceResource(Resource):
    """Resource for single experience operations"""
    
    def get(self, id=None):
        """Get experience by ID"""
        try:
            if id:
                experience = Experience.query.get_or_404(id)
            else:
                experiences = Experience.query.order_by(Experience.start_date.desc()).all()
                result = experience_list_schema.dump({'experiences': experiences})
                return make_response(jsonify(result), 200)
            
            result = experience_schema.dump(experience)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update experience"""
        try:
            experience = Experience.query.get_or_404(id)
            
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
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(experience, key, value)
            
            db.session.commit()
            
            result = experience_schema.dump(experience)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete experience"""
        try:
            experience = Experience.query.get_or_404(id)
            db.session.delete(experience)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Experience deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
