import subprocess

while True:
	in2 = input(">")
	into=in2.split(" ")
	if into[0]=="start":
		with open("index.html", "w") as f:
			f.write(f"run {into[1]}")
	elif into[0]=="stop":
		with open("index.html", "w") as f:
			f.write("stop")
	elif into[0]=="exit":
		break

