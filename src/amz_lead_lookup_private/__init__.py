# src/amz_lead_lookup_private/__init__.py
"""Private lookup implementations for amz-lead.

Commercial license required. Contact: cloud@amz-lead.example.com

This package is distributed via private PyPI (GitHub Packages).
Install with:
    pip install amz-lead-lookup-private --index-url https://pypi.pkg.github.com/cruise311/simple
"""

from __future__ import annotations

# Core implementations
from .tungee_runner import TungeeRunner
from .tungee_unlock_api import TungeeUnlockAPI
from .captcha_agent import CaptchaAgent
from .ocr_phone import OCRPhoneRecognizer, extract_phones_from_image as _extract_phones_vision
from .ocr_rapid import RapidOCREngine, extract_phones_from_image as _extract_phones_rapid
from .backfill_excel import ExcelBackfiller
from .build_batches import BatchBuilder
from .tyc_lookup import TycLookup
from .pinyin_resolve import PinyinResolver

# Unified OCR interface: auto-select best engine for platform
def extract_phones_from_image(image_path: str):
    """Auto-select OCR engine: macOS Vision (fastest) -> RapidOCR (Linux/Windows)."""
    import sys
    if sys.platform == "darwin":
        try:
            return _extract_phones_vision(image_path)
        except Exception:
            pass
    return _extract_phones_rapid(image_path)


__all__ = [
    "TungeeRunner",
    "TungeeUnlockAPI",
    "CaptchaAgent",
    "OCRPhoneRecognizer",
    "RapidOCREngine",
    "extract_phones_from_image",
    "ExcelBackfiller",
    "BatchBuilder",
    "TycLookup",
    "PinyinResolver",
]

__version__ = "0.1.0"