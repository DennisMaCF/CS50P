#([".gif", ".jpg", ".jpeg", '.png", ".pdf", ".txt", ".zip"
def main():
    filename = str(input("What's the file's name? \n")).strip().lower()
    media_type = find_type(filename)
    print(media_type)

def find_type(filename):
    extensions = {
        ".gif": "image/gif",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".png": "image/png",
        ".pdf": "application/pdf",
        ".txt": "text/plain",
        ".zip": "application/zip"
        }
    for media, media_type in extensions.items():
        if filename.endswith(media):
            return media_type
    return "application/octet-stream"

main()