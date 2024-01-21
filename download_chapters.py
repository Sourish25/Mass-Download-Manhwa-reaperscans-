import os
import requests
from PIL import Image
from img2pdf import convert
import shutil

def download_and_create_pdfs(base_url, start, end):
    overall_folder_name = f"downloaded_chapters/chapter_{start}-{end}"
    os.makedirs(overall_folder_name, exist_ok=True)

    for chapter_number in range(start, end+1):
        chapter_url = f"{base_url}{chapter_number}/"
        images = []

        image_number = 1
        while True:
            image_url = f"{chapter_url}image_{image_number}.jpg"

            try:
                response = requests.get(image_url)
                response.raise_for_status()
            except requests.exceptions.RequestException as e:
                # If an error occurs, break the loop
                print(f"Error downloading image {image_number} for Chapter {chapter_number}: {e}")
                break

            image_path = os.path.join(overall_folder_name, f"image_{image_number}.jpg")
            with open(image_path, "wb") as image_file:
                image_file.write(response.content)
            
            images.append(image_path)
            image_number += 1

        # Create PDF from downloaded images
        pdf_output_path = f"{overall_folder_name}/chapter_{chapter_number}.pdf"
        create_pdf(images, pdf_output_path)

        # Delete images after creating PDF
        for image_path in images:
            os.remove(image_path)

        print(f"Downloaded, created PDF, and deleted images for Chapter {chapter_number}")

    # Clean up residue folders
    for chapter_folder in os.listdir(overall_folder_name):
        chapter_folder_path = os.path.join(overall_folder_name, chapter_folder)
        if os.path.isdir(chapter_folder_path):
            shutil.rmtree(chapter_folder_path)

def create_pdf(images, output_path):
    if images:
        with open(output_path, "wb") as pdf_file:
            pdf_file.write(convert(images))
    else:
        print("No images to convert to PDF.")

# Replace this value with your actual base URL and the range of chapters you want to download
base_url = "https://s22.asuracomics.me/s1/scans/Omniscient%20Readers%20Viewpoint/"
start_range = 1
end_range = 5  # Adjust the end range as needed

download_and_create_pdfs(base_url, start_range, end_range)
