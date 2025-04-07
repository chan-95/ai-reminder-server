from flask import Flask, request, jsonify
from generate_voice import generate_voice
from make_call import call_with_twilio

app = Flask(__name__)

@app.route("/remind", methods=["POST"])
def remind():
    data = request.get_json()
    text = data.get("text")
    phone = data.get("phone")

    if not text or not phone:
        return jsonify({"error": "Missing text or phone"}), 400

    # generate_voice(text, "public/output.mp3")  ← 注释掉
    call_with_twilio(phone, text)  # 改成直接播报文字

    return jsonify({"status": "Reminder sent!"})

