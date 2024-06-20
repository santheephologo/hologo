from flask import Blueprint, jsonify, request, current_app
from main.services.openai_service import OpenAIService

convo_blueprint = Blueprint('convo', __name__)

openai_service = OpenAIService()

@convo_blueprint.route('/')
def index():
    return 'Working'

@convo_blueprint.route('/convo', methods=['POST'])
def convo():
    if request.method == "POST":
        message = request.json.get('message')
        if message:
            
            openai_tkn = current_app.config['OPENAI_API_TOKEN']
            assistant_id = current_app.config['ASSISTANT_ID']

            response = openai_service.connectAi(openai_tkn, message, assistant_id)
            if response:
                return jsonify(response), 200
        return "No message found", 400
