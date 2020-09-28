import os


class User:
    def __init__(self, name, mail1, mail2=None, city=None):
        self.name = name
        self.mail1 = mail1
        self.mail2 = mail2
        self.city = city
        self.db_path = os.path.normpath(os.getcwd() + f'/SR_Data/userdata/db/{self.name}_db/{self.name}_db.csv')
        self.rep_dir = os.path.normpath(os.getcwd() + f'/SR_Data/userdata/reports/{self.name}_reports')

    def send_mail(self, subject, message):
        # import modules
        import smtplib
        import ssl
        from email.mime.multipart import MIMEMultipart
        from email.mime.text import MIMEText
        from sucsessreports.MailBot import MailBot

        # setup data for bot
        bot = MailBot()
        bot.get_cred("smtp")

        # create Message:
        msg = MIMEMultipart()
        msg["From"] = bot.name
        msg["To"] = self.mail1
        msg["Subject"] = subject
        msg.attach(MIMEText(message))
        text = msg.as_string()

        # getting connection and logging in
        contxt = ssl.create_default_context()
        server = smtplib.SMTP(bot.server, bot.port)
        server.ehlo()
        server.starttls(context=contxt)
        print(server.login(bot.name, bot.pw))

        # sending mail
        server.sendmail(bot.name, self.mail1, text)

        # logging out
        print(server.quit())

    def get_mail(self):
        # import modules
        from imapclient import IMAPClient
        from sucsessreports.MailBot import MailBot

        # setup bot data
        bot = MailBot()
        bot.get_cred("imap")

        # connect to imap server
        # print(bot.server + bot.name + bot.port)
        server = IMAPClient(bot.server, port=bot.port, use_uid=True, ssl=True)
        print(server.login(bot.name, bot.pw))

        # select messages
        # print(server.list_folders())
        server.select_folder('INBOX', readonly=False)
        uids = server.search(['FROM', self.mail1, 'UNSEEN'])
        # print(uids)

        # save messages to file with email module
        if len(uids) > 0:
            import email
            from sucsessreports.Entry import Entry
            from datetime import datetime

            for uid in uids:
                r_msg = server.fetch([uid], ['RFC822'])
                # print(r_msg[uid][b'RFC822'])
                msg = email.message_from_bytes(r_msg[uid][b'RFC822'])

                if not msg.get_payload() is None:
                    # get clean from address
                    clean_from = msg.get("from").split()[-1][1:-1]

                    # get a clean date
                    messy_date = " ".join(msg.get("date").split()[0:4])
                    clean_date = datetime.strptime(messy_date, "%a, %d %b %Y").date()

                    # get text from message
                    clean_text = ""
                    for part in msg.walk():
                        if part.get_content_type() == 'text/plain':
                            clean_text = part.get_payload().split('\r\n\r\n')[0]

                    ent = Entry(uid, clean_date, clean_from, msg.get("subject"), clean_text)
                    ent.save(f'./SR_Data/userdata/db/{self.name}_db/{self.name}_db.csv')

        else:
            print("no messages found")

        print(server.logout())

    def create_report(self):
        # select the messages that match the filter and pass a list of entrys to ReportWriter
        pass

# ToDo:
#     create a method to construct the report
#     optional (not really needed atm):
#           find way to filter out signatures
#           find method to send attachments
#
#
# ----- old code -----
# save messages to file pyzmail
# if len(uids) > 0:
#     import pyzmail
#     from sucsessreports.Entry import Entry
#
#     for uid in uids:
#         r_msg = server.fetch([uid], ['BODY[]', 'FLAGS', 'ENVELOPE'])
#         msg = pyzmail.PyzMessage.factory(r_msg[uid][b'BODY[]'])
#         # head = msg.get_decode_header("date")[1]
#         # print(head)
#
#         if msg.text_part is not None:
#             ent = Entry(uid, msg.get_addresses("from")[0][1], msg.get_subject(),
#                         msg.text_part.get_payload().decode(msg.text_part.charset).split("\r\n\r\n"))
#             ent.save("./SR_Data/data.csv")
#             print("message saved")
