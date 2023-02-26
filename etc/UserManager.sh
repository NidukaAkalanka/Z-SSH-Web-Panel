#!/bin/bash
exd=$(date +%F  -d "$number days")
useradd -e $exd -M -N -s /bin/false $username && echo "$username:$password" | chpasswd &&
clear &&
exit 0
