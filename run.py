import os
import random
import time

from twilio.rest import Client

# Your Twilio account SID and auth token
account_sid = os.environ['ACCOUNT_SID']
auth_token = os.environ['AUTH_TOKEN']

# Your Twilio phone number and the recipient's phone number
twilio_number = os.environ['TWILIO_NUMBER']
recipient_number = os.environ['RECIPIENT_NUMBER']

# Create a Twilio client
client = Client(account_sid, auth_token)

# Wait a random number of seconds in the next 6 hours
delay = 8 * 60 * 60
delay_seconds = random.randint(1, delay)  # Random time in the next 8 hours
time.sleep(delay_seconds)

# Send the message
message = client.messages.create(
    body='Hey, how are you feeling?',
    from_=twilio_number,
    to=recipient_number,
)
