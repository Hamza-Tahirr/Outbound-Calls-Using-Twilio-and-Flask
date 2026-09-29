import os

from dotenv import load_dotenv
from flask import Flask, render_template
from twilio.base.exceptions import TwilioRestException
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

load_dotenv()

ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_NUMBER = os.getenv("TWILIO_PHONE_NUMBER")
# Use E.164 format (country code, no spaces). On a trial account the
# number also has to be verified in the Twilio console.
TO_NUMBER = os.getenv("CALL_TO_NUMBER")
MESSAGE = os.getenv("CALL_MESSAGE") or "Hello World, I am Hamza Tahir."

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/call", methods=["POST"])
def call():
    if not all([ACCOUNT_SID, AUTH_TOKEN, TWILIO_NUMBER, TO_NUMBER]):
        return "Twilio settings are missing. Check your .env file.", 500

    response = VoiceResponse()
    response.say(MESSAGE)

    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    try:
        outbound_call = client.calls.create(
            to=TO_NUMBER,
            from_=TWILIO_NUMBER,
            twiml=str(response),
        )
    except TwilioRestException as e:
        return f"Call failed: {e.msg}", 502

    return f"Call initiated to {TO_NUMBER}. Call SID: {outbound_call.sid}"


if __name__ == "__main__":
    app.run(debug=True)
