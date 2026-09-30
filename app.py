from flask import (
    Flask,
    render_template,
    request,
    jsonify,
    session
)

import uuid

from database import (
    initialize_database,
    save_message,
    get_messages,
    create_ticket
)

from chatbot import generate_response


app = Flask(__name__)

app.secret_key = "change-this-secret-key"


initialize_database()


@app.route("/")
def home():

    if "session_id" not in session:

        session["session_id"] = str(uuid.uuid4())

    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():

    data = request.get_json()

    user_message = data.get(
        "message",
        ""
    ).strip()

    if not user_message:

        return jsonify({
            "error": "Message cannot be empty."
        }), 400

    session_id = session["session_id"]

    history = get_messages(session_id)

    conversation_history = []

    for message in history:

        conversation_history.append({
            "sender": message["sender"],
            "message": message["message"]
        })

    save_message(
        session_id,
        "user",
        user_message
    )

    try:

        response = generate_response(
            user_message,
            conversation_history
        )

        save_message(
            session_id,
            "bot",
            response
        )

        return jsonify({
            "reply": response
        })

    except Exception as error:

        print(error)

        return jsonify({
            "error": "Unable to generate response."
        }), 500


@app.route("/create-ticket", methods=["POST"])
def ticket():

    data = request.get_json()

    issue = data.get(
        "issue",
        "Customer requested human support."
    )

    session_id = session["session_id"]

    ticket_id = create_ticket(
        session_id,
        issue
    )

    return jsonify({
        "ticket_id": ticket_id,
        "message":
        f"Your support ticket #{ticket_id} "
        "has been created successfully."
    })


if __name__ == "__main__":

    app.run(
        debug=True
    )