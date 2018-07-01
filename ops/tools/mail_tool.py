# -*- coding: utf-8 -*-
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib
import logging

class MailTool(object):
    smtp_server = 'smtp.163.com'
    from_addr = user = 'wangfoqing25@163.com'
    password = 'wangfoqing25'

    def _get_smtp_server(self):
        try:
            server = smtplib.SMTP(self.smtp_server, 25)
            server.set_debuglevel(1)
            server.login(self.user, self.password)
        except  Exception, e:
            logging.error('logon smtp server failed. %s' % e.message)
            return None
        return server

    # 发送普通的文本文件
    def send_mail(self, from_addr, to_addr, subject, content):
        mail_content = 'hello, send by Python...; %s' %content
        msg = MIMEText(mail_content, 'plain', 'utf-8')
        sender = u'Python爱好者 <%s>'%from_addr
        # msg['To'] = self._format_addr(u'管理员 <%s>'%to_addr)
        msg['From'] = from_addr
        msg['To'] = to_addr
        # msg['Subject'] = Header(u'来自SMTP的问候……%'%subject, 'utf-8').encode()
        # msg['Subject'] = Header(u'来自SMTP的问候……%', 'utf-8').encode()
        msg['Subject'] = Header(subject, 'utf-8').encode()

        server = self._get_smtp_server()
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()

    def _format_addr(s):
        name, addr = parseaddr(s)
        return formataddr(( \
            Header(name, 'utf-8').encode(), \
            addr.encode('utf-8') if isinstance(addr, unicode) else addr))

    # 发送html邮件
    def send_html_mail(self, from_addr, to_addr, subject, content):
        mail_content = '<html><body><h1>Hello; %s</h1>' % content + '<p>send by <a href="http://www.python.org"></a>...</p>' + '</body></html>'
        msg = MIMEText(mail_content, 'html', 'utf-8')
        msg['From'] = from_addr
        msg['To'] = to_addr
        msg['Subject'] = Header(subject, 'utf-8').encode()
        server = self._get_smtp_server()
        server.sendmail(from_addr, [to_addr], msg.as_string())
        server.quit()
