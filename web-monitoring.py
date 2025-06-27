### PROJECT OVERVIEW >> CREATING A SERVER ON LINODE CLOUD PLATFORM, INSTALLING DOCKER ON THAT SERVER, RUNNING NGINX CONTAINER, ACCESSING IT FROM THE WEB 
### PYTHON PROGRAM TO CHECK APPLICATIONS, SENDING EMAIL WHEN THE WEB IS DOWN
### AUTOMATING FIXING THE PROBLEM >> RESTART DOCKER CONTAINER AND SERVER WHEN DOWN 

import requests ### a module to get request from the web.
import smtplib ### library for gmail or email service, as part of project a gmail will be send to us website gets down. 
import os ### need to download the module from the internet hence showing error. 
import paramiko ### python library for ssh connections. need to install it. >> pip install paramiko 
import linode_api4 ### python library for linode cloud first we need to install it locally by pip install linode_api4
import time 
import schedule ##its not installed locally hence showing error here, so first we need to install then import thsi py library. 

EMAIL_ADDRESS = os.environ.get('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD') ### WE SET THESE ENVIRONMENT VARIABLE LOACLLY IN PYCHARM THROUGH UI.
LINODE_TOKEN = os.environ.get('LINODE_TOKEN') ### WE ARE SAVING IT AS ENV VARIABLE 
 
 
 
def restart_server_and_container():
    ### restart linode server 
    ## WE DONT SAVE THE TOKEN INSIDE CODE AS WE PUSH THE CODE TO GIT, SO THIS WOULD CREATE A SECURITY ISSUE. SO WE WILL SAVE IT IN ENV VARIABLES.
    print("REBOOTING THE SERVER....")
    client = linode_api4.LinodeClient(LINODE_TOKEN)
    nginx_server = client.load(linode_api4.Instances, 52236907) 
    nginx_server.reboot()
    
    ### restart the application 
    while True:
        nginx_server = client.load(linode_api4.Instances, 52236907) 
        if nginx_server.status == 'running':
           time.sleep(5)
           restart_container()
           break

def send_notification(email_msg):
    print("sending an email....")
    with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
            smtp.starttls()
            smtp.ehlo()
            smtp.login(EMAIL_ADDRESS , EMAIL_PASSWORD)
            message = f"Subject: SITE DOWN\n{email_msg}"
            smtp.sendmail(EMAIL_ADDRESS, EMAIL_ADDRESS, message)


def restart_container():
    print("Restarting the Application...")
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname="172.09.89.10" , username='root' , key_filename='Users/ali/.ssh/id_rsa') ## here we will put the location of the private key and ipadr as hostname.
    stdin , stdout , stderr = ssh.exec_command('docker start ee65346734ufh') 
    print(stdout.readlines())
    ssh.close ### close the connection once our execution done.
    print("Application restarted")


def monitor_application():
    try:
        response = requests.get('###url of the app')
        if response.status_code == 200:
            print("Up and Running")
        else: 
            print("App down, Fix it.")
            msg = f"Application returned {response.status_code}"
            send_notification(msg)
            restart_container()
    
        
    except Exception as ex:
         print(f"Connection error happend: {ex}")
         msg =  f"Application not accessable at all."
         send_notification(msg)
         restart_server_and_container()
         
schedule.every(5).minutes.do(monitor_application)

while True: 
    schedule.run_pending()