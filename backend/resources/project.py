"""
Projects API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_projects, get_project_by_id, create_project,
    update_project, delete_project
)


class ProjectListResource(Resource):
    def get(self):
        try:
            projects = get_all_projects()
            return make_response(jsonify({'projects': projects}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True)
            parser.add_argument('description', type=str)
            parser.add_argument('technologies', type=list, location='json', default=[])
            parser.add_argument('duration', type=str)
            parser.add_argument('role', type=str)
            parser.add_argument('features', type=list, location='json', default=[])
            parser.add_argument('project_url', type=str)
            parser.add_argument('github_url', type=str)
            parser.add_argument('image_url', type=str)
            
            data = parser.parse_args()
            project = create_project(data)
            
            if project:
                return make_response(jsonify(project), 201)
            return make_response(jsonify({'error': 'Failed to create'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class ProjectResource(Resource):
    def get(self, id=None):
        try:
            if id:
                project = get_project_by_id(id)
                if not project:
                    return make_response(jsonify({'error': 'Not found'}), 404)
                return make_response(jsonify(project), 200)
            else:
                return make_response(jsonify({'projects': get_all_projects()}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('description', type=str)
            parser.add_argument('technologies', type=list, location='json')
            parser.add_argument('duration', type=str)
            parser.add_argument('role', type=str)
            parser.add_argument('features', type=list, location='json')
            parser.add_argument('project_url', type=str)
            parser.add_argument('github_url', type=str)
            parser.add_argument('image_url', type=str)
            
            data = parser.parse_args()
            update_data = {k: v for k, v in data.items() if v is not None}
            project = update_project(id, update_data)
            
            if project:
                return make_response(jsonify(project), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            if delete_project(id):
                return make_response(jsonify({'message': 'Deleted'}), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
