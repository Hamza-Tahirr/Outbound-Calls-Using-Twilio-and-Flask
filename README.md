# Outbound-Calls-Using-Twilio-and-Flask  (Check Out Master Branch For Code)

## Overview
This project is a simple Flask application that integrates with Twilio to initiate voice calls. When a user clicks the "Call ME" button on the web interface, the application uses Twilio's API to make a call to the specified phone number.

## Requirements
- **Python 3.7+**: Ensure you have a compatible version of Python installed.
- **Flask**: The web framework used for this application.
- **Twilio**: The library for interacting with Twilio's API.
- **Twilio Account**: You need a Twilio account with a verified phone number.

## Installation

1. **Install Python and pip**:
   - If you don't have Python installed, follow the instructions for your operating system.
   - Ensure `pip` is installed, which is included in Python 3.4+ installations.

2. **Create a Virtual Environment**:
   ```bash
   python -m venv myenv
   source myenv/bin/activate  # On Windows use `myenv\Scripts\activate`
   ```
3. **Install Required Packages:**:
    ```bash
      pip install Flask twilio
   ```
## Configuration

1. **Set Up Your Twilio Credentials:**
 ```bash
      ACCOUNT_SID = 'your_account_sid'
      AUTH_TOKEN = 'your_auth_token'
      TWILIO_NUMBER = 'your_twilio_number'
   ```

2. **Verify the Phone Number:**
Ensure the phone number you want to call is registered and verified in your Twilio account.

## Running the Application
 ```bash
      git clone https://github.com/Hamza-Tahirr/Outbound-Calls-Using-Twilio-and-Flask.git
      source myenv/bin/activate  # On Windows use
      `myenv\Scripts\activate`
      python app.py
   ```

## Access the Web Interface:
  - Open your web browser and navigate to http://127.0.0.1:5000/.
  - Click the "Call ME" button to initiate a call.
