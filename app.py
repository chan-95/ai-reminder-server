from flask import Flask, request, jsonify
from make_call import call_with_twilio  # 直接用这个

app = Flask(__name__)

@app.route("/remind", methods=["POST"])
def remind():
    data = request.get_json()
    text = data.get("text")
    phone = data.get("phone")

    if not text or not phone:
        return jsonify({"error": "Missing text or phone"}), 400

    call_with_twilio(phone, text)  # ✅ 直接用 <Say> 播语音

    return jsonify({"status": "Reminder sent!"})
