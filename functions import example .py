import logging
from container_scaling import ContainerScaler
from health_checks import HealthChecker
from container_metrics import ContainerMetricsCollector

# Initialize logger
logging.basicConfig(level=logging.INFO, format="[%(levelname)s] %(message)s")
logger = logging.getLogger(__name__)

def main():
    # Example usage of Container Scaling
    scaler = ContainerScaler()
    scaler.scale_containers("my_container", num_instances=3)

    # Example usage of Health Checks
    checker = HealthChecker()
    checker.check_container_health("my_container")
    checker.check_image_health("my_image")

    # Example usage of Container Metrics
    metrics_collector = ContainerMetricsCollector()
    metrics_collector.get_container_metrics("my_container")

if __name__ == "__main__":
    main()
