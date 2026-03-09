"""
Education API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_educations, get_education_by_id, create_education,
    update_education, delete_education
)


class EducationListResource(Resource):
    def get(self):
        try:
            educations = get_all_educations()
            return make_response(jsonify({'educations': educations}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('institution', type=str, required=True)
            parser.add_argument('degree', type=str, required=True)
            parser.add_argument('field_of_study', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('start_date', type=str)
            parser.add_argument('end_date', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            education = create_education(data)
            
            if education:
                return make_response(jsonify(education), 201)
            return make_response(jsonify({'error': 'Failed to create'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class EducationResource(Resource):
    def get(self, id=None):
        try:
            if id:
                education = get_education_by_id(id)
                if not education:
                    return make_response(jsonify({'error': 'Not found'}), 404)
                return make_response(jsonify(education), 200)
            else:
                return make_response(jsonify({'educations': get_all_educations()}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('institution', type=str)
            parser.add_argument('degree', type=str)
            parser.add_argument('field_of_study', type=str)
            parser.add_argument('location', type=str)
            parser.add_argument('start_date', type=str)
            parser.add_argument('end_date', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            update_data = {k: v for k, v in data.items() if v is not None}
            education = update_education(id, update_data)
            
            if education:
                return make_response(jsonify(education), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            if delete_education(id):
                return make_response(jsonify({'message': 'Deleted'}), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
