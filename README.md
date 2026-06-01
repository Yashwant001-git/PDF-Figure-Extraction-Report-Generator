# PDF Figure Extraction & Report Generator

## Overview

PDF Figure Extraction & Report Generator is a Python-based document intelligence tool that automatically extracts figures from PDF documents, identifies their captions, matches figures with captions, and generates a structured report.

The project is designed to work with:

* Research Papers (IEEE, Springer, ACM, etc.)
* Technical Reports
* Project Documentation
* Presentation PDFs

---

## Features

### Figure Extraction

* Extracts embedded images from PDF documents.
* Filters small and irrelevant images.
* Supports multiple images per page.

### Caption Extraction

* Detects figure captions using regular expressions.
* Supports patterns such as:

  * Figure 1:
  * Figure 2.
  * Fig. 3

### Figure-Caption Matching

* Matches extracted figures with captions using page-based matching.
* Creates structured figure records.

### Report Generation

* Generates a DOCX report.
* Includes:

  * Figure captions
  * Page numbers
  * Extracted images
  * Summary table

### PDF Organization

* Stores outputs for each PDF in separate folders.
* Keeps figures, metadata, and reports organized.

---

## Project Structure

```text
pdf_figure_extractor/
│
├── app.py
│
├── src/
│   ├── image_extractor.py
│   ├── caption_extractor.py
│   ├── figure_matcher.py
│   └── report_generator.py
│
├── data/
│   ├── uploads/
│   ├── figures/
│   └── reports/
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

## Installation

### Clone Repository

```bash
git clone <repository-url>
cd pdf_figure_extractor
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

Linux/Mac:

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

### Place PDF

Copy the PDF into:

```text
data/uploads/
```

### Run Application

```bash
python app.py
```

### Output

The application will:

1. Extract figures from the PDF.
2. Extract figure captions.
3. Match figures with captions.
4. Generate a report.

Generated outputs:

```text
data/
│
├── figures/
│   ├── page_1_img_1.png
│   ├── page_2_img_1.png
│   └── ...
│
└── reports/
    └── figure_report.docx
```

---

## Workflow

```text
PDF
 │
 ▼
Figure Extraction
 │
 ▼
Caption Extraction
 │
 ▼
Figure-Caption Matching
 │
 ▼
Report Generation
 │
 ▼
DOCX Report
```

---

## Technologies Used

* Python
* PyMuPDF
* Pillow
* python-docx
* Regular Expressions (Regex)

---

## Current Limitations

* Matching is currently page-based.
* Some captions may not be detected in complex layouts.
* Multi-column PDFs may require additional processing.
* Tables are not yet extracted.

---

## Future Enhancements

* Streamlit Dashboard
* AI-powered Figure Summaries
* Figure Classification
* Table Extraction
* Coordinate-based Figure-Caption Matching
* Figure Search Engine
* PDF Metadata Dashboard

---

## Example Use Cases

* Research Paper Analysis
* Technical Documentation Processing
* Academic Project Reports
* Automated Figure Catalog Generation

---

## Author

Developed as a document intelligence and PDF processing project using Python.
