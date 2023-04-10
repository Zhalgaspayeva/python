import datetime
import time
x3 = datetime.datetime.now().timetuple()
x = datetime.datetime(int(input()), int(input()), int(input())).timetuple()
s3 = time.mktime(x3)
s = time.mktime(x)

print(s3 - s)