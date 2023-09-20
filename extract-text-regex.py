import os
import re

# Function to extract URLs from a string
def extract_urls_from_string(input_string):
    # Regular expression pattern to match URLs
    url_pattern = r'https?://\S+|www\.\S+'
    
    # Find all URLs in the input string using the regex pattern
    urls = re.findall(url_pattern, input_string)
    
    return urls

# Function to extract URLs from a file
def extract_urls_from_file(file_path):
    # Regular expression pattern to match URLs
    url_pattern = r'https?://\S+|www\.\S+'

    # Initialize an empty list to store the extracted URLs
    urls = []

    try:
        with open(file_path, 'rb') as file:  # Open the file in binary mode
            # Read the file line by line
            for line in file:
                # Decode each line with the appropriate encoding (e.g., 'utf-8' or 'latin-1')
                decoded_line = line.decode('utf-8', errors='ignore')  # Ignore decoding errors
                # Find all URLs in the line using the regex pattern
                found_urls = re.findall(url_pattern, decoded_line)
                urls.extend(found_urls)

        return urls

    except FileNotFoundError:
        return []

# Function to extract URLs from all files in a directory
def extract_urls_from_directory(directory_path):
    # Get a list of all files in the directory
    file_list = os.listdir(directory_path)

    # Initialize an empty list to store all extracted URLs from all files
    all_urls = []

    for file_name in file_list:
        file_path = os.path.join(directory_path, file_name)
        if os.path.isfile(file_path):
            extracted_urls = extract_urls_from_file(file_path)
            # Print the file name
            print(f"File: {file_name}")
            # Print the extracted URLs
            for url in extracted_urls:
                print(url)
            print()  # Add a blank line to separate URLs from different files

# Example usage:
directory_path = './'  # Replace with the path to your directory

# Extract URLs from all files in the directory
extract_urls_from_directory(directory_path)
