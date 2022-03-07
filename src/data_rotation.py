from distutils.file_util import write_file
import os
import random

maxround = 9
chunksize = 4096 #4kB
filesize = 10737418240 #10GB
filescount = 10

contents_dict = {}

def init_4k_contents():
    global contents_dict
    for i in range(10):
        contents_dict[i] = ''.join(str(i) for x in range(chunksize))

def wirte_init_files():
    chunks = int (filesize / chunksize)
    for i in range(filescount):
        target = 'data'+str(i)
        for j in range (chunks):
            index = random.randint(0, 9)
            with open(target, 'a') as f:
                f.write(contents_dict[index])

def align_file(src):
    cursize = os.path.getsize(src)
    if os.stat(src).st_size < filesize :
        sumbytes = filesize - cursize
        with open(src,'a') as f:
            tmp = 'data'+str(random.randint(0, filescount-1))
            start_pos = random.randint(0, filesize - sumbytes)
            buf = seek_file(tmp, start_pos, sumbytes)
            f.write(buf)
        print('file %s align %d bytes'% src, sumbytes)

def seek_file(src, start, offset):
    with open(src, 'rb') as fin:
        fin.seek(start)
        if start + offset > filesize:
            first = filesize - start  
            rest = offset - first
            buf = fin.read(first)
            fin.seek(0)
            buf += fin.read(rest)
            return buf
        else :
            buf = fin.read(offset)
        return buf

def write_file(target, buf, start):
    with open(target, 'ab', ) as fout:
        fout.seek(start)
        fout.write(buf)

def get_offset(filesize, totalfiles):
    return int (filesize/ totalfiles)

def align_file(src):
    cursize = os.path.getsize(src)
    if os.stat(src).st_size < filesize :
        sumbytes = filesize - cursize
        with open(src,'a') as f:
            #f.write(os.urandom(sumbytes))
            f.write(''.join(str(0) for x in range(sumbytes)))

def gen_file():   
    for k in range (maxround): 
        write_start = 0
        cur = (k + 1)* filescount
        offset = get_offset(filesize, cur)
        for l in range (filescount):
            read_start = random.randint(1, filesize - 1)
            dst = 'data'+str(cur + l)
            for i in range (cur):
                src = 'data'+str(i)
                buf = seek_file(src, read_start, offset)
                write_file(dst, buf, write_start)
                read_start = (read_start + offset) % filesize
                write_start += offset
            align_file(dst)
    


if __name__=="__main__":
    init_4k_contents()
    wirte_init_files()
    gen_file()