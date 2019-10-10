

import os, subprocess, time, datetime


while True:
	add = subprocess.Popen("git add .")
	Message = "Auto Commit at "+str(datetime.datetime.now())
	commit = subprocess.Popen('git commit -m '+'"'+Message+'"')
	time.sleep(120)

input()

