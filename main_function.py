"""Python script to set an alarm for a specific time.
   When the alarm goes off, a random youtube video will be opened.
   The possible youtube video URLs are taken from "youtube_alarm_videos.txt"
   A Log file will be created indicating all the steps that has been completed.
"""

"""Authors: David  
            Deval  
            Jonatas 
            Saurabh  
"""


#import all the required libraries
import datetime
from user_interface import *
from check_input import *
from logger import *

def my_main_function(alarm_time):
    
    """ This main function captures the input value and checks if the value is correct 
        or not. Raise exception if the value is wrong.
        
        args(string): The input alarm_time is a string input
    """
    
    #This Try and Except block will raise exception if the input value is incorrect
    while True:
        try:
            alarm_input_list = [int(n) for n in alarm_time.split(":")]
            if check_alarm_input(alarm_input_list):
                logging.debug("PASS: The time is in correct format")
                check_link_format()
                break
            else:
                raise ValueError
        except ValueError:
            logging.critical("FAIL: Please enter the time in correct format")
            break 
    
    seconds_hms = [3600, 60, 1] # Number of seconds in an Hour, Minute, and Second
    alarm_seconds = sum([a*b for a,b in zip(seconds_hms[:len(alarm_input_list)], alarm_input_list)])
    
    now = datetime.datetime.now()
    current_time_seconds = sum([a*b for a,b in zip(seconds_hms, [now.hour, now.minute, now.second])])
    
    time_diff_seconds = alarm_seconds - current_time_seconds
    if time_diff_seconds < 0:
        time_diff_seconds += 86400 # number of seconds in a day
    
     

