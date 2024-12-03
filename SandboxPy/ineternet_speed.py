import speedtest 
from datetime import date

def speed_test():
    test = speedtest.Speedtest()
    with open("st_res.txt", "w+") as file:
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
    speed_test()

