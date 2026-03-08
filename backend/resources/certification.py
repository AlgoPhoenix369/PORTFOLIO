"""
Certification API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Certification
from schemas import CertificationSchema, CertificationListSchema

certification_schema = CertificationSchema()
certification_list_schema = CertificationListSchema()


class CertificationListResource(Resource):
    """Resource for listing and creating certifications"""
    
    def get(self):
        """Get all certifications"""
        try:
            certifications = Certification.query.order_by(Certification.issue_date.desc()).all()
            result = certification_list_schema.dump({'certifications': certifications})
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new certification"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True, help='Certification name is required')
            parser.add_argument('issuer', type=str, required=True, help='Issuer is required')
            parser.add_argument('issue_date', type=str)
            parser.add_argument('expiry_date', type=str)
            parser.add_argument('credential_id', type=str)
            parser.add_argument('credential_url', type=str)
            
            data = parser.parse_args()
            
            certification = Certification(**data)
            db.session.add(certification)
            db.session.commit()
            
            result = certification_schema.dump(certification)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class CertificationResource(Resource):
    """Resource for single certification operations"""
    
    def get(self, id=None):
        """Get certification by ID"""
        try:
            if id:
                certification = Certification.query.get_or_404(id)
            else:
                certifications = Certification.query.order_by(Certification.issue_date.desc()).all()
                result = certification_list_schema.dump({'certifications': certifications})
                return make_response(jsonify(result), 200)
            
            result = certification_schema.dump(certification)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update certification"""
        try:
            certification = Certification.query.get_or_404(id)
            
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('issuer', type=str)
            parser.add_argument('issue_date', type=str)
            parser.add_argument('expiry_date', type=str)
            parser.add_argument('credential_id', type=str)
            parser.add_argument('credential_url', type=str)
            
            data = parser.parse_args()
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(certification, key, value)
            
            db.session.commit()
            
            result = certification_schema.dump(certification)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete certification"""
        try:
            certification = Certification.query.get_or_404(id)
            db.session.delete(certification)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Certification deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
