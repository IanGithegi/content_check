# List All files within a folder. To much a certain criteria
import os
path = ('./test_folder/')


def content_count(path):
    print("----------Show Files and count on Each directory")
    for r, d, files in os.walk(path):
        print (d)
        print(files)


content_count(path)
