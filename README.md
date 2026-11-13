# amz-lead-lookup-private

> **私有包 — 需商业授权**

`amz-lead` 开源框架的**闭源补号实现**，包含：
- 探迹批量登录、解锁、验证码自愈
- RapidOCR 号码识别（Apache-2.0，Linux/Windows/macOS 通用）
- macOS Vision + Tesseract 兜底（仅 macOS）
- Excel 回填、四色标记、外呼工单分批
- 天眼查兜底查询、拼音辅助还原

## 安装

### 前置条件
- 商业授权（联系：cloud@amz-lead.example.com）
- GitHub 账号有 `cruise311/amz-lead-private` 仓库的 `read:packages` 权限

### 配置 GitHub Packages 认证

```bash
# 1. 生成 Personal Access Token (Classic)
# GitHub Settings -> Developer settings -> Personal access tokens -> Generate new token
# 勾选: read:packages, write:packages (仅发布时需要)

# 2. 配置 ~/.pypirc
cat > ~/.pypirc << 'EOF'
[distutils]
index-servers = github
[github]
repository = https://pypi.pkg.github.com/cruise311
username = YOUR_GITHUB_USERNAME
password = ghp_xxxxxxxxxxxx  # 你的 PAT
EOF

# 3. 或使用环境变量 (CI 推荐)
export PIP_INDEX_URL=https://pypi.pkg.github.com/cruise311/simple
export PIP_EXTRA_INDEX_URL=https://pypi.org/simple
export GITHUB_TOKEN=ghp_xxxxxxxxxxxx
```

### 安装命令

```bash
# 开发环境（配合 amz-lead 开源版）
pip install "amz-lead[dev,lookup-private]" \
    --index-url https://pypi.pkg.github.com/cruise311/simple \
    --extra-index-url https://pypi.org/simple

# 生产环境
pip install "amz-lead[lookup-private]" \
    --index-url https://pypi.pkg.github.com/cruise311/simple
```

## 使用方式

```python
# 在 amz-lead 中自动检测并使用私有实现
from amz_lead.lookup import ILookupProvider

# 私有包安装后，amz_lead.lookup.cli 会自动导入 TungeeRunner 等实现
# 无需修改业务代码，仅需：
amz-lookup --input leads.csv --output enriched.csv --provider tungee

# 或直接使用
from amz_lead_lookup_private import TungeeRunner, RapidOCREngine

runner = TungeeRunner(settings)
results = runner.lookup_batch(companies)

engine = RapidOCREngine()
phones = engine.extract_phones("screenshot.png")
```

## 核心类

| 类 | 说明 |
|---|---|
| `TungeeRunner` | 探迹批量跑批主流程（登录、解锁、验证码、OCR、回填） |
| `TungeeUnlockAPI` | 探迹解锁接口封装（请求构造、签名、重试） |
| `CaptchaAgent` | 验证码自愈（滑块、点选、图标识别） |
| `RapidOCREngine` | RapidOCR 封装（Apache-2.0，Linux/Windows/macOS） |
| `OCRPhoneRecognizer` | macOS Vision + Tesseract 兜底（仅 macOS） |
| `extract_phones_from_image` | 统一入口：macOS 优先 Vision，其他平台 RapidOCR |
| `ExcelBackfiller` | 结果回填 Excel、四色标记（绿/黄/红/灰） |
| `BatchBuilder` | 外呼工单分批、去重、优先级排序 |
| `TycLookup` | 天眼查兜底查询 |
| `PinyinResolver` | 拼音辅助还原 |

## OCR 栈合规说明

| 引擎 | 文件 | 平台 | 许可证 | 依赖 |
|---|---|---|---|---|
| macOS Vision | `ocr_phone.py` | macOS 10.15+ | Apple 系统 | 系统内置 |
| RapidOCR | `ocr_rapid.py` | Linux/Windows/macOS | **Apache-2.0** | `rapidocr-onnxruntime` + `onnxruntime` + `opencv-python-headless` |

**无 AGPL / LGPL 依赖**，可安全用于商业闭源产品。

## 开发

```bash
# 安装开发依赖
pip install -e ".[dev]"

# 运行测试
pytest tests/ -v

# 代码检查
ruff check src/
ruff format src/
mypy src/
```

## 发布（仅维护者）

```bash
# 1. 更新版本号
# pyproject.toml version = "0.1.1"

# 2. 构建
pip install build twine
python -m build

# 3. 发布到 GitHub Packages
twine upload --repository github dist/*
# 需要 ~/.pypirc 配置 github 仓库和 PAT (write:packages)
```

## 许可证

**Proprietary / Commercial License Required**

- 禁止复制、修改、分发、反向工程
- 仅限授权方内部使用
- 详见 `LICENSE-PRIVATE.md`

---

*Package: `amz-lead-lookup-private` | Version: 0.1.0 | Author: cruise311*