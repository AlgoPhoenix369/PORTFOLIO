"""
Marshmallow Schemas for Data Validation and Serialization
"""

from marshmallow import Schema, fields, validate, validates, validates_schema, ValidationError
from datetime import datetime


class ProfileSchema(Schema):
    """Schema for Profile model"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    location = fields.Str(validate=validate.Length(max=200))
    email = fields.Email(required=True)
    phone = fields.Str(validate=validate.Length(max=20))
    summary = fields.Str()
    github_url = fields.Url(validate=validate.Length(max=200))
    linkedin_url = fields.Url(validate=validate.Length(max=200))
    portfolio_url = fields.Url(validate=validate.Length(max=200))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ExperienceSchema(Schema):
    """Schema for Experience model"""
    id = fields.Int(dump_only=True)
    company = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    position = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    location = fields.Str(validate=validate.Length(max=200))
    start_date = fields.Str(validate=validate.Length(max=20))
    end_date = fields.Str(validate=validate.Length(max=20))
    is_current = fields.Bool()
    description = fields.Str()
    responsibilities = fields.List(fields.Str())
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)
    
    @validates_schema
    def validate_dates(self, data, **kwargs):
        if 'is_current' not in data or not data['is_current']:
            if not data.get('end_date'):
                raise ValidationError('end_date is required if is_current is False', 'end_date')


class EducationSchema(Schema):
    """Schema for Education model"""
    id = fields.Int(dump_only=True)
    institution = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    degree = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    field_of_study = fields.Str(validate=validate.Length(max=200))
    location = fields.Str(validate=validate.Length(max=200))
    start_date = fields.Str(validate=validate.Length(max=20))
    end_date = fields.Str(validate=validate.Length(max=20))
    description = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class SkillSchema(Schema):
    """Schema for Skill model"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    category = fields.Str(required=True, validate=validate.Length(min=1, max=50))
    proficiency_level = fields.Int(validate=validate.Range(min=1, max=100))
    years_of_experience = fields.Int(validate=validate.Range(min=0))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ProjectSchema(Schema):
    """Schema for Project model"""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    description = fields.Str()
    technologies = fields.List(fields.Str())
    duration = fields.Str(validate=validate.Length(max=50))
    role = fields.Str(validate=validate.Length(max=100))
    features = fields.List(fields.Str())
    project_url = fields.Url(validate=validate.Length(max=200))
    github_url = fields.Url(validate=validate.Length(max=200))
    image_url = fields.Url(validate=validate.Length(max=200))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class CertificationSchema(Schema):
    """Schema for Certification model"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    issuer = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    issue_date = fields.Str(validate=validate.Length(max=20))
    expiry_date = fields.Str(validate=validate.Length(max=20))
    credential_id = fields.Str(validate=validate.Length(max=100))
    credential_url = fields.Url(validate=validate.Length(max=200))
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class AwardSchema(Schema):
    """Schema for Award model"""
    id = fields.Int(dump_only=True)
    title = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    organization = fields.Str(required=True, validate=validate.Length(min=1, max=200))
    year = fields.Str(validate=validate.Length(max=20))
    scope = fields.Str(validate=validate.Length(max=50))
    description = fields.Str()
    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)


class ContactMessageSchema(Schema):
    """Schema for Contact Message model"""
    id = fields.Int(dump_only=True)
    name = fields.Str(required=True, validate=validate.Length(min=1, max=100))
    email = fields.Email(required=True)
    subject = fields.Str(validate=validate.Length(max=200))
    message = fields.Str(required=True, validate=validate.Length(min=1))
    is_read = fields.Bool(dump_only=True)
    created_at = fields.DateTime(dump_only=True)


# Schemas for lists
class ProfileListSchema(Schema):
    profiles = fields.Nested(ProfileSchema, many=True)


class ExperienceListSchema(Schema):
    experiences = fields.Nested(ExperienceSchema, many=True)


class EducationListSchema(Schema):
    educations = fields.Nested(EducationSchema, many=True)


class SkillListSchema(Schema):
    skills = fields.Nested(SkillSchema, many=True)


class ProjectListSchema(Schema):
    projects = fields.Nested(ProjectSchema, many=True)


class CertificationListSchema(Schema):
    certifications = fields.Nested(CertificationSchema, many=True)


class AwardListSchema(Schema):
    awards = fields.Nested(AwardSchema, many=True)
