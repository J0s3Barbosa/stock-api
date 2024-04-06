import subprocess

# Create a virtual environment (optional but recommended)
subprocess.run(["python", "-m", "venv", "env"])

# Activate the virtual environment (On Windows)
subprocess.run(["env\\Scripts\\activate"], shell=True)

# Update pip to the latest version
subprocess.run(["py", "-m", "pip", "install", "--upgrade", "pip"])

# Install the required packages
subprocess.run(["pip", "install", "-r", "requirements.txt"])
