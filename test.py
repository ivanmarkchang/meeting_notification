import notification
import time
import datetime

begin_time = datetime.time(18)
end_time = datetime.time(18, 15)

sent = False
while True:
	current_time = datetime.datetime.now().time()
	print('sent:', sent)
	if begin_time <= current_time < end_time:
		if not sent:
			notification.send_notification()
			sent = True
	else:
		sent = False
	time.sleep(10)