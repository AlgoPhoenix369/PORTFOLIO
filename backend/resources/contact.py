"""
Contact API Resource - Using Supabase
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from supabase_db import (
    get_all_messages, get_message_by_id, create_message,
    update_message, delete_message
)


class ContactResource(Resource):
    def get(self):
        """Get all contact messages (admin)"""
        try:
            messages = get_all_messages()
            return make_response(jsonify({'messages': messages}), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Submit a new contact message"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('name', type=str, required=True, help='Name is required')
            parser.add_argument('email', type=str, required=True, help='Email is required')
            parser.add_argument('subject', type=str)
            parser.add_argument('message', type=str, required=True, help='Message is required')
            
            data = parser.parse_args()
            message = create_message(data)
            
            if message:
                return make_response(jsonify({
                    'message': 'Contact message sent successfully',
                    'data': message
                }), 201)
            return make_response(jsonify({'error': 'Failed to send message'}), 500)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Mark message as read"""
        try:
            message = update_message(id, {'is_read': True})
            if message:
                return make_response(jsonify(message), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete a message"""
        try:
            if delete_message(id):
                return make_response(jsonify({'message': 'Deleted'}), 200)
            return make_response(jsonify({'error': 'Not found'}), 404)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
