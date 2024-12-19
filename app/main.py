import logging
from flask import Flask, request, jsonify
import os
import requests

logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

app = Flask(__name__)


@app.route('/send_message', methods=['POST'])
def send_message():
    """
    API endpoint to send a message using Telegram.
    Expects a JSON payload with a 'message' field.
    """
    try:
        data = request.get_json()
        message = data.get('message')

        if not message:
            logging.warning("Message field is missing in the request payload.")
            return jsonify({"error": "Message field is required."}), 400

        telegram_token = os.environ.get("TELEGRAM_TOKEN")
        telegram_chat_id = os.environ.get("TELEGRAM_CHAT_ID")

        if not telegram_token or not telegram_chat_id:
            logging.error("Telegram credentials are not set in environment variables.")
            return jsonify({"error": "Telegram credentials are not set in environment variables."}), 500

        to_url = f"https://api.telegram.org/bot{telegram_token}/sendMessage?chat_id={telegram_chat_id}&text={message}"
        logging.info(f"Sending message to Telegram: {message}")
        response = requests.get(to_url)

        if response.status_code == 200:
            logging.info("Message sent successfully.")
            return jsonify({"success": "Message sent successfully."}), 200
        else:
            logging.error(f"Failed to send message. Response: {response.text}")
            return jsonify({"error": "Failed to send message.", "details": response.text}), response.status_code

    except Exception as e:
        logging.exception("An unexpected error occurred.")
        return jsonify({"error": "An unexpected error occurred.", "details": str(e)}), 500


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
