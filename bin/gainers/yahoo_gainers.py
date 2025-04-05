"""yahoo-specific gainer classes."""
from .base_gainers import GainerDownload, GainerProcess

class GainerDownloadYahoo(GainerDownload):
    """Downloads gainer data from yahoo."""

    def download(self):
        """Download uahoo gainer data."""
        print("Downloading Yahoo gainers")

class GainerProcessYahoo(GainerProcess):
    """Processes yahoo gainer data."""

    def normalize(self):
        """Normalize yahoo gainer data."""
        print("Normalizing Yahoo gainers")

    def save_with_timestamp(self):
        """Save normalized yahoo data with timestamp."""
        print("Saving Yahoo gainers")
