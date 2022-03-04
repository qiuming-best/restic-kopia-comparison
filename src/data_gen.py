import os
import sys
import argparse
import math
from multiprocessing import Pool
from functools import partial

def create_files(args, i):
    path = os.path.join(args.path, 'my-dir-name-%d' % i)
    os.mkdir(path)
    recursive_files(args, path, 0)


def statitic(args):
    countdir = 0
    for k in range (args.depth):
        countdir += math.pow(args.depth, k)
    countfile = math.pow(args.depth, (args.depth - 1)) * args.filenum
    return countdir * args.dirnum, countfile * args.dirnum

def recursive_files(args, path, depth):
    depth += 1
    if depth == args.depth:
        for n in range (args.filenum):
            with open(os.path.join(path, 'my-random-file-%d.data' % n), 'wb') as f:
                f.write(os.urandom(args.filesize))
        return

    tmp = path
    for k in range (args.depth):
        path = os.path.join(tmp, '%d'% k)
        os.mkdir(path)
        recursive_files(args, path, depth)

def main(argv):
    parser = argparse.ArgumentParser(description='Create directories and files for backup test')
    parser.add_argument('-p', '--path', type=str, required=True, help='Path to the directory')
    parser.add_argument('-n', '--dirnum', type=int, required=True, help='Number of subdirectories')
    parser.add_argument('-f', '--filenum', type=int, required=True, help='Number of files per directory')
    parser.add_argument('-s', '--filesize', type=int, required=True, help='File size')
    parser.add_argument('-d', '--depth', type=int, required=True, help='Depth of directory')
    args = parser.parse_args()
    
    if os.path.exists(args.path):
        print('ERROR: destination directory %s already exists' % args.path, file=sys.stderr)
        return 1
    elif not os.path.exists(os.path.dirname(args.path)):
        print('ERROR: parent directory for destination %s does not exist' % args.path, file=sys.stderr)
        return 1
    
    countdir, countfile = statitic(args)
    print('total dirs %d will be created' % countdir)
    print('total files %d will be created' % countfile)

    os.mkdir(args.path)
    with Pool(min(args.dirnum, 8)) as p:
        p.map(partial(create_files, args), range(args.dirnum))


if __name__ == '__main__':
    sys.exit(main(sys.argv))