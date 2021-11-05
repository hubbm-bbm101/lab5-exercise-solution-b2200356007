e_mail=input("please enter your e-mail=")

def valid_email(e_mail):
    if "@" in e_mail and "." in e_mail:
        print(e_mail,"is a valid e-mail.")
    else:
        print(e_mail,"is not a valid e-mail.")
valid_email(e_mail)