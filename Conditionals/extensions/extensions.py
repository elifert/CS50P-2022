def main():
    file_name = input()
    determine_file_extensions(file_name)


def determine_file_extensions(n):
    file_extensions = {
        ".gif" : "image/gif",
        ".jpg" :"image/jpeg",
        ".jpeg" : "image/jpeg",
        ".png" : "image/png",
        ".pdf" : "application/pdf",
        ".txt" : "text/plain",
        ".zip" : "application/zip"
    }

    file_extension = next((extension for extension in file_extensions if extension in n), None)
    if file_extension:
        print(file_extensions[file_extension])
    else:
        print("application/octet-stream")

main()