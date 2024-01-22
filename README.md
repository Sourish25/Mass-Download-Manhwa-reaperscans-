---

# Mass Download Manhwa

## Introduction
Mass Download Manhwa is a Python script designed to simplify the process of downloading manhwa chapters, compiling them into PDFs, and facilitating offline reading. Developed by Sourish, this project aims to provide an easy, organized, and portable solution for manga enthusiasts.

## Getting Started

### Prerequisites
Before running the script, ensure you have the following dependencies installed:

```bash
pip install requests
pip install beautifulsoup4
pip install img2pdf
```

### Usage
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Sourish25/Mass-Download-Manhwa-reaperscans-.git
   cd MassDownloadManhwa
   ```

2. **Run the Script:**
   Replace `base_url`, `start_range`, and `end_range` with your desired manhwa details.

   ```python
   python download_chapters.py
   ```

## Understanding the Code

### 1. Downloading Images
The script iterates through chapters, attempting to download images until an error (404) is encountered. Images are saved in chapter-specific folders.

### 2. Creating PDFs
Once images are downloaded, they are compiled into a PDF for each chapter using `img2pdf`. The resulting PDFs are stored in chapter-specific folders.

### 3. Folder Organization
To maintain a clean structure, the script organizes PDFs into an overall folder named after the range of chapters, e.g., "chapter_1-5".

### 4. Image Cleanup
After PDF creation, the script deletes the individual images, keeping only the consolidated PDFs.

## Contributing
Contributions are welcome! Fork the repository, make your changes, and submit a pull request.

## Issues
If you encounter any issues or have suggestions for improvements, please open an issue on the GitHub repository.

## Acknowledgments
Thanks to the open-source community for their valuable contributions.

---
