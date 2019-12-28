import os
import sys
ip = sys.argv[1]
user = sys.argv[2]
passw = sys.argv[3]
s_type = sys.argv[4]
command = "rtsp://" + str(user) + ":" + str(passw) + "@" + str(ip) + ":554/cam/realmonitor?channel=1&subtype=" + str(s_type)
#rtsp://admin:cltadmin12@192.168.1.121:554/cam/realmonitor?channel=1&subtype=1
command_s = "vlc "
command_t = command_s + "\"" + command + "\""
print("Opening Stream:- " + command)
os.system(command_t)
