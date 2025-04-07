import os
from twilio.rest import Client

def call_with_twilio(to_phone, text):
    from twilio.rest import Client
    import os

    client = Client(os.environ["TWILIO_SID"], os.environ["TWILIO_TOKEN"])

    call = client.calls.create(
        to=to_phone,
        from_=os.environ["TWILIO_PHONE"],
        twiml=f"""
        <Response>
            <Say>{text}</Say>
        </Response>
        """
    )

    print("📞 呼叫已发出！Call SID:", call.sid)
