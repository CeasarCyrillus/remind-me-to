# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import sendgrid
import os
from sendgrid.helpers.mail import *
os.environ["SENDGRID_API_KEY"] = "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"
sg = sendgrid.SendGridAPIClient(apikey=os.environ.get('SENDGRID_API_KEY'))
from_email = Email("test@example.com")
to_email = Email("te15ceacyr@falufri.se")
subject = "Sending with SendGrid is Fun"
content = Content("text/plain", "and easy to do anywhere, even with Python")
mail = Mail(from_email, subject, to_email, content)
response = sg.client.mail.send.post(request_body=mail.get())
print(response.status_code)
#print(response.body)
#print(response.headers)