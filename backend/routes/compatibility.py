from flask import Blueprint, request, jsonify

compatibility_bp = Blueprint('compatibility', __name__)

@compatibility_bp.route('/', methods=['POST'])
def compatibility():
    data = request.get_json(silent=True) or {}
    # Placeholder: integrate compatibility_agent
    return jsonify({"status": "ok", "input": data})
