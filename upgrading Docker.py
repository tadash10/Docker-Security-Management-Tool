def upgrade_docker():
    command = "sudo apt-get update && sudo apt-get upgrade -y docker-ce"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print("Docker upgrade completed.")
    else:
        print("Failed to upgrade Docker.")
