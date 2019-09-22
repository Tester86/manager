import imaplib
import email
import sys

def read_email_from_gmail():
        users = {}
        count = 0
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login('german.cousillas@a.munabe.com','Arrigorriaga.3')
        mail.select('inbox')
        result, data = mail.search(None, 'unseen')
        mail_ids = data[0]
        id_list = mail_ids.split()   
        first_email_id = int(id_list[0])
        latest_email_id = int(id_list[-1])

        for i in range(latest_email_id,first_email_id, -1):
            # need str(i)
            result, data = mail.fetch(str(i), '(RFC822)' )

            for response_part in data:
                if isinstance(response_part, tuple):
                    count += 1
                    # from_bytes, not from_string
                    msg = email.message_from_bytes(response_part[1])
                    email_subject = msg['subject']
                    email_from = msg['from']
                    print(count)
                    if email_from in users:
                        users[email_from] += 1
                    else:
                        users[email_from] = 1
        for i in users:
            print("    " + str(users[i]) + " emails de " + i)
                    

# nothing to print here
read_email_from_gmail()
