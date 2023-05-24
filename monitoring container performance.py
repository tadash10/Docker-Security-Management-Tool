def monitor_container_performance(container_name):
    command = f"docker stats {container_name}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        stats = result.stdout.strip()
        print(f"Performance stats for Container {container_name}:")
        print(stats)
    else:
        print(f"Failed to retrieve performance stats for Container {container_name}.")
