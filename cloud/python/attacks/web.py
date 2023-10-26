import subprocess

subprocess.Popen(["python", "-m", "http.server", "8888", "--bind", "0.0.0.0"])
