import subprocess, sys, time

for i in range(sys.argv[3]):
  subprocess.Popen(["ping", f"{sys.argv[1]}", "-c", f"{sys.argv[2]}", "-s", f"{sys.argv[4]}"])
  time.sleep(1.5)
