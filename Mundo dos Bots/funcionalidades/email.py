#!/usr/bin/env python
# -*- coding: utf-8 -*-

import smtplib #EMAIL
import unicodedata #REMOVER ACENTUAÇÕES

'''função para enviar emails'''
def send_email(user, pwd, recipient, subject, body):
    
    '''Valores do E-mail'''
    gmail_user = user
    gmail_pwd = pwd
    FROM = user
    TO = recipient if type(recipient) is list else [recipient] #pode ser uma lista
    SUBJECT = subject
    TEXT = body

    # Preparar a mensagem
    message = """From: %s\nTo: %s\nSubject: %s\n\n%s
    """ % (FROM, ", ".join(TO), SUBJECT, TEXT)
    
    #tenta mandar usando smpt
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.ehlo()
        server.starttls()
        server.login(gmail_user, gmail_pwd)
        server.sendmail(FROM, TO, message)
        server.close()
        print ("email enviado com sucesso")
    except:
        print ("falha ao enviar email")