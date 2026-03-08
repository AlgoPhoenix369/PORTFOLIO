"""
Education API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Education
from schemas import EducationSchema, EducationListSchema

education_schema = EducationSchema()
education_list_schema = EducationListSchema()


class EducationListResource(Resource):
    """Resource for listing and creating educations"""
    
    def get(self):
        """Get all educations"""
        try:
            educations = Education.query.order_by(Education.end_date.desc()).all()
            result = education_list_schema.dump({'educations': educations})
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new education"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('institution', type=str, required=True, help='Institution is required')
            parser.add_argument('degree', type=str, required=True, help='Degree is required')
            parser.add_argument('field_of_study', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('start_date', type=str)
            parser.add_argument('end_date', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            
            education = Education(**data)
            db.session.add(education)
            db.session.commit()
            
            result = education_schema.dump(education)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class EducationResource(Resource):
    """Resource for single education operations"""
    
    def get(self, id=None):
        """Get education by ID"""
        try:
            if id:
                education = Education.query.get_or_404(id)
            else:
                educations = Education.query.order_by(Education.end_date.desc()).all()
                result = education_list_schema.dump({'educations': educations})
                return make_response(jsonify(result), 200)
            
            result = education_schema.dump(education)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update education"""
        try:
            education = Education.query.get_or_404(id)
            
            parser = reqparse.RequestParser()
            parser.add_argument('institution', type=str)
            parser.add_argument('degree', type=str)
            parser.add_argument('field_of_study', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('start_date', type=str)
            parser.add_argument('end_date', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(education, key, value)
            
            db.session.commit()
            
            result = education_schema.dump(education)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete education"""
        try:
            education = Education.query.get_or_404(id)
            db.session.delete(education)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Education deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
