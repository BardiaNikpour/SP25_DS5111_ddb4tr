import platform
import sys
import pytest

ALLOWED_OSES = ['linux', 'darwin']
ALLOWED_PYTHON_VERSIONS = [(3, 10), (3, 11), (3, 12)]

def test_os_is_acceptable():
    os_name = platform.system().lower()
    assert os_name in ALLOWED_OSES, f"Expected OS in {ALLOWED_OSES}, but got: {os_name}"

def test_python_version():
    version = (sys.version_info.major, sys.version_info.minor)
    assert version in ALLOWED_PYTHON_VERSIONS, f"Python version must be one of {ALLOWED_PYTHON_VERSIONS}, got {version[0]}.{version[1]}"
