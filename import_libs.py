"""Python script to set an alarm for a specific time.
   When the alarm goes off, a random youtube video will be opened.
   The possible youtube video URLs are taken from "youtube_alarm_videos.txt"
   A Log file will be created indicating all the steps that has been completed.
"""

"""Authors: David Camilo
           Deval Arora
           Jonatas 
           Saurabh Deswal
"""

"""
   This module imports all the required libraries
"""
import datetime
import os
import time
import random
import webbrowser
from tkinter import *
import tkinter as tk
import smtplib
import logging
