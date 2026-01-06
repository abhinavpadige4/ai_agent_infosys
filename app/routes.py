from flask import Blueprint, request, jsonify
from app.agents import agent

api = Blueprint("api", __name__)

@api.route("/chat", methods=["POST"])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    result = agent.invoke({
        "input": message,
        "output": ""
    })

    return jsonify({
        "response": result["output"]
    })
