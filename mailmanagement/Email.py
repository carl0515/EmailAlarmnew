#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:carrot
# Time :2020/9/16 13:33

import sys
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class Email_send(object):
    def __init__(self,msgTo,data2,Subject):
        self.msgTo=msgTo
        self.data2=data2
        self.Subject=Subject

    def sendEmail(self):
        # (attachment,html) = content
        msg = MIMEMultipart()
        msg['Subject'] = self.Subject
        msg['From'] = 'cc.1204899702@qq.com'
        msg['To'] = '727008203@qq.com'
        html_att = MIMEText(self.data2, 'html', 'utf-8')
        #att = MIMEText(attachment, 'plain', 'utf-8')
        msg.attach(html_att)
        #msg.attach(att)
        try:
            smtp = smtplib.SMTP_SSL()
            smtp.connect('smtp.qq.com', 465)
            smtp.login(msg['From'], 'uxhgvhqkywhdhjja') #邮箱密码
            smtp.sendmail(msg['From'], msg['To'].split(','), msg.as_string())
            return('成功发送邮件')
        except Exception as e:
            print('$$$$$$',e)

    def curl(self):
        import pycurl
        c=pycurl.Curl()
        #indexfile=open(os.path.dirname(os.path.realpath(__file__))+"/content.txt","wb")
        c.setopt(c.URL,url)
        c.setopt(c.VERBOSE,1)
        c.setopt(c.ENCODING,"gzip")
        #模拟火狐浏览器
        c.setopt(c.USERAGENT,"Mozilla/5.0 (Windows NT 6.1; rv:35.0) Gecko/20100101 Firefox/35.0")
        return c


