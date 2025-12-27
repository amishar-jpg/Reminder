import time
from plyer import notification

while True:
    notification.notify(
        title="Reminder",
        message="Time to take a short break, stretch and drink water!",
    )
    time.sleep(60*60);  