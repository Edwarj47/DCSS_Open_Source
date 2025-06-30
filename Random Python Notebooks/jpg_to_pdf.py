from PIL import Image
import glob
import os

# Update these paths
input_folder = r"YOUR FULL FILE PATH HERE"  # e.g., r"C:\Users\USER\OneDrive\Desktop\DCSS\DCSS_Open_Source_Git\Random Python Notebooks"
output_pdf = os.path.join(input_folder, "output.pdf")

try:
    # Find all .jpg files in the folder
    jpg_files = sorted(glob.glob(f"{input_folder}\\*.jpg"))

    if not jpg_files:
        raise Exception("No .jpg files found in the specified folder.")

    # Open images and convert to RGB
    images = [Image.open(f).convert("RGB") for f in jpg_files]

    # Save as PDF
    images[0].save(output_pdf, save_all=True, append_images=images[1:])
    print(f"Successfully combined {len(images)} images into {output_pdf}!")
except Exception as e:
    print(f"Error: {e}")