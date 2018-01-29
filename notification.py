#add comment
import os

filename = "/Users/ivan/notification.txt"

def send_notification():
	os.system("open " + filename)
	print("sent notification")

print("notification.py name:", __name__)

if __name__ == '__main__':
	send_notification()