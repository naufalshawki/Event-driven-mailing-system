from kafka import KafkaConsumer
import json
import smtplib
import os
import config_var as conf
from dotenv import load_dotenv
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

load_dotenv()

sender_email = conf.sender_email
sender_password = conf.sender_password
sender_host = conf.sender_host
sender_port = conf.sender_port

consumer = KafkaConsumer(
    bootstrap_servers = conf.kafka_server,
    security_protocol = 'SASL_SSL',
    sasl_mechanism = 'PLAIN',
    sasl_plain_username = conf.kafka_username,
    sasl_plain_password = conf.kafka_password,
    group_id = conf.kafka_group,
    client_id = conf.kafka_client
    )

consumer.subscribe(conf.kafka_topics)

print('Consumer Started')
while True:
    try:
        for message in consumer:
                data = json.loads(message.value)
                mail_content = data['isi']
                
                # The mail addresses and password
                receiver_address = data['email']
                
                #Setup the MIME
                message = MIMEMultipart()
                message['From'] = sender_email
                message['To'] = receiver_address
                
                #The subject line
                message['Subject'] = data['subject']

                #The body and the attachments for the mail
                message.attach(MIMEText(mail_content, 'plain'))
                
                #Create SMTP session for sending the mail
                session = smtplib.SMTP(sender_host, sender_port) #use gmail with port
                session.starttls() #enable security
                session.login(sender_email, sender_password) #login with mail_id and password
                text = message.as_string()
                session.sendmail(sender_email, receiver_address, text)
                session.quit()
                print('Mail Sent')

    except Exception as e:
        print(e)
    
    finally : 

        try :
            session.quit()
            print('smtp session flushed')
        
        except Exception as e:
            print(e)
