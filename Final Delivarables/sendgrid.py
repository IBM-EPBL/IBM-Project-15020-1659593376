# # using SendGrid's Python Library
# # https://github.com/sendgrid/sendgrid-python
# import os
# from sendgrid import SendGridAPIClient
# from sendgrid.helpers.mail import Mail

# message = Mail(
#     from_email='sample_email@example.com',
#     to_emails='sample@gmail.com',
#     subject='Sending with Twilio SendGrid is Fun',
#     html_content='<strong>and easy to do anywhere, even with Python</strong>')
# try:
#     sg = SendGridAPIClient('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')
#     response = sg.send(message)
#     print(response.status_code)
#     print(response.body)
#     print(response.headers)
# except Exception as e:
#     print(e.message)


# using SendGrid's Python Library
# https://github.com/sendgrid/sendgrid-python
import os
import sendgrid
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='from_email@example.com',
    to_emails='to@example.com',
    subject='Sending with Twilio SendGrid is Fun',
    html_content='<strong>and easy to do anywhere, even with Python</strong>')
try: 
    sg = SendGridAPIClient('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')
    response = sg.send(message)
    print(response.status_code)
    print(response.body)
    print(response.headers)
except Exception as e:
    print(e.message)