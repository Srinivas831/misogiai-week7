from abc import ABC, abstractmethod
from typing import List

# ---------------- MediaContent ABC ----------------
class MediaContent(ABC):
    def __init__(self, title, premium=False):
        self.title = title
        self.ratings = []
        self.premium = premium

    @abstractmethod
    def play(self):
        pass

    @abstractmethod
    def get_duration(self):
        pass

    @abstractmethod
    def get_file_size(self):
        pass

    @abstractmethod
    def calculate_streaming_cost(self):
        pass

    def add_rating(self, rating):
        self.ratings.append(rating)

    def get_average_rating(self):
        return sum(self.ratings) / len(self.ratings) if self.ratings else None

    def is_premium_content(self):
        return self.premium

# ---------------- StreamingDevice ABC ----------------
class StreamingDevice(ABC):
    def __init__(self, name):
        self.name = name

    @abstractmethod
    def connect(self):
        pass

    @abstractmethod
    def stream_content(self, content: MediaContent):
        pass

    @abstractmethod
    def adjust_quality(self):
        pass

    def get_device_info(self):
        return f"{self.name} is ready."

    def check_compatibility(self, content: MediaContent):
        return True  # Basic compatibility check
