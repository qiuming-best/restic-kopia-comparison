2. small files with vast directories (6291456 files, 10bytes)
    - Generate data
        ```
        python3 data_gen.py -n 7 -f 1 -s 100 -d 7 -p /mnt/deepdir/data
        ^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@^@ 52G ./

        du -sh --apparent-size
        ^@^@^@^@^@^@^@^@^@^@29G	.
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
 
        command time kopia snapshot create /mnt/deepdir/data
        Processed 13481692 contents, discovered 13481692...
        Looking for unreferenced contents...
        Rewriting contents from short packs...
        ^@Not enough time has passed since previous successful Snapshot GC. Will try again next time.
        Skipping blob deletion because not enough time has passed yet (59m59s left).
        Cleaned up 0 logs.
        Cleaning up old index blobs which have already been compacted...
        Finished full maintenance.
        2207.86user 724.99system 49:56.32elapsed 97%CPU (0avgtext+0avgdata 2401237maxresident)k
        206958808inputs+32172544outputs (6122major+4586940minor)pagefaults 0swaps
        ```
    - restic 

        ```
        restic init --repo /mnt/dst/restic-repo
        restic cache --cleanup
        no old cache dirs found
 
        root@localhost:/# command time restic -r /mnt/dst/restic-repo backup create /mnt/deepdir/data --verbose
        create does not exist, skipping
        open repository
        lock repository
        load index files
        no parent snapshot found, will read all files
        start scan on [/mnt/deepdir/data/]
        start backup on [/mnt/deepdir/data/]
        scan finished in 1078.340s: 6291456 files, 600.000 MiB

        Files:       6291456 new,     0 changed,     0 unmodified
        Dirs:        7190238 new,     0 changed,     0 unmodified
        Data Blobs:  6291456 new
        Tree Blobs:  7190239 new
        Added to the repo: 5.219 GiB

        processed 6291456 files, 600.000 MiB in 17:58
        snapshot d98b10df saved
        1035.20user 508.30system 17:59.35elapsed 143%CPU (0avgtext+0avgdata 1931100maxresident)k
        121377216inputs+42433216outputs (116major+561775minor)pagefaults 0swaps   
        ```
    -  Disk Usage
        ```
        root@localhost:/# du -sh /mnt/dst/kopia-repo
        7.6G    /mnt/dst/kopia-repo
        root@localhost:/# du -sh /mnt/dst/restic-repo
        6.0G    /mnt/dst/restic-repo
        ```