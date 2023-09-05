import subprocess
import time
import sys
def main():
    # Define the command you want to run

    print("started in a venv? ",sys.prefix != sys.base_prefix)
    try:
        """         if(not isVenv):
            subprocess.run(commandActVenv, shell=True, check=True) """
        creat = subprocess.Popen(["daiporcodio/bin/python3.11", "TheCreator.py", "-c"])
        creat.wait()
        time.sleep(5)
        upl = subprocess.Popen(["daiporcodio/bin/python3.11", "TheCreator.py", "-u"])
        upl.wait()
        return
        """ subprocess.run(commandCreate, shell=True, check=True)
        time.sleep(5)
        subprocess.run(commandUp, shell=True, check=True) """
    except subprocess.CalledProcessError as e:
        print(f"Error running the command: {e}")
        return

if __name__ == "__main__":
    main()
