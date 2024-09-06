from flask import Flask, render_template, request
from twilio.rest import Client
from twilio.twiml.voice_response import VoiceResponse

app = Flask(__name__)

# Your Twilio credentials
ACCOUNT_SID = ''  # Replace with your Twilio Account SID
AUTH_TOKEN = ''      # Replace with your Twilio Auth Token
TWILIO_NUMBER = ''  # Replace with your Twilio number you can see this number in your twilio account

client = Client(ACCOUNT_SID, AUTH_TOKEN)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/call', methods=['POST'])
def call():
# The number to call make sure you have registered/verified this number on your Twilio Account also make sure donot use anyspaces and
#  insert country code before entering number for example +923332151715 etc   
    to_number = ''  
    response = VoiceResponse()
    response.say("Hello World I am Hamza Tahir")
    
    # Make the call
    call = client.calls.create(
        to=to_number,
        from_=TWILIO_NUMBER,
        twiml=str(response)
    )
    
    return f"Call initiated to {to_number}. Call SID: {call.sid}"

if __name__ == "__main__":
    app.run(debug=True)