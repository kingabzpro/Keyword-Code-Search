import os


def search_codebase(directory: str, keywords: list, allowed_extensions: list) -> list:
    """
    Search for code snippets in the codebase that match any of the given keywords.
    Returns a list of dictionaries with file path, the line number where a match was found,
    and a code snippet that includes 2 lines of context before and after the matched line.
    """
    matches = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(allowed_extensions)):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                    for i, line in enumerate(lines):
                        # Check if any keyword is in the current line (case insensitive)
                        if any(keyword in line.lower() for keyword in keywords):
                            snippet = {
                                "file": file_path,
                                "line_number": i + 1,
                                "code": "".join(lines[max(0, i - 2) : i + 3]),
                            }
                            matches.append(snippet)
                except Exception as e:
                    print(f"Skipping file {file_path}: {e}")
    return matches
import os


def search_codebase(directory: str, keywords: list, allowed_extensions: list) -> list:
    """
    Search for code snippets in the codebase that match any of the given keywords.
    Returns a list of dictionaries with file path, the line number where a match was found,
    and a code snippet that includes 2 lines of context before and after the matched line.
    """
    matches = []

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(tuple(allowed_extensions)):
                file_path = os.path.join(root, file)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        lines = f.readlines()
                    for i, line in enumerate(lines):
                        # Check if any keyword is in the current line (case insensitive)
                        if any(keyword in line.lower() for keyword in keywords):
                            snippet = {
                                "file": file_path,
                                "line_number": i + 1,
                                "code": "".join(lines[max(0, i - 2) : i + 3]),
                            }
                            matches.append(snippet)
                except Exception as e:
                    print(f"Skipping file {file_path}: {e}")
    return matches
