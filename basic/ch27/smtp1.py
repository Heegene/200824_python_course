# mail message 사용 객체 선언

from email.message import EmailMessage
import smtplib

# SSL로 open(SMTP 객체 생성
smtp = smtplib.SMTP_SSL('smtp.gmail.com', 465)
# smtp 정상여부 hello test

smtp.ehlo()

# login
smtp.login('dev.heejin@gmail.com', '앱 비밀번호')

# message 생성
msg = EmailMessage()

# 메일내용 내부적으로 dic 선언
msg['Subject'] = '파이썬 mailing test'
msg['From'] = 'dev.heejin@gmail.com'
msg['To'] = 'dev.heejin@gmail.com'
msg.set_content('''
                    청주 얼굴맛집 이콩이!
                    콩이는 얼굴천재다
                    face genius KongE
                ''')

# 메일전송
smtp.send_message(msg)
smtp.quit()


