1. small files with 5 directories (5M, 10bytes, 5 dir)
    - Generate data
        ```
        python3 data_gen.py -n 5 -f 1000000 -s 100 -d 1 -p /mnt/deepdir/data^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@ 20G ./
        root@localhost:/mnt/tinyfiles/data# du -sh --apparent-size 727M 
        ```
    - kopia
        ```
        root@localhost:~# kopia repository create filesystem --path /mnt/dst/kopia-repo
        root@localhost:~# kopia policy set --compression=gzip-best-compression --global
 
        root@localhost:~# command time kopia snapshot create /mnt/tinyfiles/data
        Snapshotting root@localhost:/mnt/tinyfiles/data ...
        * 0 hashing, 5000000 hashed (500 MB), 0 cached (0 B), uploaded 1.6 GB, estimated 500 MB (100.0%) 0s left   ^@@^@
        Created snapshot with root kc2e1a8d3010ce834465fe1beb76c289e and ID 5e28e6ce2146a8848baea6197f81cad9 in 8m22s
        ^@703.26user 286.55system 8:39.08elapsed 190%CPU (0avgtext+0avgdata 3490460maxresident)k
        43894248inputs+6934248outputs (112major+1320783minor)pagefaults 0swaps
        ```
    - restic 

        ```
        restic init --repo /mnt/dst/restic-repo
        restic cache --cleanup
        no old cache dirs found
 
        root@localhost:/# command time restic -r /mnt/dst/restic-repo backup create /mnt/tinyfiles/data --verbose
        create does not exist, skipping
        open repository
        enter password for repository:
        repository a0d1ca5e opened successfully, password is correct
        created new cache in /root/.cache/restic
        lock repository
        load index files
        no parent snapshot found, will read all files
        start scan on [/mnt/tinyfiles/data]
        start backup on [/mnt/tinyfiles/data]
        scan finished in 72.752s: 5000000 files, 476.837 MiB
 
        Files:       5000000 new,     0 changed,     0 unmodified
        Dirs:           13 new,     0 changed,     0 unmodified
        Data Blobs:  5000000 new
        Tree Blobs:     14 new
        Added to the repo: 2.233 GiB
 
        processed 5000000 files, 476.837 MiB in 7:43
        snapshot 2afba28b saved
        349.40user 205.16system 7:47.78elapsed 118%CPU (0avgtext+0avgdata 4975576maxresident)k
        43012304inputs+16723280outputs (1major+834701minor)pagefaults 0swaps
 
        root@localhost:/mnt/tinyfiles/bin# command time bupstash put --key backups.key --repository /mnt/dst/bupstash-repo /mnt/tinyfiles/data
        52aa330062f8a6ec0021205bc1ad3a04
        80.88user 144.99system 4:04.16elapsed 92%CPU (0avgtext+0avgdata 1278332maxresident)k
        39946104inputs+2611824outputs (1major+1533054minor)pagefaults 0swaps    
        ```
    -  Disk Usage
        ```
        root@localhost:/# du -sh /mnt/dst/kopia-repo
        1.9G    /mnt/dst/kopia-repo
        root@localhost:/# du -sh /mnt/dst/restic-repo
        3.2G    /mnt/dst/restic-repo 
        ```