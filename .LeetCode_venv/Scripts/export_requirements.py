import subprocess

# Run pip freeze command and decode the output
output = subprocess.check_output(["pip", "freeze"]).decode("utf-8")

# Write output to requirements.txt file
with open("requirements.txt", "w") as f:
    f.write(output)
