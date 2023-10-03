
import os
from twilio.rest import Client
import re
account_sid = "ACb316103c2548187fa72d3e5f25ad8e9d"
auth_token = "94d197246d949e899612fc37a5ebabc0"
def sendsms(mobile_number):
    client = Client(account_sid, auth_token)
    if mobile_number.startswith("+91"):
        to_number = mobile_number
    else:
        clean_number = re.sub(r"\D", "", mobile_number)
        to_number = "+91" + clean_number
    message = client.messages.create(
                    from_='+12707431151',
                    body=f"Thank you for submitting your enquiry to Pestokiller. We acknowledge that we have received your response successfully. Our team will review your enquiry and get back to you shortly.",
                    to=to_number)

 





