import time
from plyer import notification

title ="It's time to drink water now"

message= "You should consume atleast 3.6 litres water in the entire day"
while True:
    notification.notify(title=title,
                        message=message,
                        app_icon=None,
                        timeout=10,
                        )

    time.sleep(60*60)