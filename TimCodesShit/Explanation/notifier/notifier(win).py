from pynotifier import Notification
import time

Notification(
	title='Notification Title',
	description='Notification Description',
	#icon_path='path/to/image/file/icon.png', # On Windows .ico is required, on Linux - .png
	duration=5,                              # Duration in seconds
	#urgency=Notification.URGENCY_CRITICAL
).send()

time.sleep(6) #code must sleep long enough for the other notification to go away. Else the second notification doesnt come

Notification(
	title='Notification Title',
	description='Notification Description',
	#icon_path='path/to/image/file/icon.png', # On Windows .ico is required, on Linux - .png
	duration=5,                              # Duration in seconds
	#urgency=Notification.URGENCY_CRITICAL
).send()