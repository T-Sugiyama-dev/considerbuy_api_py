from flask import Blueprint, jsonify, request, make_response
from flask_cors import CORS
import os
from dotenv import load_dotenv
from app.service.calc_service import CalcService

calc_controller = Blueprint('calc_controller', __name__)
load_dotenv()
client_origin = os.getenv("CLIENT_ORIGIN")
CORS(calc_controller)
calc_service = CalcService()

@calc_controller.route("/calcValue", methods=["POST", "OPTIONS"])
def api_create_order():
    if request.method == "OPTIONS": # CORS preflight
        return _build_cors_preflight_response()
    elif request.method == "POST": # The actual request
        data = request.get_json()
        calc_service = CalcService()
        result = calc_service.calculate(data)
        return _corsify_actual_response(jsonify(result))
    else:
        raise RuntimeError("Weird - don't know how to handle method {}".format(request.method))

def _build_cors_preflight_response():
    response = make_response()
    response.headers.add("Access-Control-Allow-Origin", client_origin)
    response.headers.add('Access-Control-Allow-Headers', "Content-Type")
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    response.headers.add('Access-Control-Allow-Methods', 'POST, OPTIONS')
    return response

def _corsify_actual_response(response):
    response.headers.add("Access-Control-Allow-Origin", client_origin)
    response.headers.add('Access-Control-Allow-Headers', "Content-Type")
    response.headers['Content-Type'] = 'application/json'
    response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response
