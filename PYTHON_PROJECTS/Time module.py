

import time

# Get current hour in 24-hour format
current_hour = int(time.strftime('%H'))
current_time = time.strftime('%H:%M:%S')

print(f"Current Time: {current_time}\n")

if 5 <= current_hour < 12:
    print("Good Morning, Sir!")
elif 12 <= current_hour < 17:
    print("Good Afternoon, Sir!")
elif 17 <= current_hour < 21:
    print("Good Evening, Sir!")
else:
    print("Good Night, Sir!")