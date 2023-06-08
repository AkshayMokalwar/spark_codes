from time import sleep
from datetime import datetime
# import time
# sys.exit()
start_time = datetime.now().strftime("%S")
print(start_time)

while(int(start_time)+30<50):
    print("s")
    sleep(5)
print("a")
# while(start_time):
#     print(start_time)
#     print("hello world")
#     sleep(5)
#     print("After five second")
#     sleep(25)
#     print("After twentyfive second")
#     # end_time=time()
#     print(end_time)
#     print("total time exceution : {0}".format(end_time-start_time))