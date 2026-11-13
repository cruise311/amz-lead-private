# Private Package License Notice

## ⚠️ This package contains PROPRIETARY code — NOT open source

The `amz-lead-lookup-private` package is **excluded from the MIT license** that covers the `amz-lead` open-source repository.

### Files affected (all files in this package):
- `tungee_runner.py`
- `tungee_unlock_api.py`
- `captcha_agent.py`
- `ocr_phone.py`
- `ocr_rapid.py`
- `backfill_excel.py`
- `build_batches.py`
- `tyc_lookup.py`
- `pinyin_resolve.py`

### License terms:
- **Commercial license required** for any use, modification, or distribution
- **Not permitted** to copy, modify, distribute, or sublicense without written agreement
- **Not permitted** to reverse engineer or derive implementations from the public interface
- Available only via commercial agreement: cloud@amz-lead.example.com

### Open-source components (MIT licensed, in `amz-lead` repo):
- `src/lookup/__init__.py` — Interface definitions (`ILookupProvider`, `CompanyInfo`, `PhoneResult`)
- `src/lookup/cli.py` — CLI entry point (uses interface only)
- `StubLookupProvider` — Test stub implementation

### OCR Stack Compliance:
This package uses **only Apache-2.0 / MIT licensed dependencies**:
- `rapidocr-onnxruntime` (Apache-2.0)
- `onnxruntime` (MIT)
- `opencv-python-headless` (Apache-2.0)
- No AGPL / LGPL / Copyleft dependencies

### Compliance:
If you received this code without a commercial license, you are in violation of copyright law. Please delete all files and contact us for licensing options.