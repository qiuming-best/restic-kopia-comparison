#! /bin/bash
nowDate=$(date +%F)

kopia repository create filesystem --path /mnt/dst/kopia-repo -p 123
command time kopia snapshot create /mnt/deepdir/data/ -p 123 > "kopia-"$nowDate.log 2>&1
du -sh /mnt/dst/kopia-repo >> "kopia-"$nowDate.log
rm -rf /mnt/dst/kopia-repo

kopia repository create filesystem --path /mnt/dst/kopia-repo -p 123
kopia policy set --compression=gzip-best-compression --global
command time kopia snapshot create /mnt/deepdir/data/ -p 123 > "kopia-compress-"$nowDate.log 2>&1
du -sh /mnt/dst/kopia-repo >> "kopia-compress-"$nowDate.log
rm -rf /mnt/dst/kopia-repo

restic init --repo /mnt/dst/restic-repo -p /root/pass.txt
command time restic -r /mnt/dst/restic-repo -p /root/pass.txt backup create /mnt/deepdir/data/ --verbose > "restic-"$nowDate.log 2>&1
du -sh /mnt/dst/restic-repo >> "restic-"$nowDate.log