from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'enter acc number'
auth_token = 'enter auth key'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey Rachel, This is Emanbot, please text Animesh saying you got this, he's tryna see if this works",
                     from_='',
                     to=''
                 )

print(message.sid)