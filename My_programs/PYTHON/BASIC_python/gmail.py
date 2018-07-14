import smtplib

def send_mail(user,pwd,recipient,subject,body):
    

    gmail_user= user
    gmail_pwd=pwd
    FROM=user
    TO=recipient if type(recipient) is list else[recipient]
    SUBJECT=subject
    TEXT=body
    
    "%s:%d"%("prashant",45)
    message="From: %s \n To:%s\n Subject:%s\n\n%s"%(FROM,",".join(TO),SUBJECT,TEXT)

    server=smtplib.SMTP("smtp.gmail.com",587)

    
    server.ehlo()
    server.starttls()
    server.login(gmail_user,gmail_pwd)
    server.sendmail(FROM,TO,message)
    server.close()
    print"successfully sent the mail"
    #print"failed to send mail"
    

send_mail("manish.25297@gmail.com","m*password*7","anmol14789@gmail.com","helloSUBJECT","manishBODY")
