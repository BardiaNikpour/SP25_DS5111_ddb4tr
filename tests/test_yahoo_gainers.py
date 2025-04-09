import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append('.')

import pytest
##from bin.gainers.yahoo import GainerDownloadYahoo, GainerProcessYahoo
from bin.gainers.yahoo_gainers import GainerDownloadYahoo, GainerProcessYahoo

def test_yahoo_downloader_exists():
    downloader = GainerDownloadYahoo()
    assert isinstance(downloader, GainerDownloadYahoo)

def test_yahoo_processor_exists():
    processor = GainerProcessYahoo()
    assert isinstance(processor, GainerProcessYahoo)

def test_yahoo_download_prints(capsys):
    downloader = GainerDownloadYahoo()
    downloader.download()
    captured = capsys.readouterr()
    assert "Downloading Yahoo gainers" in captured.out

def test_yahoo_normalize_prints(capsys):
    processor = GainerProcessYahoo()
    processor.normalize()
    captured = capsys.readouterr()
    assert "Normalizing Yahoo gainers" in captured.out

def test_yahoo_save_prints(capsys):
    processor = GainerProcessYahoo()
    processor.save_with_timestamp()
    captured = capsys.readouterr()
    assert "Saving Yahoo gainers" in captured.out
