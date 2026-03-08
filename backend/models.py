"""
Database Models for Portfolio API
"""

from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Profile(db.Model):
    """Profile model for personal information"""
    __tablename__ = 'profiles'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(20))
    summary = db.Column(db.Text)
    github_url = db.Column(db.String(200))
    linkedin_url = db.Column(db.String(200))
    portfolio_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'title': self.title,
            'location': self.location,
            'email': self.email,
            'phone': self.phone,
            'summary': self.summary,
            'github_url': self.github_url,
            'linkedin_url': self.linkedin_url,
            'portfolio_url': self.portfolio_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class Experience(db.Model):
    """Experience model for work history"""
    __tablename__ = 'experiences'
    
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    position = db.Column(db.String(200), nullable=False)
    location = db.Column(db.String(200))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    is_current = db.Column(db.Boolean, default=False)
    description = db.Column(db.Text)
    responsibilities = db.Column(db.JSON)  # Array of responsibilities
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'company': self.company,
            'position': self.position,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'is_current': self.is_current,
            'description': self.description,
            'responsibilities': self.responsibilities or [],
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class Education(db.Model):
    """Education model for academic background"""
    __tablename__ = 'educations'
    
    id = db.Column(db.Integer, primary_key=True)
    institution = db.Column(db.String(200), nullable=False)
    degree = db.Column(db.String(200), nullable=False)
    field_of_study = db.Column(db.String(200))
    location = db.Column(db.String(200))
    start_date = db.Column(db.String(20))
    end_date = db.Column(db.String(20))
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'institution': self.institution,
            'degree': self.degree,
            'field_of_study': self.field_of_study,
            'location': self.location,
            'start_date': self.start_date,
            'end_date': self.end_date,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class Skill(db.Model):
    """Skill model for technical skills"""
    __tablename__ = 'skills'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    proficiency_level = db.Column(db.Integer)  # 1-100
    years_of_experience = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'category': self.category,
            'proficiency_level': self.proficiency_level,
            'years_of_experience': self.years_of_experience,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class Project(db.Model):
    """Project model for portfolio projects"""
    __tablename__ = 'projects'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text)
    technologies = db.Column(db.JSON)  # Array of technologies
    duration = db.Column(db.String(50))
    role = db.Column(db.String(100))
    features = db.Column(db.JSON)  # Array of features
    project_url = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    image_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'technologies': self.technologies or [],
            'duration': self.duration,
            'role': self.role,
            'features': self.features or [],
            'project_url': self.project_url,
            'github_url': self.github_url,
            'image_url': self.image_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class Certification(db.Model):
    """Certification model for professional certifications"""
    __tablename__ = 'certifications'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
    issuer = db.Column(db.String(200), nullable=False)
    issue_date = db.Column(db.String(20))
    expiry_date = db.Column(db.String(20))
    credential_id = db.Column(db.String(100))
    credential_url = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'issuer': self.issuer,
            'issue_date': self.issue_date,
            'expiry_date': self.expiry_date,
            'credential_id': self.credential_id,
            'credential_url': self.credential_url,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class Award(db.Model):
    """Award model for achievements and recognition"""
    __tablename__ = 'awards'
    
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    organization = db.Column(db.String(200), nullable=False)
    year = db.Column(db.String(20))
    scope = db.Column(db.String(50))  # Local, National, International, Global
    description = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'title': self.title,
            'organization': self.organization,
            'year': self.year,
            'scope': self.scope,
            'description': self.description,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None,
        }


class ContactMessage(db.Model):
    """Contact message model for contact form submissions"""
    __tablename__ = 'contact_messages'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), nullable=False)
    subject = db.Column(db.String(200))
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'subject': self.subject,
            'message': self.message,
            'is_read': self.is_read,
            'created_at': self.created_at.isoformat() if self.created_at else None,
        }
