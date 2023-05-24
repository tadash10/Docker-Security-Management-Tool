import docker
import subprocess

def check_docker_status():
    client = docker.from_env()
    try:
        client.ping()
        print("Docker is running.")
    except docker.errors.DockerException:
        print("Failed to connect to Docker.")

def check_container_status():
    command = "docker ps -a --format '{{.ID}}\t{{.Names}}\t{{.Status}}'"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Containers: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            container_id, container_name, container_status = line.split("\t")
            print(f"Container ID: {container_id}, Name: {container_name}, Status: {container_status}")
    else:
        print("Failed to retrieve container information.")

def check_images():
    command = "docker images --format '{{.Repository}}\t{{.Tag}}\t{{.Size}}'"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Images: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            repository, tag, size = line.split("\t")
            print(f"Repository: {repository}, Tag: {tag}, Size: {size}")
    else:
        print("Failed to retrieve image information.")

def check_networks():
    command = "docker network ls --format '{{.ID}}\t{{.Name}}\t{{.Driver}}'"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        output = result.stdout.strip().split("\n")
        print(f"Number of Networks: {len(output) - 1}")  # Subtracting header row
        for line in output[1:]:
            network_id, network_name, driver = line.split("\t")
            print(f"Network ID: {network_id}, Name: {network_name}, Driver: {driver}")
    else:
        print("Failed to retrieve network information.")

def check_logs(container_name):
    command = f"docker logs {container_name}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        logs = result.stdout.strip()
        print(f"Logs for Container {container_name}:")
        print(logs)
    else:
        print(f"Failed to retrieve logs for Container {container_name}.")

def run_container(container_name, image_name):
    command = f"docker run --name {container_name} -d {image_name}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        container_id = result.stdout.strip()
        print(f"Container {container_name} started with ID: {container_id}")
    else:
        print(f"Failed to start Container {container_name}.")

def stop_container(container_name):
    command = f"docker stop {container_name}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print(f"Container {container_name} stopped.")
    else:
        print(f"Failed to stop Container {container_name}.")

def remove_container(container_name):
    command = f"docker rm {container_name}"
    result = subprocess.run(command, capture_output=True, text=True, shell=True)
    if result.returncode == 0:
        print(f"Container {container_name} removed.")
    else:
        print(f"Failed to remove Container {container_name}.")

# Main function
def main():
    print("Cloud Security Monitoring and Management (Docker):")
    print("-----------------------------------------------")
    check_docker_status()
    print()
    check_container_status()
    print()
    check_images()
    print()
    check_networks()
    print()
    check_logs("my_container")
    print()
    run_container("my_container", "my_image:latest")
    print()
    stop_container("my_container")
    print()
    remove_container("my_container")

if __name__ == "__main__":
    main()
