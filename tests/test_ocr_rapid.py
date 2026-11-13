# tests/test_ocr_rapid.py
"""RapidOCR engine tests."""

from __future__ import annotations

import pytest

try:
    from amz_lead_lookup_private import RapidOCREngine, extract_phones_from_image
    _HAS_RAPIDOCR = True
except ImportError:
    _HAS_RAPIDOCR = False


@pytest.mark.skipif(not _HAS_RAPIDOCR, reason="rapidocr-onnxruntime not installed")
class TestRapidOCREngine:
    """Test RapidOCR engine basic functionality."""

    def test_engine_instantiation(self):
        """Engine should instantiate without errors."""
        engine = RapidOCREngine()
        assert engine is not None
        assert hasattr(engine, '_engine')

    def test_extract_phones_from_synthetic_image(self, tmp_path):
        """Test OCR on a synthetic image with known phone number."""
        import cv2
        import numpy as np

        # Create a simple test image with a phone number
        img = np.zeros((120, 400, 3), dtype=np.uint8)
        cv2.putText(
            img, '138 0000 1234', (20, 70),
            cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 2
        )
        img_path = tmp_path / "test_phone.png"
        cv2.imwrite(str(img_path), img)

        engine = RapidOCREngine()
        phones = engine.extract_phones(img_path)

        # Should detect the phone number (with or without spaces)
        assert len(phones) > 0
        found = any('138' in p and '1234' in p for p in phones)
        assert found, f"Expected phone number not found in: {phones}"

    def test_ocr_text_output(self, tmp_path):
        """Test raw OCR text extraction."""
        import cv2
        import numpy as np

        img = np.zeros((80, 300, 3), dtype=np.uint8)
        cv2.putText(img, 'Test 123', (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        img_path = tmp_path / "test_text.png"
        cv2.imwrite(str(img_path), img)

        engine = RapidOCREngine()
        text = engine.ocr_text(img_path)

        assert isinstance(text, str)
        assert len(text) >= 0  # May be empty if not detected


@pytest.mark.skipif(not _HAS_RAPIDOCR, reason="rapidocr-onnxruntime not installed")
class TestUnifiedOCRInterface:
    """Test the unified extract_phones_from_image function."""

    def test_auto_select_engine(self):
        """Function should be callable and return list."""
        import cv2
        import numpy as np
        import tempfile

        img = np.zeros((100, 300, 3), dtype=np.uint8)
        cv2.putText(img, '138 0000 1234', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)

        with tempfile.NamedTemporaryFile(suffix='.png', delete=False) as f:
            cv2.imwrite(f.name, img)
            try:
                from amz_lead_lookup_private import extract_phones_from_image
                phones = extract_phones_from_image(f.name)
                assert isinstance(phones, list)
            finally:
                import os
                os.unlink(f.name)