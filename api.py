from twilio.rest import Client

account_sid = "Get SID From Twilio Account"
auth_token = "Get Token From Twilio Account"

client = Client(account_sid, auth_token)

from_ = "whatsapp:+14155238886"
to = "whatsapp:+221778577500"

client.messages.create(body="Testing via twilio", from_=from_, to=to)
