"""Factory module to return the appropriate downloader and processor classes."""

from .yahoo_gainers import GainerDownloadYahoo, GainerProcessYahoo
from .wsj_gainers import GainerDownloadWSJ, GainerProcessWSJ


class GainerFactory:
    """Factory class for returning the appropriate gainer downloader and processor."""

    def __init__(self, choice: str):
        """
        Initialize the factory with a source choice.

        Args:
            choice (str): Either 'yahoo' or 'wsj'
        """
        self.choice = choice.lower()
        self._downloaders = {
            'yahoo': GainerDownloadYahoo,
            'wsj': GainerDownloadWSJ,
        }
        self._processors = {
            'yahoo': GainerProcessYahoo,
            'wsj': GainerProcessWSJ,
        }

        if self.choice not in self._downloaders:
            raise ValueError(f"Unrecognized gainer type: {self.choice}")

    def get_downloader(self):
        """Return the downloader class for the selected source."""
        return self._downloaders[self.choice]()

    def get_processor(self):
        """Return the processor class for the selected source."""
        return self._processors[self.choice]()
