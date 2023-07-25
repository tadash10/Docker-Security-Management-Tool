import docker
import logging

logger = logging.getLogger(__name__)

class HealthChecker:
    def __init__(self):
        self.client = docker.from_env()

    def check_container_health(self, container_name_or_id):
        try:
            container = self.client.containers.get(container_name_or_id)
            health_status = container.attrs.get("State", {}).get("Health", {}).get("Status")
            logger.info(f"Health check for Container {container_name_or_id}: {health_status}")
        except docker.errors.NotFound as e:
            logger.error(f"Container not found: {e}")
        except docker.errors.APIError as e:
            logger.error(f"Failed to perform health check: {e}")

    def check_image_health(self, image_name):
        try:
            image = self.client.images.get(image_name)
            health_status = image.attrs.get("Health", {}).get("Status")
            logger.info(f"Health check for Image {image_name}: {health_status}")
        except docker.errors.ImageNotFound as e:
            logger.error(f"Image not found: {e}")
        except docker.errors.APIError as e:
            logger.error(f"Failed to perform health check: {e}")
