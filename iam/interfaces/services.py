from flask import Blueprint, request, jsonify

from iam.application.services import AuthApplicationService

iam_api = Blueprint('iam_api', __name__)

auth_service = AuthApplicationService()

def authenticate_request():
    """
    Authenticate a request using device_id and API key.

    Checks for 'device_id' in JSON body and 'X-API-KEY' in headers.
    :returns: None if authenticated, else a Flask response with 401 status.
    """
    device_id = request.json.get('device_id') if request.json else None
    api_key = request.headers.get('X-API-KEY')
    if not device_id or not api_key:
        return jsonify({'error': 'Mising device_id or API key'}), 401
    if not auth_service.authenticate(device_id, api_key):
        return jsonify({'error': 'Invalid device_id or API key'}), 401
    return None
