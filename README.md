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
    | retic | 467 | 118% | 4.74 | 3.2 | 20 |
    

- Notes


### Case2: small files with vast directories (6291456 files, 10bytes)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(GB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 2504 | 73% | 2.29 | 6.0 | 52 |
    | retic | 1079 | 143%| 1.84 | 7.6 | 52 |
   
- Notes

### Case3. empty files with vast directories (5882450 files, 10bytes, 6862850 dirs)

- Performance summary:
    | tool | time(s) | cpu | max mem(MB) | repo size(MB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 8591 | 109% | 160 | 395 | 29 |
    | retic | 913 | 132%| 992 | 5324 | 29 |
    
- Notes

### Case4. 1 T file with all zero content  (1 file, 1TB, 1 dir)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(MB) | repo size(MB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 1105 | 165% | 221 | 38 | 1024 |
    | retic | 2514 | 368%| 1290 | 136 | 1024 |
    

### Case5. 1 T files with all random content  (11 file, 1004GB, 1 dir)

- Performance summary: 
        
    |tool | time(s) | cpu | max mem(GB) | repo size(GB) |target size(GB) |
    |:-----:| :----: | :----: | :----: | :----: | :----: |
    | kopia | 9444 | 301% | 357 | 1004 | 1004 |
    | retic | 5560 | 335%| 532 | 1005 | 1004 |
    
