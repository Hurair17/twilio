import os
import dropbox
import requests
from flask import Flask, request, Response
from dotenv import load_dotenv
from twilio.twiml.voice_response import Gather, VoiceResponse, Dial

load_dotenv()
app = Flask(__name__)


@app.route('/inbound/voice/call', methods=['POST'])
def incoming_voice_call():
    response = VoiceResponse()
    gather = Gather(action='/outbound/voice/call', method='POST')
    gather.say('Please enter the number to dial, followed by the pound sign')
    response.append(gather)
    response.say('We didn\'t receive any input. Goodbye')
    return str(response)
@app.route('/outbound/voice/call', methods=['POST'])


def make_outbound_call():
    phone_number = request.form['Digits']
    response = VoiceResponse()
    dial = Dial(record=True, recording_status_callback='/recording/callback', recording_status_callback_event='completed')
    dial.number(f"+{phone_number}", url='/seek/consent')
    response.append(dial)
    return str(response)


@app.route('/seek/consent', methods=['POST'])
def seek_consent():
    response = VoiceResponse()
    response.say('This call is going to be recorded. You can hang up if you\'re not okay with it')
    return str(response)


if __name__ == '__main__':
    app.run()
