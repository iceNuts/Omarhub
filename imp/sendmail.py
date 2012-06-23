# coding: utf-8
# 导入 smtplib 和 MIMEText 
import smtplib 
from email.mime.text import MIMEText 
 
# 定义发送列表 
#mailto_list=[] 
 
# 设置服务器名称、用户名、密码以及邮件后缀 
mail_host = "smtp.126.com" 
mail_user = "buaasoft2009" 
mail_pass = "soft2009" 
mail_postfix="126.com" 
 
# 发送邮件函数 
def send_mail(to, sub, context): 
    '''''
    to_list: 发送给谁
    sub: 主题
    context: 内容
    send_mail("xxx@126.com","sub","context")
    ''' 
    me = mail_user + "<"+mail_user+"@"+mail_postfix+">" 
    msg = MIMEText(context,'plain','utf-8') 
    msg['Subject'] = sub 
    msg['From'] = me 
    msg['To'] = to 
    mailto_list=[]
    mailto_list.append(to)
    try: 
        send_smtp = smtplib.SMTP() 
        send_smtp.connect(mail_host) 
        send_smtp.login(mail_user, mail_pass) 
        send_smtp.sendmail(me, mailto_list, msg.as_string()) 
        send_smtp.close() 
        return True 
    except Exception as e: 
        print(str(e)) 
        return False 
         
if __name__ == '__main__': 
     
    if (True == send_mail(mailto_list,"subject","恭喜你中大奖，请迅速致电18600576221查询详情")): 
        print ("测试成功")
    else: 
        print ("测试失败") 
