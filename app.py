from flask import Flask, request

app = Flask(__name__)


@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the payload sent to the webhook
    payload = request.json

    # Print the payload
    print("Received Payload:", payload)

    # You can process the payload further here

    return {"message": "Received the payload successfully!"}, 200


@app.route("/test", methods=["GET"])
def test_route():
    return {"message": "Pinged successfully!"}, 200

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=int(5000))
