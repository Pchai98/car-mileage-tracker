import os
from PIL import Image
from PIL.ExifTags import TAGS


def extract_exif_metadata(image_path):
    """
    Extracts EXIF metadata from a given image path.
    Returns a dictionary with relevant metadata.
    """
    if not os.path.exists(image_path):
        raise FileNotFoundError(f"File not found: {image_path}")

    image = Image.open(image_path)
    exif_data = image._getexif() 
    metadata = {}

    if exif_data is not None:
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            metadata[tag] = value
    else:
        raise ValueError("No EXIF metadata found.")

    return metadata


def get_photo_timestamp(image_path):
    metadata = extract_exif_metadata(image_path)
    if 'DateTime' in metadata:
        return metadata['DateTime']
    else:
        raise ValueError("No DateTime found in EXIF metadata.")


def get_camera_info(image_path):
    metadata = extract_exif_metadata(image_path)
    camera_info = {
        'Make': metadata.get('Make'),
        'Model': metadata.get('Model'),
        'Software': metadata.get('Software')
    }
    return camera_info

