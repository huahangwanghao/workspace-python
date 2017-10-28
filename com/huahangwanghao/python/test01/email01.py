#coding:utf-8
import smtplib
from email.mime.text import  MIMEText
from email.header import  Header

main_host='smtp.163.com'
main_user='18101307677@163.com'
main_pass='www.wanghao.com1'
sender="18101307677@163.com"
rec="309140958@qq.com"
message=MIMEText("张春春,同学你好!很高兴可以和你共进午餐,请您务必在到来的路上想好吃什么? 谢谢~","plain","utf-8")
message['From']="18101307677@163.com"
message['To']="309140958@qq.com"
subject="姐姐收的到吗?"
message['Subject']=Header(subject,'utf-8')
try:
    smtpObj=smtplib.SMTP()
    smtpObj.connect(main_host,25)
    smtpObj.login(main_user,main_pass)
    smtpObj.sendmail(sender,rec,message.as_string())
    smtpObj.quit()
    print("发送成功")
except smtplib.SMTPException as e:
    print("发送邮件失败",e)