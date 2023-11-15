import subprocess
import os

print(subprocess.run(["python launch.py --port " + str(os.environ['CDSW_APP_PORT'])], shell=True))