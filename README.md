# Automatic Stamp Machine for PDF

An automated tool designed to streamline the process of applying digital stamps or signatures to multiple PDF documents simultaneously. This tool helps eliminate the repetitive task of manually placing stamps on every page or every file.

## 🚀 Features

* **Batch Processing:** Apply stamps to multiple PDF files in a single run.
* **Precise Positioning:** Define specific coordinates (X, Y) for stamp placement.
* **Page Selection:** Choose to stamp all pages, only the first page, or specific page ranges.
* **Transparency Support:** Supports PNG images with transparency for a professional "wet stamp" look.
* **Scaling & Rotation:** Easily adjust the size and orientation of the stamp image.

## 🛠️ Installation

1.  **Clone the Repository:**
    ```bash
    git clone [https://github.com/kang851216/Automatic-Stamp-Machine-for-PDF.git](https://github.com/kang851216/Automatic-Stamp-Machine-for-PDF.git)
    cd Automatic-Stamp-Machine-for-PDF
    ```

## 📋 Prerequisites

* Python 3.x
* `PyMuPDF` (fitz) or `ReportLab` (depending on the specific implementation used in the source code)

## 📖 Usage

1.  Prepare your source PDF files.
2.  Prepare your stamp image.
3.  Configure the coordinates and settings in the script or configuration file.
4.  Run the application:
    ```bash
    python Automatic Stamp Machine for PDF.py
    ```
5.  Simply UI windown will be appeared.
6.  Find your stamp image.
7.  Find your target PDF document.
8.  Click "Merge" and save the result.pdf in same directory of this code.

## ⚙️ Configuration

You can adjust the following parameters within the script:
* `STAMP_IMG`: Path to your stamp image.
* `COORDINATES`: (x, y) position on the PDF page.
* `SCALE`: Resizing factor for the stamp.
* `PAGES`: Specify which pages to apply the stamp to.
