from flask import Blueprint, request, jsonify

testi_bp = Blueprint("testi", __name__, url_prefix="/testi")

@testi_bp.route("/urltest")
def urlTest():
    name = request.args.get('name')
    type = request.args.get('type', 'all')
    return f"Testi onnistui, löytyi {name} ja tyyppi: {type}"

@testi_bp.route("/posttest/<int:id>", methods=['POST'])
def postTest(id):
    data = request.get_json()
    name = data.get('name')
    return f"Testi onnistui bodystä löytyi {name} ja urlista id: {id}"