import docker
import logging

logger = logging.getLogger(__name__)

class ContainerMetricsCollector:
    def __init__(self):
        self.client = docker.from_env()

    def get_container_metrics(self, container_name_or_id):
        try:
            container = self.client.containers.get(container_name_or_id)
            stats = container.stats(stream=False)
            logger.info(f"Metrics for Container {container_name_or_id}:")
            logger.info(f"CPU Usage: {stats['cpu_stats']['cpu_usage']['total_usage']}")
            logger.info(f"Memory Usage: {stats['memory_stats']['usage']}")
            logger.info(f"Network Stats: {stats['networks']}")
        except docker.errors.NotFound as e:
            logger.error(f"Container not found: {e}")
        except docker.errors.APIError as e:
            logger.error(f"Failed to retrieve container metrics: {e}")
