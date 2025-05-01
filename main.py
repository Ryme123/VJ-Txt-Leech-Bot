from utils import modify_link

if name == "main":
    # Example usage
    original_link = input("Enter the original link: ").strip()
    modified_link = modify_link(original_link)
    print("Modified Link:", modified_link)
