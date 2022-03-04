5. 1 T file with all random content  (1 file, 1TB, 1 dir)
    - Generate data
        ```
        dd if=/dev/zero  of=/mnt/src/data bs=1M count=1048576
        ```
    - kopia
        ```
        root@localhost:/mnt/dst# kopia repository create filesystem --path /mnt/dest/kopia-repo

        root@localhost:/mnt/dst# kopia policy set --compression=gzip-best-compression --global
 
        root@localhost:~# command time kopia snapshot create /mnt/src/
    
        Created snapshot with root ke843de9e14304dc9cc2887dd267da77d and ID ae0174632ef259c63a0f58e6e69da1e5 in 2h37m24s
        27530.40user 927.36system 2:37:24elapsed 301%CPU (0avgtext+0avgdata 365716maxresident)k
        2098691128inputs+2105422184outputs (45major+37223minor)pagefaults 0swaps
        ```
    - restic 

        ```
        root@localhost:~# restic init --repo /mnt/dest/restic-repo
        root@localhost:~# restic cache --cleanup
        no old cache dirs found
 
        root@localhost:~# command time restic -r /mnt/dest/restic-repo backup create /mnt/src --verbose
        create does not exist, skipping
        open repository
        lock repository
        load index files
        no parent snapshot found, will read all files
        start scan on [/mnt/src/]
        start backup on [/mnt/src/]
        scan finished in 0.202s: 11 files, 1003.543 GiB

        Files:          11 new,     0 changed,     0 unmodified
        Dirs:            2 new,     0 changed,     0 unmodified
        Data Blobs:  686415 new
        Tree Blobs:      3 new
        Added to the repo: 1003.592 GiB

        processed 11 files, 1003.543 GiB in 1:32:39
        snapshot 19b3f4aa saved
        16755.47user 1874.83system 1:32:40elapsed 335%CPU (0avgtext+0avgdata 545328maxresident)k
        2101627904inputs+4211674376outputs (95major+1136335minor)pagefaults 0swaps 
        ```
    -  Disk Usage
        ```
       root@localhost:~# du -sh /mnt/dest/kopia-repo
        1004G	/mnt/dest/kopia-repo
        root@localhost:~# du -sh /mnt/src/
        1004G	/mnt/src/
        root@localhost:~# du -sh /mnt/dest/restic-repo
        1005G	/mnt/dest/restic-repo
        ```