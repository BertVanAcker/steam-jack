# How to close the UDP socket manually
kill -9 $(ps -A | grep python | awk '{print $1}')