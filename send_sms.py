from twilio.rest import Client


# Your Account Sid and Auth Token from twilio.com/console
# DANGER! This is insecure. See http://twil.io/secure
account_sid = 'ACc2a5792a8f5d9b0299b8118a6c826fde'
auth_token = '8e742a3a4b4d6d3b0eb0bedac1b2560d'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Hey Rachel, This is Emanbot, please text Animesh saying you got this, he's tryna see if this works",
                     from_='+16193243920',
                     to='+19162210003'
                 )

print(message.sid)