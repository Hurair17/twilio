from twilio.rest import Client
# Your Account SID from twilio.com/console
account_sid = "ACd3b2983fb783e5a8ede5301eb338715a"
# Your Auth Token from twilio.com/console
auth_token  = "0f9aec408f3c785c69937a287e56896b"
# The SID of the recording you want to download
recording_sid = "REec28ccf2d5d2eae9679ea79be77b76e4"






client = Client(account_sid, auth_token)
# Retrieve the recording

recording = client.recordings(recording_sid).fetch()
# print(recording.uri)
# Save the recording to a file

url = 'http:///2010-04-01/Accounts/ACd3b2983fb783e5a8ede5301eb338715a/Recordings/REec28ccf2d5d2eae9679ea79be77b76e4'
file = client.request(method= "GET",uri=url)
print(file)
# with open("recording.mp3", "wb") as f:
#     recording.uri.download(f)
    
    #  client.recordings(recording_sid).uri.download(f)
    
