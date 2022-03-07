5. Large size files with all duplicate content  (100 file, 1000GB, 1 dir)
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
        * 0 hashing, 2 hashed (107.4 GB), 0 cached (0 B), uploaded 106.3 GB, estimated 107.4 GB (100.0%) 0s left
        Created snapshot with root kb04082b87acba37fe5fb9808a312830b and ID 13e01544d92651fc4b49315e9090e8a9 in 12m16s
        2718.61user 88.80system 12:16.60elapsed 381%CPU (0avgtext+0avgdata 334264maxresident)k
        209697024inputs+207704672outputs (17major+36166minor)pagefaults 0swaps
        ```
    - kopia
        ```
        kopia repository create filesystem --path /mnt/dst/kopia-repo -p 123 
        command time kopia snapshot create /mnt/src/data -p 123
        Snapshotting root@localhost:/mnt/src/data ...
        * 0 hashing, 2 hashed (107.4 GB), 0 cached (0 B), uploaded 59.8 GB, estimated 107.4 GB (100.0%) 0s left
        Created snapshot with root k09c96c2eed56de2bb7d57bcf4d08deb7 and ID b86b088f9e0d4c45548b29f3162717e0 in 5m19s
        Running full maintenance...
        Looking for active contents...
        Processed 3 contents, discovered 3...
        Looking for unreferenced contents...
        Rewriting contents from short packs...
        Not enough time has passed since previous successful Snapshot GC. Will try again next time.
        Skipping blob deletion because not enough time has passed yet (59m59s left).
        Cleaned up 0 logs.
        Cleaning up old index blobs which have already been compacted...
        Finished full maintenance.
        575.41user 62.31system 5:19.41elapsed 199%CPU (0avgtext+0avgdata 256736maxresident)k
        209700128inputs+116798928outputs (36major+57078minor)pagefaults 0swaps
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
        scan finished in 0.201s: 2 files, 100.000 GiB

        Files:           2 new,     0 changed,     0 unmodified
        Dirs:            3 new,     0 changed,     0 unmodified
        Data Blobs:  35009 new
        Tree Blobs:      4 new
        Added to the repo: 52.072 GiB

        processed 2 files, 100.000 GiB in 7:35
        snapshot c9bf4ab1 saved
        1379.68user 105.38system 7:35.56elapsed 325%CPU (0avgtext+0avgdata 187316maxresident)k
        209702968inputs+218529696outputs (25major+83599minor)pagefaults 0swaps
        ```
    -  Disk Usage
        ```
       root@localhost:~# du -sh /mnt/dst/kopia-repo
        56G	/mnt/dst/kopia-repo
        du -hs /mnt/dst/restic-repo
        53G	/mnt/dst/restic-repo
        du -hs /mnt/src/data
        100G   /mnt/src/data
        ```   