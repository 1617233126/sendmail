import smtplib
import email.mime.multipart
import email.mime.text
 
 msg=email.mime.multipart.MIMEMultipart()
 msg['from']='13401386003@163.com'
 msg['to']='1078437234@qq.com'
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
 smtp.login('13401386003@163.com','niceW001')
 smtp.sendmail('13401386003@163.com','1078437234@qq.com',str(msg))
 smtp.quit()
