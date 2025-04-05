import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
sys.path.append('.')

import pytest
##from bin.gainers.wsj import GainerDownloadWSJ, GainerProcessWSJ
from bin.gainers.wsj_gainers import GainerDownloadWSJ, GainerProcessWSJ

def test_wsj_downloader_exists():
    downloader = GainerDownloadWSJ()
    assert isinstance(downloader, GainerDownloadWSJ)

def test_wsj_processor_exists():
    processor = GainerProcessWSJ()
    assert isinstance(processor, GainerProcessWSJ)

def test_wsj_download_prints(capsys):
    downloader = GainerDownloadWSJ()
    downloader.download()
    captured = capsys.readouterr()
    assert "Downloading WSJ gainers" in captured.out

def test_wsj_normalize_prints(capsys):
    processor = GainerProcessWSJ()
    processor.normalize()
    captured = capsys.readouterr()
    assert "Normalizing WSJ gainers" in captured.out

def test_wsj_save_prints(capsys):
    processor = GainerProcessWSJ()
    processor.save_with_timestamp()
    captured = capsys.readouterr()
    assert "Saving WSJ gainers" in captured.out
