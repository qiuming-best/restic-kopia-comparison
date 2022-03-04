3. empty files with vast directories (5882450 files, 10bytes, 6862850 dirs)
    - Generate data
        ```
        python3 data_gen.py -n 50 -f 1 -s 0 -d 7 -p /mnt/deepdir/emptyfile/data
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

        root@localhost:~# kopia policy set --compression=gzip-best-compression --global

        root@localhost:~# command time kopia snapshot create /mnt/deepdir/emptyfile/data
        Snapshotting root@localhost:/mnt/deepdir/emptyfile/data ...
        * 0 hashing, 5882450 hashed (0 B), 0 cached (0 B), uploaded 335.9 MB, estimating...^@
        Created snapshot with root k106ecd5927ebec1cfe7d16b858540bef and ID 2258c72279308df1bc7f05b4494aaf6a in 14m19s
        573.06user 364.26system 14:19.90elapsed 109%CPU (0avgtext+0avgdata 164064maxresident)k
        60883744inputs+5443168outputs (489major+60377minor)pagefaults 0swaps
        ```
    - restic 

        ```
        restic init --repo /mnt/dst/restic-repo
        restic cache --cleanup
        no old cache dirs found
 
       root@localhost:/mnt/deepdir# command time restic -r /mnt/dst/restic-repo backup create /mnt/deepdir/emptyfile --verbose
        create does not exist, skipping
        open repository
        enter password for repository:
        repository fe2b8a17 opened successfully, password is correct
        created new cache in /root/.cache/restic
        lock repository
        load index files
        no parent snapshot found, will read all files
        start scan on [/mnt/deepdir/emptyfile]
        start backup on [/mnt/deepdir/emptyfile]
        scan finished in 909.589s: 5882450 files, 0 B

        Files:       5882450 new,     0 changed,     0 unmodified
        Dirs:        6862854 new,     0 changed,     0 unmodified
        Data Blobs:      0 new
        Tree Blobs:  6862855 new
        Added to the repo: 3.958 GiB

        processed 5882450 files, 0 B in 15:09
        snapshot 9c622e52 saved
        795.38user 413.73system 15:13.29elapsed 132%CPU (0avgtext+0avgdata 1016636maxresident)k
        59981296inputs+30849552outputs (138major+584487minor)pagefaults 0swaps
        ```
    -  Disk Usage
        ```
        root@localhost:/mnt/dst# du -sh kopia-repo
        395M	kopia-repo
        root@localhost:~# du -hs /mnt/dst/restic-repo
        5.2G	/mnt/dst/restic-repo
        ```