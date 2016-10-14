from tarfile import TarFile
from zipfile import ZipFile

path = 'g:/geek/'

for i in range(0, 300)[::-1]:
    extract_path = path + str(i)
    #put_path =path +str(i + 1)
    file = open(extract_path, 'rb')
    strr = file.read()
    try:
        if "\x50\x4B\x03\x04" in strr:
            tar = ZipFile(extract_path)
            tar.extract(str(i - 1), path)
            tar.close()
            file.close()
        elif "\x1F\x8B\x08" in strr:
            tar = TarFile.gzopen(extract_path)
            tar.extract(str(i - 1), path)
            tar.close()
            file.close()
        elif "\x42\x5A\x68\x39" in strr:
            tar = TarFile.bz2open(extract_path)
            tar.extract(str(i - 1), path)
            tar.close()
            file.close()
        file.close()
    except:
        print "something error!"
