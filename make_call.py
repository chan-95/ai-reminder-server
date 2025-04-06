import os
from twilio.rest import Client

def call_with_twilio(to_phone, audio_url):
    account_sid = os.environ["TWILIO_SID"]
    auth_token = os.environ["TWILIO_TOKEN"]
    from_phone = os.environ["TWILIO_PHONE"]

    client = Client(account_sid, auth_token)

    call = client.calls.create(
        to=to_phone,
        from_=from_phone,
        twiml=f"""
        <Response>
            <Play>{audio_url}</Play>
        </Response>
        """
    )
    print("📞 呼叫已发出！SID:", call.sid)
