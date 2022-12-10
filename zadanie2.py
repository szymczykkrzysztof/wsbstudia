import os

path = os.environ['IDEA_INITIAL_DIRECTORY']

os.system(f'cmd /c "cd {path}\\nauka\\wsbstudia && dir /s new.txt >> result.txt"')
