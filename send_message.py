# Download the helper library from https://www.twilio.com/docs/python/install
import os
from twilio.rest import Client



# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ.get('twilio_account_sid_test')
auth_token = '8e48f637988000a21741d4caf5a0279c'
# client = Client(account_sid, auth_token)

# message = client.messages \
#                 .create(
#                      body="Join Earth's mightiest heroes. Like Kevin Bacon.",
#                      from_='+18337026590',
#                      to='+16786404053'
#                  )
#
# print(message.sid)

print(account_sid)
print(os.environ.get("twilio_account_sid_test"))
