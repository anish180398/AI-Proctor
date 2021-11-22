from eye_tracker import tracked_eye
from phone_detector import mobile_detection
from head_pose_estimation import tracked_head
from mouth_movement import mouthOpenCount
import smtplib, ssl
import cv2
import numpy as np

capture = cv2.VideoCapture(0)
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email = "anish18398@gmail.com"  # Enter your address
receiver_email = "anish18398@gmail.com"  # Enter receiver address
password = "RebelUnited@18"
message = """
Subject: Hi there

This message is sent from Python."""


print(tracked_eye)
print(tracked_head)
print(mobile_detection)
print(mouthOpenCount)


'''

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

'''

