import subprocess
import time
import sys
def main():
    # Define the command you want to run
    commandCreate = "python3 TheCreator.py -c"
    commandUp = "python3 TheCreator.py -u"
    commandActVenv = "source daiporcodio/bin/activate"
    print(sys.prefix != sys.base_prefix)
    isVenv = sys.prefix != sys.base_prefix
    # Use subprocess to run the command in the Command Prompt

    try:
        if(not isVenv):
            subprocess.run(commandActVenv, shell=True, check=True)
        subprocess.run(commandCreate, shell=True, check=True)
        time.sleep(5)
        subprocess.run(commandUp, shell=True, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error running the command: {e}")
        return

if __name__ == "__main__":
    main()
