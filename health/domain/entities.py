"""Domain Entities for Heatlh Module"""
from datetime import datetime


class HealthRecord:
    """Represents a Health Record entity in the Health Context

    Attributes:
    """
    def __init__(self, devide_id: str, bpm: float, created_at:datetime, id: int = None):
        """Initialize a HealthRecord instance
        """
        self.id = id
        self.device_id = devide_id
        self.created_at = created_at
        self.bpm = bpm
