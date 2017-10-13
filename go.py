import os
import sys
import re

if len(sys.argv) <= 1:
    raise ValueError("Invalid input directory")

incoming_dir = sys.argv[1]

for incoming_file in os.listdir(incoming_dir):
    if incoming_file[len(incoming_file)-5:] == ".webm":
        avconv = os.popen("avconv -i "+incoming_dir+incoming_file+" 2>&1").read()
        print(avconv)
        m = re.search(r"Duration: (?P<duration>.*), s", avconv) #Duration: 00:00:21.33,
        duration = m.group("duration")
        time_split = duration.split(":")
        seconds = int(time_split[0])*3600 + int(time_split[1])*60 + float(time_split[2])

        # TODO: Get 3 random points in this video to take screenshots
