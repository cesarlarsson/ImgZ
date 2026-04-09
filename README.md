<div align="center">
  <img src="https://raw.githubusercontent.com/cesarlarsson/ImgZ/main/ImgZ.jpg" alt="ImgZ Logo" width="400"/>

  # ImgZ

  ### Fast and simple image compression from the command line

</div>

## 🎯 Project Goal
**ImgZ** is a robust and cross-platform Command Line Interface (CLI) utility that allows for bulk compression of JPG and PNG images. Designed to provide maximum ease of use across any operating system (Windows, macOS, Linux).

## ✨ Main Features
*   **Batch Processing:** Massive compression of `.jpg` and `.png` files within a selected folder.
*   **Data Separation:** Generates a dedicated output directory for compressed results, keeping the original source intact.
*   **Advanced Control (Configurable):** Allows adjusting critical parameters directly from the CLI:
    *   `--output-dir [PATH]`: Defines the output directory (default: `./compressed_images`).
    *   `--jpg-quality [1-100]`: Defines the desired JPEG compression quality (default: 85).
    *   `--max-dimension [PIXELS]`: Resizes images to limit their maximum size (width or height in pixels).

## 💻 Technology Stack
*   **Language:** Python 3.6+
*   **Key Libraries:** `Pillow` (PIL Fork) for image manipulation; `argparse` for robust CLI argument handling.
*   **Distribution:** Packaged as an installable package with `setup.py` to create the global command **`imgz`**.

## 📋 Prerequisites
*   Python 3.6 or higher
*   pip (Python package manager)

## 📦 Installation

### Option 1: Development Mode Installation (Recommended with venv)
```bash
# 1. Clone or navigate to the project directory
cd /path/to/project

# 2. Create and activate virtual environment
python -m venv venv
# On Windows:
venv\Scripts\activate
# On Linux/Mac:
source venv/bin/activate

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install package in development mode
pip install -e .
```

### Option 2: Standard Installation
```bash
# From the project directory
pip install .
```

## 🚀 Usage

### Basic Syntax
```bash
imgz [OPTIONS] <input_directory>
```

### Available Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `input_dir` | Required | - | Path to directory containing images to compress |
| `--output-dir` | Optional | `./compressed_images` | Directory where processed images will be saved |
| `--jpg-quality` | Optional | `85` | JPEG compression quality (1-100) |
| `--max-dimension` | Optional | `None` | Maximum dimension in pixels (width or height) |
| `--lang` | Optional | `es` | Output message language (es/en) |

### Usage Examples

**Example 1: Basic compression (default values)**
```bash
imgz ./my_photos
```
- Compresses all JPG/PNG images from `./my_photos`
- Saves them to `./compressed_images`
- Uses JPEG quality of 85
- Does not resize

**Example 2: Compression with custom quality**
```bash
imgz --jpg-quality 90 ./my_photos
```
- Compresses with JPEG quality of 90 (higher quality)

**Example 3: Compression with resizing**
```bash
imgz --max-dimension 1200 ./my_photos
```
- Resizes images so they don't exceed 1200px in any dimension
- Maintains aspect ratio

**Example 4: Full custom configuration**
```bash
imgz --output-dir ./web_ready --jpg-quality 80 --max-dimension 1920 ./original_photos
```
- Reads images from `./original_photos`
- Saves them to `./web_ready`
- Compresses JPG with quality 80
- Resizes to maximum 1920px

**Example 5: Use English messages**
```bash
imgz --lang en ./my_photos
```
- All output messages will be displayed in English

## 🏗️ Project Architecture

```
.
├── config.py             # Translations and multilanguage configuration
├── image_processor.py    # Compression logic and batch processing
├── cli.py                # Argument parsing and path validation
├── image_compressor.py   # Main entry point (executable)
├── setup.py              # Installation configuration
├── requirements.txt      # Project dependencies
├── .gitignore            # Files and folders excluded from Git
├── README.md             # Documentation in Spanish
└── README_EN.md          # Documentation in English
```

## 🔧 Development

### Modular Code Structure

**ImgZ** is designed with a clear modular architecture:

1. **`config.py`** (47 lines)
   - Multilanguage translation dictionary
   - Helper function `t()` for internationalization

2. **`image_processor.py`** (73 lines)
   - `compress_image()`: Processes an individual image
   - `process_batch()`: Coordinates batch processing
   - Compression and resizing logic

3. **`cli.py`** (77 lines)
   - `parse_arguments()`: CLI argument parsing
   - `validate_and_setup_paths()`: Directory validation and setup
   - `run()`: Main execution function

4. **`image_compressor.py`** (10 lines)
   - Main program entry point

### Running in Development Mode
```bash
# Run directly without installation
python image_compressor.py --jpg-quality 85 ./my_photos
```

## 📄 License
This project is open source and available for free use.

---

