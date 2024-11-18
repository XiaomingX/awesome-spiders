import re
import requests

def extract_links_from_markdown(markdown_content):
    """
    Extract all URLs from the given Markdown content.
    """
    link_pattern = r'\[.*?\]\((http[s]?://.*?)\)'
    return re.findall(link_pattern, markdown_content)

def check_url_status(url):
    """
    Check if a URL is valid (not 404 or 403).
    """
    try:
        response = requests.head(url, allow_redirects=True, timeout=5)
        if response.status_code in [403, 404]:
            return False
        return True
    except requests.RequestException:
        return False

def main():
    # Load your markdown file content
    markdown_file = "README.md"  # Replace with your markdown file name
    with open(markdown_file, "r", encoding="utf-8") as file:
        markdown_content = file.read()

    # Extract links
    links = extract_links_from_markdown(markdown_content)
    if not links:
        print("No links found in the Markdown file.")
        return

    # Check each link
    print("Checking links...")
    for url in links:
        if not check_url_status(url):
            print(f"❌ Link is not accessible: {url}")
        else:
            print(f"✅ Link is valid: {url}")

if __name__ == "__main__":
    main()
