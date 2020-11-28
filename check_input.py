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
    