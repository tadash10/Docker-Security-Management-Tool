import docker
import logging

logger = logging.getLogger(__name__)

class ContainerScaler:
    def __init__(self):
        self.client = docker.from_env()

    def scale_containers(self, container_name, num_instances):
        try:
            for _ in range(num_instances):
                self.client.containers.run(container_name, detach=True)
            logger.info(f"Scaled {container_name} to {num_instances} instances.")
        except docker.errors.APIError as e:
            logger.error(f"Failed to scale containers: {e}")
