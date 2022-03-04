4. 1 T file with all zero content  (1 file, 1TB, 1 dir)
    - Generate data
        ```
        dd if=/dev/zero  of=/mnt/src/data bs=1M count=1048576
        ```
    - kopia
        ```
        kopia repository create filesystem --path /mnt/dst/kopia-repo
        kopia policy set --global --ignore-cache-dirs false
        Setting policy for (global)
        - setting "ignore cache dirs" to false.
        Running full maintenance...
        Looking for active contents...
        Processed 0 contents, discovered 0...
        Looking for unreferenced contents...
        Rewriting contents from short packs...
        Not enough time has passed since previous successful Snapshot GC. Will try again next time.
        Skipping blob deletion because not enough time has passed yet (59m59s left).
        Cleaned up 0 logs.
        Cleaning up old index blobs which have already been compacted...
        Finished full maintenance.

        root@localhost:~# kopia policy set --compression=gzip-best-compression --global
        
        command time kopia snapshot create /mnt/src/
        Snapshotting root@localhost:/mnt/src/data ...
        * 0 hashing, 1 hashed (1.1 TB), 0 cached (0 B), uploaded 23.6 MB, estimated 1.1 TB (100.0%) 0s left
        Created snapshot with root IIx90e0a1dbf8508ffbfdd5d92c56eeb85a and ID 2b2dcf207c8f596084d7c954b7915a66 in 18m25s
        1530.89user 294.49system 18:25.57elapsed 165%CPU (0avgtext+0avgdata 226684maxresident)k
        2147487360inputs+196016outputs (24major+40490minor)pagefaults 0swaps
        ```
    - restic 

        ```
        restic init --repo /mnt/dst/restic-repo
        restic cache --cleanup
        no old cache dirs found
 
        root@localhost:~# command time restic -r /mnt/dest/restic-repo backup create /mnt/deepdir/emptyfile/data --verbose
        create does not exist, skipping
        open repository
        lock repository
        load index files
        no parent snapshot found, will read all files
        start scan on [/mnt/src/data]
        start backup on [/mnt/src/data]
        scan finished in 0.202s: 1 files, 1024.000 GiB

        Files:           1 new,     0 changed,     0 unmodified
        Dirs:            2 new,     0 changed,     0 unmodified
        Data Blobs:      1 new
        Tree Blobs:      3 new
        Added to the repo: 134.501 MiB

        processed 1 files, 1024.000 GiB in 41:53
        snapshot 1e95810c saved
        8963.49user 296.44system 41:54.34elapsed 368%CPU (0avgtext+0avgdata 1318020maxresident)k
        2147485392inputs+825552outputs (4major+322089minor)pagefaults 0swaps
        ```
    -  Disk Usage
        ```
        root@localhost:/mnt/dst# du -sh kopia-repo
        38M	kopia-repo
        root@localhost:/mnt/dst# du -sh restic-repo
        136M	restic-repo