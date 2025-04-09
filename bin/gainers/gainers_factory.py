"""Factory to create appropriate gainer downloader and processor."""

from .yahoo_gainers import GainerDownloadYahoo, GainerProcessYahoo
from .wsj_gainers import GainerDownloadWSJ, GainerProcessWSJ


class GainerFactory:
    """Factory class to return downloader and processor objects."""

    def __init__(self, choice):
        """Initialize the factory with a data source choice."""
        self.choice = choice
        self._downloaders = {
            'yahoo': GainerDownloadYahoo,
            'wsj': GainerDownloadWSJ,
        }
        self._processors = {
            'yahoo': GainerProcessYahoo,
            'wsj': GainerProcessWSJ,
        }

        if self.choice not in self._downloaders:
            raise ValueError(f"Unrecognized gainer type: {choice}")

    def get_downloader(self):
        """Return the appropriate downloader class."""
        return self._downloaders[self.choice]()

    def get_processor(self):
        """Return the appropriate processor class."""
        return self._processors[self.choice]()
