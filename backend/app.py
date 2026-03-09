"""
Portfolio Backend API
Flask RESTful API with Supabase backend
Production-ready for Railway/Render deployment
"""

from flask import Flask, jsonify
from flask_cors import CORS
from flask_restful import Api
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Import all resources
from resources.profile import ProfileResource, ProfileListResource
from resources.experience import ExperienceResource, ExperienceListResource
from resources.education import EducationResource, EducationListResource
from resources.skill import SkillResource, SkillListResource
from resources.project import ProjectResource, ProjectListResource
from resources.certification import CertificationResource, CertificationListResource
from resources.award import AwardResource, AwardListResource
from resources.contact import ContactResource


def create_app():
    """Application factory for creating Flask app"""
    app = Flask(__name__)
    
    # Configuration
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'dev-secret-key')
    
    # Supabase configuration
    app.config['SUPABASE_URL'] = os.getenv('SUPABASE_URL')
    app.config['SUPABASE_KEY'] = os.getenv('SUPABASE_KEY')
    
    # Validate Supabase configuration
    if not app.config['SUPABASE_URL'] or not app.config['SUPABASE_KEY']:
        app.logger.warning("Supabase credentials not configured. Set SUPABASE_URL and SUPABASE_KEY")
    
    # CORS configuration
    cors_origins = os.getenv('CORS_ORIGINS', 'http://localhost:3000,http://localhost:5173').split(',')
    CORS(app, origins=cors_origins)
    
    # Initialize Flask-RESTful
    api = Api(app)
    
    # Register all routes
    register_routes(api)
    
    # Register error handlers
    register_error_handlers(app)
    
    return app


def register_routes(api):
    """Register all API resources"""
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
        app.logger.error(f'Internal error: {error}')
        return jsonify({'error': 'Internal server error'}), 500
    
    @app.errorhandler(400)
    def bad_request(error):
        return jsonify({'error': 'Bad request'}), 400
    
    @app.route('/api/health')
    def health_check():
        """Health check endpoint"""
        supabase_configured = bool(os.getenv('SUPABASE_URL') and os.getenv('SUPABASE_KEY'))
        return jsonify({
            'status': 'healthy',
            'message': 'Portfolio API is running',
            'database': 'Supabase',
            'supabase_configured': supabase_configured,
            'version': '1.0.0'
        }), 200
    
    @app.route('/')
    def index():
        """API documentation endpoint"""
        return jsonify({
            'name': 'Portfolio API',
            'version': '1.0.0',
            'endpoints': {
                'health': '/api/health',
                'profiles': '/api/profiles',
                'experience': '/api/experiences',
                'education': '/api/educations',
                'skills': '/api/skills',
                'projects': '/api/projects',
                'certifications': '/api/certifications',
                'awards': '/api/awards',
                'contact': '/api/contact'
            }
        }), 200


# Create app instance
app = create_app()


if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    debug = os.getenv('FLASK_ENV') == 'development'
    app.run(debug=debug, host='0.0.0.0', port=port)
