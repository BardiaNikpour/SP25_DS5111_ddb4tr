"""WSJ-specific gainer classes."""

from .base_gainers import GainerDownload, GainerProcess

class GainerDownloadWSJ(GainerDownload):
    """Downloads gainer data from WSJ."""

    def download(self):
        """Download WSJ gainer data."""
        print("Downloading WSJ gainers")


class GainerProcessWSJ(GainerProcess):
    """Processes WSJ gainer data."""

    def normalize(self):
        """Normalize WSJ gainer data."""
        print("Normalizing WSJ gainers")

    def save_with_timestamp(self):
        """Save normalized WSJ data with timestamp."""
        print("Saving WSJ gainers")
