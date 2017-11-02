import smtplib
import email.mime.multipart
import email.mime.text
 
 msg=email.mime.multipart.MIMEMultipart()
 msg['from']='1078437234@qq.com'
 msg['to']='1479510302@qq.com'
 msg['subject']='test'
 content='''''
     你好，
             这是一封自动发送的邮件。
             
             
 '''
 txt=email.mime.text.MIMEText(content)
 msg.attach(txt)
 
 smtp=smtplib
 smtp=smtplib.SMTP()
 smtp.connect('smtp.qq.com','25')
 smtp.login('1078437234@qq.com','niceW001')
 smtp.sendmail('1078437234@qq.com','1479510302@qq.com',str(msg))
 smtp.quit()
