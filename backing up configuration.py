def backup_configuration():
    command = "docker exec -it my_container cp /path/to/config.yml /path/to/backup/config.yml"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print("Configuration backup completed.")
    else:
        print("Failed to backup configuration.")
