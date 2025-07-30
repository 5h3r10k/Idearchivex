import requests
from bs4 import BeautifulSoup
import os

'''
Takes a webpage with pdf download links and downloads all the pdfs to a specified directory.
'''

# URL of the page with PDF links
page_url = 'https://inst.eecs.berkeley.edu/~cs188/fa24/assets/discussions/'  # Replace with your URL

# Directory to save downloaded PDFs
download_directory = './files'  # Specify your directory

def download_pdfs_from_page(page_url, download_dir):
    # Create the download directory if it doesn't exist
    os.makedirs(download_dir, exist_ok=True)
    
    try:
        # Send a GET request to the page
        response = requests.get(page_url)
        response.raise_for_status()  # Raise an error for bad responses

        # Parse the page content
        soup = BeautifulSoup(response.content, 'html.parser')

        # Find all links ending with .pdf
        pdf_links = [a['href'] for a in soup.find_all('a', href=True) if a['href'].endswith('.pdf')]
        
        # Download each PDF
        for pdf_url in pdf_links:
            # Handle relative URLs
            if not pdf_url.startswith('http'):
                pdf_url = requests.compat.urljoin(page_url, pdf_url)
            
            # Get the filename from the URL
            filename = os.path.join(download_dir, pdf_url.split('/')[-1])
            
            # Download the PDF
            pdf_response = requests.get(pdf_url)
            pdf_response.raise_for_status()
            
            # Write the content to a file
            with open(filename, 'wb') as f:
                f.write(pdf_response.content)
            print(f'Downloaded: {filename}')
    
    except requests.exceptions.RequestException as e:
        print(f'Failed to retrieve the page: {e}')

# Call the function
download_pdfs_from_page(page_url, download_directory)