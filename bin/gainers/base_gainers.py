"""Base abstract classes for all gainer data sources."""

from abc import ABC, abstractmethod


class GainerDownload(ABC):
    """Abstract base class for downloading gainer data."""

    @abstractmethod
    def download(self):
        """Download gainer data from a source."""
        ...

    def source_name(self):
        """Return the name of the source."""
        return self.__class__.__name__


class GainerProcess(ABC):
    """Abstract base class for processing gainer data."""

    @abstractmethod
    def normalize(self):
        """Normalize raw gainer data."""
        ...

    @abstractmethod
    def save_with_timestamp(self):
        """Save normalized data with a timestamp."""
        ...
