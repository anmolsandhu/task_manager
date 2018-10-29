import os

a = "/proc/1/fd/0"

print os.stat(a).st_ino