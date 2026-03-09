"""
Awards API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_awards, get_award_by_id, create_award,
    update_award, delete_award
)


class AwardListResource(Resource):
    def get(self):
        try:
            awards = get_all_awards()
            return make_response(jsonify({'awards': awards}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True)
            parser.add_argument('organization', type=str, required=True)
            parser.add_argument('year', type=str)
            parser.add_argument('scope', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            award = create_award(data)
            
            if award:
                return make_response(jsonify(award), 201)
            return make_response(jsonify({'error': 'Failed to create'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)


class AwardResource(Resource):
    def get(self, id=None):
        try:
            if id:
                award = get_award_by_id(id)
                if not award:
                    return make_response(jsonify({'error': 'Not found'}), 404)
                return make_response(jsonify(award), 200)
            else:
                return make_response(jsonify({'awards': get_all_awards()}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('organization', type=str)
            parser.add_argument('year', type=str)
            parser.add_argument('scope', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            update_data = {k: v for k, v in data.items() if v is not None}
            award = update_award(id, update_data)
            
            if award:
                return make_response(jsonify(award), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        try:
            if delete_award(id):
                return make_response(jsonify({'message': 'Deleted'}), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
