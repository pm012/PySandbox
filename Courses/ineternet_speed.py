# pip install speedtest-cli
import speedtest 
import os
from datetime import date


def speed_test():
    test = speedtest.Speedtest(secure=True) #secure is False by default
    test.get_best_server()
    with open(file_path, "w+") as file:
        file.write(str(date.today()))
    
        down_speed = test.download()
        down_speed = round(down_speed /10 ** 6, 2)
        res = "Download Speed in Mbps: " + str(down_speed)
        file.write(res)
        print(res)


        up_speed = test.upload()
        up_speed = round(up_speed/10**6, 2)
        res = "\n Uopload Speed in Mbps: " + str(up_speed)
        file.write(res)
        print(res)

        ping = test.results.ping
        res = "\n Ping: " + str(ping)
        print(res)
        file.write(res)

if __name__ == "__main__":
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, "st_res.txt")
    
    speed_test()

