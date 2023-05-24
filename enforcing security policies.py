def enforce_security_policies(container_name):
    command = f"docker exec {container_name} /path/to/security_script.sh"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print(f"Security policies enforced for Container {container_name}.")
    else:
        print(f"Failed to enforce security policies for Container {container_name}.")
