from import_libs import *
from user_interface import *
from check_input import *
from logger import *

def my_main_function(alarm_time):
    
    """ This main function captures the input value and checks if the value is correct 
        or not. Raise exception if the value is wrong.
        
        args(string): The input alarm_time is a string input
    """
    
    #This Try and Eexcept block will raise exception if the input value is not correct
    while True:
        try:
            alarm_input_list = [int(n) for n in alarm_time.split(":")]
            if check_alarm_input(alarm_input_list):
                logging.debug("PASS: The time is in correct format")
                break
            else:
                raise ValueError
        except ValueError:
            logging.critical("ERROR: Please enter the time in correct format")
            break 
    
    seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_input_list)], alarm_input_list)])
    
    now = datetime.datetime.now()
    current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
    
    time_diff_seconds = alarm_seconds - current_time_seconds
    if time_diff_seconds < 0:
        time_diff_seconds += 86400 # number of seconds in a day
    print("Alarm set to go off in %s" % datetime.timedelta(seconds=time_diff_seconds))
    
    time.sleep(time_diff_seconds)
    logging.debug("Wake up!: The time has come!")
    
    #To read the input text file
    with open("youtube_alarm_videos.txt", "r") as alarm_file:
         videos = alarm_file.readlines()
        
    #Opens a random youtube video from a set of youtibe videos
    webbrowser.open(random.choice(videos))
    logging.debug("PASS: The youtube video has been opened in the web browser")

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
    

    
