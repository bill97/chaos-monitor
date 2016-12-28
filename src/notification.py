
import os
import smtplib


gmail_user = ""  #enter the email id to send from
gmail_pwd = ""   #enter the password of that account

"""
To use the send_notification function, user has to allow his gmail account to be used by less secure
apps, which can be done from https://myaccount.google.com/security , option is available at the last
section of the page.
"""


class Notification:
    """
    Interface which allows user to send notifications.

    """
   
    def __init__(self):
        """
         Set up the information required to send information to desired source.

         Most likely arguments: email, server information etc...

        """
        recipients = open("recipients.txt","a") #: file containing a list of recipients or their emails
        recipients.close()
        

    def add_recipient(self,recipient):
        """
        An email address will be added to the existing list.

        """
        recipients = open("recipients.txt","a") #: text file to append
        recipients.write(recipient + os.linesep)
        recipients.close()

    def send_notification(self, message, recipient):
        """
        A message(written in "message") will be sent to the email address provided as recipient.

        """
        print(message, recipient)
        TO = recipient
        SUBJECT = "Notification from Vulnerability"
        TEXT = message
        server = smtplib.SMTP('smtp.gmail.com', 587)

        server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_pwd) #: a login attemt by server
        BODY = '\r\n'.join(['To: %s' % TO,
                'From: %s' % gmail_user,
                'Subject: %s' % SUBJECT,
                '', TEXT])

        server.sendmail(gmail_user, [TO], BODY)
        print ('email sent')


if __name__ == "__main__":
    notification_sender = Notification()
    message = "Message I want to send"
    source = "Who I want to send the message to. Most likely an email address??"
    notification_sender.send_notification("Hi",'anshul.dbgt@gmail.com')
    
