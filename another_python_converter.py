import os
import re
import shutil
import fnmatch

# --- CONFIGURATION ---
# IMPORTANT: Update these paths to match your folder structure.

# Directory where your markdown posts are located.
posts_dir = "/Users/patrickyang/CTF/writeups/bakayang-folder/bakayang/src/content/posts/umcs-finals-2025"

# Directory where your original Obsidian attachments are stored.
attachments_dir = "/Users/patrickyang/Documents/Obsidian/Rainbell/attachments"

# The destination for the images, relative to the posts directory.
# This script will create a folder named 'assets' inside the 'posts_dir'.
static_images_dir = os.path.join(posts_dir, "assets")

# --- SCRIPT LOGIC ---

def find_image_case_insensitive(image_name, search_dir):
    """
    Finds a file in a directory, ignoring case.
    Returns the full path to the file if found, otherwise None.
    """
    for root, _, files in os.walk(search_dir):
        for file in files:
            if fnmatch.fnmatch(file.lower(), image_name.lower()):
                return os.path.join(root, file)
    print(f"⚠️  Image not found in attachments: {image_name}")
    return None

def convert_wikilink_and_copy(match):
    """
    This function is called by re.sub for each wikilink found.
    It converts the wikilink to a standard Markdown link and copies the file.
    """
    original_wikilink = match.group(0)
    # .strip() handles potential whitespace around the filename
    image_name = match.group(1).strip()

    # --- Step 1: Handle the file copying ---
    image_source_path = find_image_case_insensitive(image_name, attachments_dir)

    if image_source_path:
        # Define the final destination for the image file
        image_dest_path = os.path.join(static_images_dir, image_name)
        
        # Ensure the destination directory exists
        os.makedirs(os.path.dirname(image_dest_path), exist_ok=True)
        
        try:
            print(f"    ↳ Copying '{image_name}' to '{static_images_dir}'")
            shutil.copy(image_source_path, image_dest_path)
        except Exception as e:
            print(f"❌ Error copying '{image_name}': {e}")
            # If copying fails, return the original text to avoid broken links.
            return original_wikilink
    else:
        # If the image isn't found in attachments, don't change the text.
        return original_wikilink

    # --- Step 2: Convert the wikilink to a standard Markdown link ---
    
    # Construct the new relative Markdown path.
    new_markdown_path = f'./assets/{image_name}'
    markdown_link = f"![]({new_markdown_path})"
    
    print(f"🔄 Converting '{original_wikilink}' to '{markdown_link}'")
    
    return markdown_link


def process_markdown_files():
    """
    Main function to loop through markdown files and process them.
    """
    print(f"🚀 Starting Wikilink-to-Markdown conversion and file copy in: {posts_dir}")
    
    # This regex finds Obsidian wikilinks, capturing the filename and ignoring dimensions.
    # It handles optional whitespace around the filename and the pipe character.
    wikilink_regex = re.compile(r'!\[\[\s*([^|\]]+?)\s*(?:\|.*?)?\]\]')

    for filename in os.listdir(posts_dir):
        if filename.endswith(".md"):
            filepath = os.path.join(posts_dir, filename)
            print(f"\n📄 Processing file: {filename}")

            try:
                with open(filepath, "r", encoding="utf-8") as file:
                    content = file.read()

                # Use re.sub with our replacer function to perform the conversion and copy
                updated_content = wikilink_regex.sub(convert_wikilink_and_copy, content)

                # Write the modified content back to the file if changes were made
                if updated_content != content:
                    with open(filepath, "w", encoding="utf-8") as file:
                        file.write(updated_content)
                    print(f"✅ Finished processing: {filename}")
                else:
                    print(f"No relevant wikilinks found in {filename}.")

            except Exception as e:
                print(f"❌ An unexpected error occurred with {filename}: {e}")
    
    print("\n\n🎉 All markdown files processed successfully.")

# --- RUN SCRIPT ---
if __name__ == "__main__":
    process_markdown_files()
