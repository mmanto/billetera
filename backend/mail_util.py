import smtplib
from Cheetah.Template import Template
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import socket



class EMail:

    def __init__(self, smtp_server, port):
        self.server = smtplib.SMTP()
        # Connect to server
        try:
            self.server.connect(smtp_server, port)
        except socket.gaierror:
            print("mail error", "Wrong server, are you sure is correct?")
        except socket.error:
            print("mail error", "Server unavailable or connection refused")

    def login(self, login, password):
        # Login in server
        try:
            self.server.starttls()
            self.server.login(login,password)
        except smtplib.SMTPAuthenticationError:
            print("mail error", "Authentication error")
        except smtplib.SMTPException:
            print("mail error", "No suitable authentication method")

    def sendMail(self, from_addr, to_addr_list, cc_addr_list,
                  subject, message,
                  login, password):
        header  = 'From: %s\n' % from_addr
        header += 'To: %s\n' % ','.join(to_addr_list)
        header += 'Cc: %s\n' % ','.join(cc_addr_list)
        header += 'Subject: %s\n\n' % subject

        message = header + message

        self.login(login, password)
        self.sendEmail(from_addr, to_addr_list, message)
        self.server.quit()

    def sendEmail(self, from_addr, to_addr_list, msg):
             # Send mail
            try:
                self.server.sendmail(msg['From'], to_addr_list, msg.as_string())
            except smtplib.SMTPRecipientsRefused:
                print("mail error", "All recipients were refused."
                          "Nobody got the mail.")
            except smtplib.SMTPSenderRefused:
                print("mail error", "The server didn t accept the from_addr")
            except smtplib.SMTPDataError:
                print("mail error", "An unexpected error code, Data refused")


    def sendMailFromTemplate(self, from_addr, to_addr_list, cc_addr_list,
                      subject, login, password,
                      content_template,
                      template_path):

            msg = MIMEMultipart('alternative')
            msg['From'] = from_addr
            msg['To'] = to_addr_list
            msg['Cc'] = cc_addr_list
            msg['Subject'] = subject

            self.login(login, password)

            nameSpace = content_template
            html = Template(file=template_path, searchList=[nameSpace])

            # encoders.encode_base64(html)
            part1 = MIMEText(str(html), 'html')

            msg.attach(part1)

            #self.server.sendmail(msg['From'], to_addr_list, msg.as_string())
            self.sendEmail(from_addr, to_addr_list, msg)
            self.server.quit()
                #logging.error('No se pudo enviar el correo..')

'''
email = EMail('smtp.gmail.com','587')
email.sendMailFromTemplate('prueba.mmanto@gmail.com',
    'prueba.mmanto@gmail.com',
    '',
    'Hola! este es mi asunto de mensaje',
    'prueba.mmanto',
    'prueba.mmanto2k14',
    {'title': 'Este es mi titulo', 'contents': 'este es mi contenido',
     'links': [{'url' : 'www.google.com','label' : 'Ir a google...'}]},
    'b_logic/mail_templates/mail.tmpl')
'''