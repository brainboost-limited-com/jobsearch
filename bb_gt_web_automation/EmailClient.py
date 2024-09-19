from imapclient import IMAPClient
import base64
import ssl
import email


class EmailClient:
    
    
    def __init__(self) -> None:
        # Connect to the IMAP server
        self.imap_server = 'outlook.office365.com'
        self.username = 'pablotomasborda@hotmail.com'
        self.password = 'a^&65wcj*r!PC3&Bw7M9'

    def check_email(self,search_criteria='a'):
        # Create an IMAPClient instance and connect
        context = ssl.create_default_context()
        with IMAPClient(self.imap_server, ssl=True, ssl_context=context) as client:
            # Login to your account
            client.login(self.username, self.password)

            # Select the mailbox/folder you want to search
            mailbox = 'INBOX'
            client.select_folder(mailbox)

            # Search for emails
            search_criteria = ['SUBJECT',search_criteria ]
            messages = client.search(search_criteria)

            # Fetch the email data for the matching messages
            for message_id, message_data in client.fetch(messages, 'RFC822').items():
                raw_email = message_data[b'RFC822']
                email_message = email.message_from_bytes(raw_email)

                # Check if the 'SUBJECT' key exists before accessing it
                if 'Subject' in email_message:
                    subject = email_message['Subject']
                else:
                    subject = '[No subject]'
                print("Subject:", subject)

                # Iterate over email parts
                for part in email_message.walk():
                    content_type = part.get_content_type()

                    # Skip printing images
                    if content_type.startswith('image/'):
                        continue

                    try:
                        # Decode the part payload
                        payload = part.get_payload(decode=True)
                        if isinstance(payload, bytes):
                            # Decode the payload using different encodings
                            email_body = payload.decode('utf-8', errors='ignore')
                            break
                    except UnicodeDecodeError:
                        # Unable to decode the part payload
                        print("Unable to decode email body")

                if email_body:
                    # Print the body
                    print("Body:", email_body)
                    return ({'subject': subject,'email_body':email_body})

            # Logout from the server
            client.logout()
