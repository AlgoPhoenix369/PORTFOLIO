"""
Contact API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, ContactMessage
from schemas import ContactMessageSchema

contact_schema = ContactMessageSchema()


class ContactResource(Resource):
    """Resource for contact form submissions"""
    
    def get(self):
        """Get all contact messages (admin only)"""
        try:
            messages = ContactMessage.query.order_by(ContactMessage.created_at.desc()).all()
            result = {'messages': [contact_schema.dump(msg) for msg in messages]}
            return make_response(jsonify(result), 200)
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
            
            contact_message = ContactMessage(**data)
            db.session.add(contact_message)
            db.session.commit()
            
            result = contact_schema.dump(contact_message)
            return make_response(jsonify({
                'message': 'Contact message sent successfully',
                'data': result
            }), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Mark a message as read"""
        try:
            message = ContactMessage.query.get_or_404(id)
            message.is_read = True
            db.session.commit()
            
            result = contact_schema.dump(message)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete a contact message"""
        try:
            message = ContactMessage.query.get_or_404(id)
            db.session.delete(message)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Message deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
