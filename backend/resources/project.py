"""
Project API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Project
from schemas import ProjectSchema, ProjectListSchema

project_schema = ProjectSchema()
project_list_schema = ProjectListSchema()


class ProjectListResource(Resource):
    """Resource for listing and creating projects"""
    
    def get(self):
        """Get all projects"""
        try:
            projects = Project.query.order_by(Project.created_at.desc()).all()
            result = project_list_schema.dump({'projects': projects})
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new project"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help='Title is required')
            parser.add_argument('description', type=str)
            parser.add_argument('technologies', type=list, location='json', default=[])
            parser.add_argument('duration', type=str)
            parser.add_argument('role', type=str)
            parser.add_argument('features', type=list, location='json', default=[])
            parser.add_argument('project_url', type=str)
            parser.add_argument('github_url', type=str)
            parser.add_argument('image_url', type=str)
            
            data = parser.parse_args()
            
            project = Project(**data)
            db.session.add(project)
            db.session.commit()
            
            result = project_schema.dump(project)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class ProjectResource(Resource):
    """Resource for single project operations"""
    
    def get(self, id=None):
        """Get project by ID"""
        try:
            if id:
                project = Project.query.get_or_404(id)
            else:
                projects = Project.query.order_by(Project.created_at.desc()).all()
                result = project_list_schema.dump({'projects': projects})
                return make_response(jsonify(result), 200)
            
            result = project_schema.dump(project)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update project"""
        try:
            project = Project.query.get_or_404(id)
            
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
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(project, key, value)
            
            db.session.commit()
            
            result = project_schema.dump(project)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete project"""
        try:
            project = Project.query.get_or_404(id)
            db.session.delete(project)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Project deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
