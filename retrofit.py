import time, os

path = os.path.join("home","Shigure","discordpy-shigubot")

os.system("cd " + path)
os.system("git pull https://github.com/ecfidler/discordpy-shigubot.git")
time.sleep(5)

os.system("ls")
os.system("python3 " + path + "/shigubot.py &")
print("cloned")
