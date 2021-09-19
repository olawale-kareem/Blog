

def store_file(file):
    with open('file_storage/image.jpg', 'wb+') as dest:
        for chunk in file.chunks():
            dest.write(chunk)

