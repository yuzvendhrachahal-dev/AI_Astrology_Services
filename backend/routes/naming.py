from flask import Blueprint, request, jsonify

naming_bp = Blueprint('naming', __name__)

@naming_bp.route('/', methods=['POST'])
def naming():
    data = request.get_json(silent=True) or {}
    # Placeholder: integrate naming_agent
    return jsonify({"status": "ok", "input": data})
