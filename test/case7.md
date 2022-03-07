7: Large size files with duplicate content (100 files, 1000GB, 1 dir, compressible data)
    - Generate data
        ```
        pthon3 data_rotation.py
        ```
    - kopia (compress)
        ```
        kopia repository create filesystem --path /mnt/dst/kopia-repo -p 123 
        kopia policy set --compression=gzip-best-compression --global
        command time kopia snapshot create /mnt/src/data -p 123
        Snapshotting root@localhost:/mnt/src/data ...
        * 0 hashing, 103 hashed (1.1 TB), 0 cached (0 B), uploaded 1.6 GB, estimated 1.1 TB (100.0%) 0s left
        Created snapshot with root k9a60d9078646306f44ab97c713c5581f and ID 8dfc76d2eb9f2f272b18234572a02599 in 1h2m27s
        12154.08user 310.54system 1:02:27elapsed 332%CPU (0avgtext+0avgdata 206240maxresident)k
        2092467368inputs+3598832outputs (9major+61615minor)pagefaults 0swaps
        ```
    - kopia
        ```
        kopia repository create filesystem --path /mnt/dst/kopia-repo -p 123 
        command time kopia snapshot create /mnt/src/data -p 123
        Snapshotting root@localhost:/mnt/src/data ...
        * 0 hashing, 103 hashed (1.1 TB), 0 cached (0 B), uploaded 1.1 TB, estimated 1.1 TB (100.0%) 0s left
        Created snapshot with root k608a1b40f773bc8e384607d053784f5b and ID b16c136d1281ed4e1847b83c345c3cd0 in 25m51s
        Running full maintenance...
        Looking for active contents...
        Processed 44 contents, discovered 104...
        Processed 85 contents, discovered 104...
        Processed 104 contents, discovered 104...
        Looking for unreferenced contents...
        Rewriting contents from short packs...
        Not enough time has passed since previous successful Snapshot GC. Will try again next time.
        Skipping blob deletion because not enough time has passed yet (59m59s left).
        Cleaned up 0 logs.
        Cleaning up old index blobs which have already been compacted...
        Finished full maintenance.
        2220.26user 973.54system 25:56.41elapsed 205%CPU (0avgtext+0avgdata 470200maxresident)k
        2092137832inputs+2098991864outputs (117major+119992minor)pagefaults 0swaps
        ```
    - restic 

        ```
        restic init --repo /mnt/dst/restic-repo
        restic cache --cleanup
        no old cache dirs found
 
        root@localhost:~# command time restic -r /mnt/dest/restic-repo backup create does not exist, skipping
        open repository
        lock repository
        load index files
        no parent snapshot found, will read all files
        start scan on [/mnt/src/data]
        start backup on [/mnt/src/data]
        scan finished in 0.202s: 103 files, 1000.000 GiB

        Files:         103 new,     0 changed,     0 unmodified
        Dirs:            3 new,     0 changed,     0 unmodified
        Data Blobs:  128003 new
        Tree Blobs:      4 new
        Added to the repo: 1000.008 GiB

        processed 103 files, 1000.000 GiB in 1:35:34
        snapshot 89cb1f06 saved
        17399.09user 1859.44system 1:35:35elapsed 335%CPU (0avgtext+0avgdata 250308maxresident)k
        2092541488inputs+4196508488outputs (93major+1334259minor)pagefaults 0swaps
        ```
    -  Disk Usage
        ```
       root@localhost:~# du -sh /mnt/dst/kopia-repo
        1.6G	/mnt/dst/kopia-repo
        du -hs /mnt/dst/restic-repo
        1001G	/mnt/dst/restic-repo
        du -hs /mnt/src
        1001G   /mnt/src
        ```   