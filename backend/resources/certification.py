"""
Certifications API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_certifications, get_certification_by_id, create_certification,
    update_certification, delete_certification
)


class CertificationListResource(Resource):
    def get(self):
        try:
            certifications = get_all_certifications()
            return make_response(jsonify({'certifications': certifications}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True)
            parser.add_argument('issuer', type=str, required=True)
            parser.add_argument('issue_date', type=str)
            parser.add_argument('expiry_date', type=str)
            parser.add_argument('credential_id', type=str)
            parser.add_argument('credential_url', type=str)
            
            data = parser.parse_args()
            cert = create_certification(data)
            
            if cert:
                return make_response(jsonify(cert), 201)
            return make_response(jsonify({'error': 'Failed to create'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class CertificationResource(Resource):
    def get(self, id=None):
        try:
            if id:
                cert = get_certification_by_id(id)
                if not cert:
                    return make_response(jsonify({'error': 'Not found'}), 404)
                return make_response(jsonify(cert), 200)
            else:
                return make_response(jsonify({'certifications': get_all_certifications()}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str)
            parser.add_argument('issuer', type=str)
            parser.add_argument('issue_date', type=str)
            parser.add_argument('expiry_date', type=str)
            parser.add_argument('credential_id', type=str)
            parser.add_argument('credential_url', type=str)
            
            data = parser.parse_args()
            update_data = {k: v for k, v in data.items() if v is not None}
            cert = update_certification(id, update_data)
            
            if cert:
                return make_response(jsonify(cert), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            if delete_certification(id):
                return make_response(jsonify({'message': 'Deleted'}), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
