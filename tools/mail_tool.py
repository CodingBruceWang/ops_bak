# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

class MailTool(object):
    # def __init__(self, from_addr, to_addr, subject, smtp_server, password):
    #     self.from_addr = from_addr
    #     self.to_addr = to_addr
    #     self.subject = subject
    #     self.smtp_server = smtp_server
    #     self.password = password

    def send_mail(self, from_addr, to_addr, subject, smtp_server, password):
        msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
        sender = u'Python爱好者 <%s>'%from_addr
        # msg['To'] = self._format_addr(u'管理员 <%s>'%to_addr)
        msg['From'] = from_addr
        msg['To'] = to_addr
        # msg['Subject'] = Header(u'来自SMTP的问候……%'%subject, 'utf-8').encode()
        msg['Subject'] = Header(u'来自SMTP的问候……%', 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        server.set_debuglevel(1)
        server.login(from_addr, password)
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))
