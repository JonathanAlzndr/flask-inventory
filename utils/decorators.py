from functools import wraps
from flask_jwt_extended import get_jwt_identity
from flask import jsonify

def role_required(role_name):
    def wrapper(fn):
        @wraps(fn)
        def decorator(*args, **kwargs):
            identity = get_jwt_identity()
            if not identity or identity.get("role") != role_name:
                return jsonify({"error": "Unauthorized"}), 403
            return fn(*args, **kwargs)
        return decorator
    return wrapper
