"""Main entry point for processing stock gainers."""

# pylint: disable=E0401, E0611, R0903

from bin.gainers.factory import GainerFactory


class ProcessGainer:
    """Handles the template process for downloading and processing gainers."""

    def __init__(self, downloader, processor):
        """Initialize with a downloader and processor."""
        self.downloader = downloader
        self.processor = processor

    def process(self):
        """Run the download, normalize, and save steps."""
        self.downloader.download()
        self.processor.normalize()
        self.processor.save_with_timestamp()


if __name__ == "__main__":
    import sys

    choice = sys.argv[1]
    factory = GainerFactory(choice)
    runner = ProcessGainer(factory.get_downloader(), factory.get_processor())
    runner.process()
