# Comparing restic and kopia

## Key Points
- split
- hash
- index
- deduplicate
- encrypt
- compress
- upload

## Metrics:
- time consuming
- memory
- disk usage
- cpu

## Environment
    kopia --version
    0.10.5 build: 512dcebaf4e4dd2b2ed04bfffb340640724f00f6 from: kopia/kopia 
    restic version 
    restic 0.12.1 compiled with go1.16.6 on linux/amd64
    


## Test Cases
### Case 1: small files with 5 directories (5M, 10bytes, 5 dir)
    
- Performance summary: 
        
    |tool | time(s) | cpu | max mem(GB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 340 | 156% | 2.98 | 1.9 | 20 |
    | restic | 467 | 118% | 4.74 | 3.2 | 20 |
    

- Notes


### Case2: small files with vast directories (6291456 files, 10bytes)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(GB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia(compress) | 3021 | 80% | 1.83 | 6.0 | 52 |
    | restic | 1079 | 143%| 1.84 | 7.6 | 52 |
   
- Notes

### Case3: empty files with vast directories (5882450 files, 10bytes, 6862850 dirs)

- Performance summary:
    | tool | time(s) | cpu | max mem(MB) | repo size(MB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 859 | 109% | 160 | 395 | 29 |
    | restic | 913 | 132%| 992 | 5324 | 29 |
    
- Notes

### Case4: 1 T file with all zero content  (1 file, 1TB, 1 dir)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(MB) | repo size(MB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 1105 | 165% | 221 | 38 | 1024 |
    | restic | 2514 | 368%| 1290 | 136 | 1024 |

- Notes
    - kopia is 2.27x much more faster than restic
    - kopia is 2.23x much less cpu than restic
    - kopia is 5.8x much less memeroy than restic
    - kopia is 3.57x much smaller repo size than restic

### Case5: Large size files with all random content  (11 file, 1004GB, 1 dir)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(MB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia(compressed) | 9444 | 301% | 357 | 1004 | 1004 |
    | kopia | 2358 | 264% | 339 | 1004 | 1004 |
    | restic | 5560 | 335%| 532 | 1005 | 1004 |
    
- Notes

### Case6: Large size files with duplicate content  (1000 file, 1000GB, 1 dir)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(MB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia(compressed) | 7203 | 380% | 329 | 984 | 1000 |
    | kopia | 2016 | 308% | 380 | 984 | 1000 |
    | restic | 5480 | 327%| 471 | 922 | 1000 |
    
### Case7: Large size files with duplicate content (100 files, 1000GB, 1 dir, compressible data)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(MB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia(compressed) | 3747 | 332% | 201 | 1.6 | 1000 |
    | kopia | 1556 | 205% | 459 | 1001 | 1000 |
    | restic | 5735 | 335%| 5944 | 1001 | 1000 |

### Case8: Large size files with duplicate content (2 files, 100GB, 1 dir, incompressible data)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(MB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia(compressed) | 732 | 381% | 326 | 100 | 100 |
    | kopia | 379 | 199% | 250 | 56 | 100 |
    | restic | 385 | 325%| 182 | 53 | 100 |

### Case9: 1T DD /dev/urandom BandWidth Test (same test data with case5)
The X axis present time(second), the Y axis present bandwidth(MB/s)
From 0s to 3116s is testing againt kopia, rest is restic.
![Bandwidth](img/bandwidth.png)