
from twilio.rest import Client
import keys
client = Client(keys.SID, keys.token)

message = client.messages.create(
    body="This is new message from twilio",
    from_=keys.twilio_number,
    to=keys.pno
)
print(message.body)
