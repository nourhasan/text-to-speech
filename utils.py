# utils.py

def read_text_file(filepath):
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            return f.read().strip()
    except Exception as e:
        raise FileNotFoundError(f"Failed to read the file: {e}")
