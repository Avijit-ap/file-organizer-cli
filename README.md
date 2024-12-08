 1. **Clone the repo:**

    ```bash
    git clone https://github.com/your-username/file-organizer-cli.git
    cd file-organizer-cli
    ```

2. **Create a virtual environment (recommended):**
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```


## Usage

```bash
python file_organizer.py <directory_path> [options] 
```


**Example:**

```bash
python file_organizer.py /path/to/your/files -t custom_types.json
```

## Configuration

The configuration file (e.g., `custom_types.json`) should be a JSON file with the following structure:

```json
{
  "image_extensions": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
  "document_extensions": [".pdf", ".doc", ".docx", ".txt", ".rtf"],
  "video_extensions": [".mp4", ".avi", ".mov", ".mkv"]
    // Add other categories as needed
}
