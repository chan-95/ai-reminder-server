from twilio.rest import Client
import os

def call_with_twilio(to_phone, reminder_text):
    client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_TOKEN"])
    from_phone = os.environ["TWILIO_PHONE"]

    call = client.calls.create(
        to=to_phone,
        from_=from_phone,
        twiml=f"""
        <Response>
            <Say>{reminder_text}</Say>
        </Response>
        """
    )

    print("✅ 呼叫已发出！Call SID:", call.sid)
