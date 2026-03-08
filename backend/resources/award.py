"""
Award API Resource
"""

from flask_restful import Resource, reqparse
from flask import jsonify, make_response
from models import db, Award
from schemas import AwardSchema, AwardListSchema

award_schema = AwardSchema()
award_list_schema = AwardListSchema()


class AwardListResource(Resource):
    """Resource for listing and creating awards"""
    
    def get(self):
        """Get all awards"""
        try:
            awards = Award.query.order_by(Award.year.desc()).all()
            result = award_list_schema.dump({'awards': awards})
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def post(self):
        """Create a new award"""
        try:
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str, required=True, help='Title is required')
            parser.add_argument('organization', type=str, required=True, help='Organization is required')
            parser.add_argument('year', type=str)
            parser.add_argument('scope', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            
            award = Award(**data)
            db.session.add(award)
            db.session.commit()
            
            result = award_schema.dump(award)
            return make_response(jsonify(result), 201)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)


class AwardResource(Resource):
    """Resource for single award operations"""
    
    def get(self, id=None):
        """Get award by ID"""
        try:
            if id:
                award = Award.query.get_or_404(id)
            else:
                awards = Award.query.order_by(Award.year.desc()).all()
                result = award_list_schema.dump({'awards': awards})
                return make_response(jsonify(result), 200)
            
            result = award_schema.dump(award)
            return make_response(jsonify(result), 200)
        except Exception as e:
            return make_response(jsonify({'error': str(e)}), 500)
    
    def put(self, id):
        """Update award"""
        try:
            award = Award.query.get_or_404(id)
            
            parser = reqparse.RequestParser()
            parser.add_argument('title', type=str)
            parser.add_argument('organization', type=str)
            parser.add_argument('year', type=str)
            parser.add_argument('scope', type=str)
            parser.add_argument('description', type=str)
            
            data = parser.parse_args()
            
            # Update fields
            for key, value in data.items():
                if value is not None:
                    setattr(award, key, value)
            
            db.session.commit()
            
            result = award_schema.dump(award)
            return make_response(jsonify(result), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
    
    def delete(self, id):
        """Delete award"""
        try:
            award = Award.query.get_or_404(id)
            db.session.delete(award)
            db.session.commit()
            
            return make_response(jsonify({'message': 'Award deleted successfully'}), 200)
        except Exception as e:
            db.session.rollback()
            return make_response(jsonify({'error': str(e)}), 500)
