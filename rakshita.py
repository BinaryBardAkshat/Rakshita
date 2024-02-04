import subprocess
import logging

# Configure logging
logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s',
                    datefmt='%Y-%m-%d %H:%M:%S',
                    filename='script_runner.log',
                    filemode='a')

def run_script(script_path):
    try:
        logging.info(f"Running script: {script_path}")
        subprocess.run(["python", script_path], check=True)
        logging.info(f"Script executed successfully: {script_path}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running script: {script_path}")
        logging.error(f"Error details: {e}")

if __name__ == "__main__":
    
    scripts = [
        "ECU.py",
        "finder.py",
        "Sender.py",
        "call.st.1.py",
        "encryption.py"
       
    ]

    # Run each script in a separate process
    for script in scripts:
        run_script(script)
