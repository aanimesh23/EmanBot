from flask import Flask, request
import process
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def sms_ahoy_reply():
    """Respond to incoming messages with a friendly SMS."""
    # Start our response
    # for i in request.values.keys():
    # 	print(i)
    phonebook = {"+19497716557": "Animesh", "+19162210003": "Rachel"}
    msg = request.values.get("Body")
    print("{} sent the message {}".format(request.values.get("From"), msg))
    r_msg = process.reply_with(msg)
    print("message sent is: {}".format(r_msg))
    resp = MessagingResponse()

    # Add a message
    resp.message(r_msg)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)