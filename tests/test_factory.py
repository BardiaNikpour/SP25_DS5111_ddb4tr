import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append('.')

from bin.gainers.factory import GainerFactory

def test_factory_yahoo():
    factory = GainerFactory("yahoo")
    assert factory.get_downloader().__class__.__name__ == "GainerDownloadYahoo"
    assert factory.get_processor().__class__.__name__ == "GainerProcessYahoo"

def test_factory_wsj():
    factory = GainerFactory("wsj")
    assert factory.get_downloader().__class__.__name__ == "GainerDownloadWSJ"
    assert factory.get_processor().__class__.__name__ == "GainerProcessWSJ"
