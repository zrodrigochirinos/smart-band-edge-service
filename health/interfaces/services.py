from flask import Blueprint, request, jsonify

from health.domain.services import HealthRecordService
from iam.interfaces.services import authenticate_request

health_api = Blueprint('health_api', __name__)

health_record_service = HealthRecordService()


@health_api.route('/api/v1/health-monitoring/data-records', methods=['POST'])
def create_health_record():
    """
    Endpoint to create a new health data record.
    Expects JSON body with 'device_id', 'bpm', and optionally 'created_at'.
    Requires an X-API-Key header with the API key.

    :return: JSON response with the created record with its ID.
    201 Created on success, 400 Bad Request on failure.
    """
    auth_result = authenticate_request()
    if auth_result:
        return auth_result
    data = request.json
    try:
        device_id = data['device_id']
        bpm = data['bpm']
        created_at = data['created_at']
        record = health_record_service.create_record(device_id, bpm, created_at, request.headers.get("X-API-Key"))
        return jsonify({
            "id": record.id,
            "device_id": record.device_id,
            "bpm": record.bpm,
            "created_at": record.created_at.isoformat() + "Z"
        }), 201
    except KeyError:
        return jsonify({"error": "Missing device_id or bpm"}), 400
    except ValueError as e:
        return jsonify({"error": str(e)}), 400

