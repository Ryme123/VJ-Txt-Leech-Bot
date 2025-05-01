def modify_link(original_link):
    """
    Prepends a specific URL to the given link.

    Args:
        original_link (str): The original URL to be modified.

    Returns:
        str: The modified URL.
    """
    base_url = "https://api.extractor.workers.dev/player?url="
    return base_url + original_link
