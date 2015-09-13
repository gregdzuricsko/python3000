# source directory
sourceDir = ''
# destination directory name (on s3s)
destDir = ''
uploadFileNames = []

import boto
conn = boto.connect_s3()
b = conn.get_bucket('gregdzuricsko.pw')
from boto.s3.key import Key

# k.set_contents_from_string("testttttfoo")

import os
include = ('.js', '.html', '.txt', '.css')
exclude = set(['node_modules', 'jspm_packages', '__pycache__'])
for root, dirs, files in os.walk(".", topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude]
    for name in files:
        if('front' in root and name.lower().endswith(include)):
            uploadFileNames.append(os.path.join(root, name))#append, not extend, which will add individual characters(from the iterable c-array)

for fileName in uploadFileNames:
    print('uploading key of ' + fileName + ' to ', b)
    k = Key(b)
    k.key = fileName[1:].replace("\\","/")
    k.set_contents_from_filename(fileName)
