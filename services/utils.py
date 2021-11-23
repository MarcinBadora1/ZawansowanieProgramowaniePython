def read_file(path): #import pliku
    file = open(path, 'r+')
    data = file
    file.close()
    return data
