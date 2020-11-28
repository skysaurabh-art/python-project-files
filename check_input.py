import random
import requests
import webbrowser
import time
import smtplib

def check_alarm_input(alarm_input):
    
    """ This function validates if the the input value is entered in correct format or not
        
        args (list): Takes alarm_input value as a list
        
        Returns True if input format is correct otherwise False
    
    """
    
    if len(alarm_input) == 1: 
        # [Hour] Format
        if (alarm_input[0] < 24) and (alarm_input[0] >= 0):
            return True
    if len(alarm_input) == 2: 
        # [Hour:Minute] Format
        if (alarm_input[0] < 24) and (alarm_input[0] >= 0) \
            and (alarm_input[1] < 60) and (alarm_input[1] >= 0):
            return True
    elif len(alarm_input) == 3: 
        # [Hour:Minute:Second] Format
        if (alarm_input[0] < 24 and alarm_input[0] >= 0) and \
           (alarm_input[1] < 60 and alarm_input[1] >= 0) and \
           (alarm_input[2] < 60 and alarm_input[2] >= 0):
            return True
    return False

def check_link_format():
    """This function checks if the input youtube link provided is correct or not"""
    
    #To read the input text file
    with open("youtube_alarm_videos.txt", "r") as alarm_file:
         videos = alarm_file.readlines()
        
    #Opens a random youtube video from a set of youtube videos
    x=random.choice(videos)
    
    try:
       r = requests.head(x)
       print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
       time.sleep(time_diff_seconds)
       logging.debug("Wake up!: The time has come! Opening your youtube video!")
       webbrowser.open(x)
    except requests.ConnectionError:
       logging.debug("FAIL: The input link is invalid")
       
    # creates SMTP session 
    #s = smtplib.SMTP('smtp.gmail.com', 587) 
  
    # start TLS for security 
    #s.starttls() 
  
    # Authentication 
    #s.login("sender@gmail.com", "sender_password") 
  
    # message to be sent 
    #message = "Message_you_need_to_send"
  
    # sending the mail 
    #s.sendmail("sender@gmail.com", "receiver@gmail.com", message) 
  
    # terminating the session 
    #s.quit() 
    

    

    