
from flask import Flask, request, jsonify
from caesar import encrypt, decrypt, brute_force, auto_crack
app = Flask(__name__)


@app.route("/api/encrypt", methods=["POST"])
def encrypt_api():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Expected a JSON object"}), 400

    message = data.get("message")
    key = data.get("key")

    if not isinstance(message, str):
        return jsonify({"error": "Message must be text"}), 400

    if not isinstance(key, int) or isinstance(key, bool):
        return jsonify({"error": "Key must be an integer"}), 400

    if len(message) > 10000:
        return jsonify({"error": "Message is too long"}), 400

    result = encrypt(message, key)

    return jsonify({
        "original": message,
        "encrypted": result,
        "key": key
    })


@app.route("/api/decrypt", methods=["POST"])
def decrypt_api():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    message = data.get("message")
    key = data.get("key")

    if not isinstance(message, str) or len(message) > 10000:
        return jsonify({"error": "Invalid message"}), 400

    if type(key) is not int:
        return jsonify({"error": "Key must be an integer"}), 400

    return jsonify({
        "decrypted": decrypt(message, key),
        "key": key
    })


@app.route("/api/brute-force", methods=["POST"])
def brute_force_api():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    message = data.get("message")

    if not isinstance(message, str) or len(message) > 10000:
        return jsonify({"error": "Invalid message"}), 400

    return jsonify({
        "results": brute_force(message)
    })


@app.route("/api/auto-crack", methods=["POST"])
def auto_crack_api():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({"error": "Invalid JSON"}), 400

    message = data.get("message")

    if not isinstance(message, str) or len(message) > 10000:
        return jsonify({"error": "Invalid message"}), 400

    if not any(c.isascii() and c.isalpha() for c in message):
        return jsonify({"error": "Message must contain English letters"}), 400

    return jsonify(auto_crack(message))


if __name__ == "__main__":
    app.run(debug=True)
