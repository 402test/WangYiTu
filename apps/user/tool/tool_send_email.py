# encoding: utf-8
__author__ = 'ChengweiHuang'
__date__ = '2019/3/5 16:37'
from random import Random
from django.core.mail import send_mail
from user.models import EmailVerifyRecord

from Wa.settings import EMAIL_FROM
def random_str(randomlength=8):
    str = ''
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str+=chars[random.randint(0, length)]
    return str



def send_register_email(email, send_type="register"):
    code = random_str(16)
    email_title = "喝酒不叫我---注册"
    email_record = EmailVerifyRecord()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    if send_type =='register':
        email_body = "请点击下面的链接激活你的账号: http://127.0.0.1:8000/active/{0}".format(code)
    elif send_type=='forget':
        email_body = "请点击下面的链接修改你的密码: http://127.0.0.1:8000/active/{0}".format(code)
    try:

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            return True
    except Exception as e:
        print(e)
        return False
