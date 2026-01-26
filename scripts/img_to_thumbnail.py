import argparse
import os
import sys
from PIL import Image

def create_linkedin_thumbnail(input_path, output_path=None, color=(255, 255, 255)):
    """
    Pads an image to exactly 1.91:1 aspect ratio (LinkedIn Standard) and resizes to 1200x627.
    """
    if not os.path.exists(input_path):
        print(f"❌ Error: File not found: {input_path}")
        sys.exit(1)

    try:
        img = Image.open(input_path)
        
        # Convert to RGB if it's RGBA (transparent) to avoid black backgrounds when saving as JPG
        if img.mode in ('RGBA', 'LA'):
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[-1])
            img = background
        elif img.mode != 'RGB':
            img = img.convert('RGB')

        # Target Dimensions
        target_ratio = 1.91
        current_ratio = img.width / img.height
        
        if current_ratio < target_ratio:
            # Too tall: Pad width
            new_width = int(img.height * target_ratio)
            new_height = img.height
            offset = ((new_width - img.width) // 2, 0)
        else:
            # Too wide: Pad height
            new_width = img.width
            new_height = int(img.width / target_ratio)
            offset = (0, (new_height - img.height) // 2)

        # Create canvas
        canvas = Image.new('RGB', (new_width, new_height), color)
        canvas.paste(img, offset)

        # Resize to optimal web standard
        final_thumb = canvas.resize((1200, 627), Image.Resampling.LANCZOS)
        
        # Generate output filename if not provided
        if output_path is None:
            base, _ = os.path.splitext(input_path)
            output_path = f"{base}_thumbnail.jpg"

        final_thumb.save(output_path, quality=95)
        print(f"✅ Success! Saved thumbnail to: {output_path}")

    except Exception as e:
        print(f"❌ Error: {e}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Create LinkedIn-optimized thumbnails (1200x627)")
    parser.add_argument("-i", "--input", help="Path to the input image")
    parser.add_argument("-o", "--output", help="Path to the output image (optional)")
    
    args = parser.parse_args()
    create_linkedin_thumbnail(args.input, args.output)
