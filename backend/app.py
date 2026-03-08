"""
Portfolio Backend API
Flask RESTful API with Supabase/PostgreSQL backend
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import resources
from resources.profile import ProfileResource, ProfileListResource
from resources.experience import ExperienceResource, ExperienceListResource
from resources.education import EducationResource, EducationListResource
from resources.skill import SkillResource, SkillListResource
from resources.project import ProjectResource, ProjectListResource
from resources.certification import CertificationResource, CertificationListResource
from resources.award import AwardResource, AwardListResource
from resources.contact import ContactResource

# Import database
from models import db


def create_app():
    """Application factory for creating Flask app"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv(
        'DATABASE_URL', 
        'postgresql://postgres:postgres@localhost:5432/portfolio_db'
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Supabase configuration
    app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
    app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')
    
    # CORS configuration
    cors_origins = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://localhost:5173').split(',')
    CORS(app, origins=cors_origins)
    
    # Initialize extensions
    db.init_app(app)
    
    # Initialize Flask-RESTful
    api = Api(app)
    
    # Register routes
    register_routes(api)
    
    # Register error handlers
    register_error_handlers(app)
    
    # Create tables
    with app.app_context():
        db.create_all()
    
    return app


def register_routes(api):
    """Register API resources"""
    # Profile
    api.add_resource(ProfileListResource, '/api/profiles')
    api.add_resource(ProfileResource, '/api/profile', '/api/profile/<int:id>')
    
    # Experience
    api.add_resource(ExperienceListResource, '/api/experiences')
    api.add_resource(ExperienceResource, '/api/experience', '/api/experience/<int:id>')
    
    # Education
    api.add_resource(EducationListResource, '/api/educations')
    api.add_resource(EducationResource, '/api/education', '/api/education/<int:id>')
    
    # Skills
    api.add_resource(SkillListResource, '/api/skills')
    api.add_resource(SkillResource, '/api/skill', '/api/skill/<int:id>')
    
    # Projects
    api.add_resource(ProjectListResource, '/api/projects')
    api.add_resource(ProjectResource, '/api/project', '/api/project/<int:id>')
    
    # Certifications
    api.add_resource(CertificationListResource, '/api/certifications')
    api.add_resource(CertificationResource, '/api/certification', '/api/certification/<int:id>')
    
    # Awards
    api.add_resource(AwardListResource, '/api/awards')
    api.add_resource(AwardResource, '/api/award', '/api/award/<int:id>')
    
    # Contact
    api.add_resource(ContactResource, '/api/contact')


def register_error_handlers(app):
    """Register error handlers"""
    
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({'error': 'Resource not found'}), 404
    
    @app.errorhandler(500)
    def internal_error(error):
        return jsonify({'error': 'Internal server error'}), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request'}), 400
    
    @app.route('/api/health')
    def health_check():
        return jsonify({'status': 'healthy', 'message': 'Portfolio API is running'}), 200


# Create app instance
app = create_app()


if __name__ == '__main__':
    app.run(debug=True, port=5000)
