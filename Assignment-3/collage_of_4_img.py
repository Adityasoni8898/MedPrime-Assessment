from PIL import Image
import os

def create_collage(image_paths, output_file, output_format, resize_option):
    try:
        # loading images
        images = []
        for path in image_paths:
            if not os.path.exists(path):
                print("Error, file does not exist.")
                return
            try:
                img = Image.open(path)
                images.append(img)
            except Exception as e:
                print(f"Error, could not open image ({path}). Details: {e}")
                return

        # calculating the size for each cell
        min_width = min(img.width for img in images)
        min_height = min(img.height for img in images)

        # adjusting image sizes
        adjusted_images = []
        for img in images:
            if resize_option == "resize":
                # resizing image
                adjusted_images.append(img.resize((min_width, min_height)))
            elif resize_option == "crop":
                # croping algorithm
                img_aspect = img.width / img.height
                target_aspect = min_width / min_height
                if img_aspect > target_aspect:
                    new_width = int(img.height * target_aspect)
                    offset = (img.width - new_width) // 2
                    cropped_img = img.crop((offset, 0, offset + new_width, img.height))
                else:
                    new_height = int(img.width / target_aspect)
                    offset = (img.height - new_height) // 2
                    cropped_img = img.crop((0, offset, img.width, offset + new_height))
                
                adjusted_images.append(cropped_img.resize((min_width, min_height)))

        # creating a blank collage
        collage_width = 2 * min_width
        collage_height = 2 * min_height
        collage = Image.new('RGB', (collage_width, collage_height))

        # arranging images
        collage.paste(adjusted_images[0], (0, 0))
        collage.paste(adjusted_images[1], (min_width, 0))
        collage.paste(adjusted_images[2], (0, min_height))
        collage.paste(adjusted_images[3], (min_width, min_height))

        # converting the extension in lowercase
        output_format = output_format.lower()
        if output_format not in ['jpg', 'jpeg', 'png', 'bmp']:
            print(f"Error, unsupported output file format '{output_format}'. Use jpg, jpeg, png, or bmp.")
            return
        
        # converting jpg to jpeg for PIL
        if output_format == 'jpg':
            output_format = 'jpeg'

        output_file = f"{os.path.splitext(output_file)[0]}.{output_format}"
        collage.save(output_file, format=output_format.upper())
        print(f"Collage saved as '{output_file}'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    try:
        image_paths = []
        for i in range(4):
            path = input(f"Please enter the path for Image {i + 1}: ").strip()
            image_paths.append(path)

        # asking how to handle bigger images
        resize_option = None
        while resize_option not in ["resize", "crop"]:
            resize_option = input("Do you want to resize (may stretch) or crop the images? (resize/crop): ").strip().lower()

        output_format = input("Please specify the output file format (jpg, png, bmp): ").strip()
        output_file = "collage"

        # creating the collage
        create_collage(image_paths, output_file, output_format, resize_option)
    except KeyboardInterrupt:
        print("\nProcess interrupted by user.")