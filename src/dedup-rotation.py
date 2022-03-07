from distutils.file_util import write_file
import os
import random

chunksize = 4096 #4kB
holes = 1000

def write_file(target, buf, start):
    with open(target, 'r+b') as fout:
        fout.seek(start)
        fout.write(buf)

def gen_file():   
    src = 'data0'
    filesize = os.path.getsize(src)
    for m in range (holes):
        write_start = random.randint(0, filesize - chunksize)
        print('%d start pos %d offset %d' % (m, write_start, chunksize))
        buf = os.urandom(chunksize)
        write_file(src, buf, write_start)

if __name__=="__main__":
    gen_file()