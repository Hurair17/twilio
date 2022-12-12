import os
from twilio.rest import Client

account_sid = 'ACd3b2983fb783e5a8ede5301eb338715a'
auth_token = '0f9aec408f3c785c69937a287e56896b'
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='http://demo.twilio.com/docs/voice.xml',
                        # twiml='<Response><Say> Welcome Hurair</Say><Response>',
                        recording_track='inbound',
                        record=True,
                        to = '+923035966833',
                        from_='+18339262040'
                    )



print(call)
