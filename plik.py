import os
import time

os.chdir(f"{os.environ['IDEA_INITIAL_DIRECTORY']}\\nauka\\wsbstudia")
os.mkdir("nowy folder")
print(os.listdir(os.getcwd()))
time.sleep(2)
print(os.getcwd())
os.rename("nowy folder", "zmiana nowy folder")
print(os.listdir(os.getcwd()))
time.sleep(2)
os.rmdir("zmiana nowy folder")
print(os.listdir(os.getcwd()))
print(os.getcwd())
print(os.system("git status"))
os.system(f"cmd /c cd {os.environ['IDEA_INITIAL_DIRECTORY']}'")
