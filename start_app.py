import subprocess

print(subprocess.run(["python launch.py --port=${CDSW_APP_PORT}"], shell=True))