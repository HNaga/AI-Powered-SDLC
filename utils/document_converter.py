import os
from markdownify import markdownify

def html_to_markdown(html_content):
    """
    Convert HTML content to Markdown format
    
    Args:
        html_content (str): HTML content to convert
        
    Returns:
        str: Converted Markdown content
    """
    try:
        return markdownify(html_content)
    except Exception as e:
        raise Exception(f"Error converting HTML to Markdown: {str(e)}")

def convert_html_file_to_markdown(html_file_path):
    """
    Convert an HTML file to Markdown and return the content
    
    Args:
        html_file_path (str): Path to the HTML file
        
    Returns:
        str: Converted Markdown content
    """
    try:
        if not os.path.exists(html_file_path):
            raise FileNotFoundError(f"HTML file not found: {html_file_path}")
            
        with open(html_file_path, 'r', encoding='utf-8') as file:
            html_content = file.read()
            
        return html_to_markdown(html_content)
    except Exception as e:
        raise Exception(f"Error converting HTML file to Markdown: {str(e)}")