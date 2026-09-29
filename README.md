# Outbound Calls with Twilio and Flask

A small Flask web app that places an outbound voice call through the Twilio API. When you click the button on the page, the app calls a preset phone number and reads out a text-to-speech message.

## Features

- Single page with a "Call ME" button
- `POST /call` creates a call with the Twilio REST API and passes the message as inline TwiML (`<Say>`)
- Twilio credentials, caller number, target number and message are read from a `.env` file
- The result (call SID or an error message) is shown in a browser alert

## Tech Stack

- Python
- Flask
- Twilio Python SDK
- python-dotenv
- HTML and plain JavaScript (`fetch`)

## Project Structure

```
.
├── app.py              # Flask routes and Twilio call logic
├── templates/
│   └── index.html      # Page with the call button
├── requirements.txt
└── .env.example        # Environment variables template
```

## Setup

You need Python 3.8 or newer and a Twilio account with a voice-capable phone number.

1. Clone the repository and create a virtual environment:

   ```bash
   git clone https://github.com/Hamza-Tahirr/Outbound-Calls-Using-Twilio-and-Flask.git
   cd Outbound-Calls-Using-Twilio-and-Flask
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

2. Install the dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Copy `.env.example` to `.env` and fill in your values:

   | Variable | Description |
   | --- | --- |
   | `TWILIO_ACCOUNT_SID` | Account SID from the Twilio console |
   | `TWILIO_AUTH_TOKEN` | Auth token from the Twilio console |
   | `TWILIO_PHONE_NUMBER` | Your Twilio number, used as the caller ID |
   | `CALL_TO_NUMBER` | Number to call |
   | `CALL_MESSAGE` | Message read out on the call (optional) |

   Phone numbers must be in E.164 format, with the country code and no spaces (for example `+15551234567`). On a Twilio trial account you can only call numbers you have verified in the console.

## Running

```bash
python app.py
```

Open http://127.0.0.1:5000/ and click "Call ME" to start the call.

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
