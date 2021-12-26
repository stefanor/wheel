from __future__ import annotations

import base64
import logging

log = logging.getLogger('wheel')

# ensure Python logging is configured
try:
    __import__('setuptools.logging')
except ImportError:
    # setuptools < ??
    from . import _setuptools_logging
    _setuptools_logging.configure()


def urlsafe_b64encode(data: bytes) -> bytes:
    """urlsafe_b64encode without padding"""
    return base64.urlsafe_b64encode(data).rstrip(b"=")


def urlsafe_b64decode(data: bytes) -> bytes:
    """urlsafe_b64decode without padding"""
    pad = b"=" * (4 - (len(data) & 3))
    return base64.urlsafe_b64decode(data + pad)
