from flask import Flask, request, jsonify
from generate_voice import generate_voice
from make_call import call_with_twilio

app = Flask(__name__)

@app.route("/remind", methods=["POST"])
def remind():
    data = request.json
    text = data.get("text")
    phone = data.get("phone")

    if not text or not phone:
        return jsonify({"error": "Missing text or phone"}), 400

    # 生成语音文件
    generate_voice(text, "public/output.mp3")

    # 拨打电话并播放语音
    call_with_twilio(phone, "https://your-vercel-url/output.mp3")

    return jsonify({"status": "Reminder sent!"})
