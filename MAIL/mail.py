#!/usr/bin/python3
# -*- coding: utf-8 -*-
# Author:carrot
# Time :2019/11/29 10:04

import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

mail_host =('smtp.qq.com')
port =465
send_by = ('cc.1204899702@qq.com')
password = ('uxhgvhqkywhdhjja')
send_to = ('727008203@qq.com')

def send_mail(title,content,):
    m=MIMEText(content,'plain','utf-8')
    m['From']=send_by
    m['To']=send_to
    m['Subject']=title
    #登录
    try:
        smpt=smtplib.SMTP_SSL(mail_host,port,'utf-8')
        smpt.login(send_by,password)
        smpt.sendmail(send_by,send_to,m.as_string())
        print('success!')
    except smtplib.SMTPException as e:
        print('Error:',e)
if __name__=="__main__":
    title='Test'
    content='恭喜你收到邮件！'
    send_mail(title,content)
