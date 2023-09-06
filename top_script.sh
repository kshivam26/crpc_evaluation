#!/bin/sh
# __process_name=$1
> top_log_stats5.txt
while (true)
do
  # clear
#   __arg=$(pgrep -d',' -f $__process_name)
    # top -H -b -n 1 -p $(pgrep -d',' -f deptran) >> top_log_test.txt
  top -H -b -n 1 -p $(pgrep -d',' deptran) >> top_log_stats5.txt
  sleep 0.85
done

#  top -H -n 5 -b -p $(pgrep -d',' -f deptran)