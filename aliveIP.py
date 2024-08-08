import subprocess
import re

def is_host_up(ip):
    try:
        output = subprocess.check_output(["ping", "-c", "1", ip], stderr=subprocess.STDOUT, timeout=5)  # Increased timeout
        return not re.search(b"100% packet loss", output)
    except subprocess.CalledProcessError:
        return False
    except subprocess.TimeoutExpired:
        print(f"Host {ip} timed out after 5 seconds")
        return False
target = 1
up = 0
down = 0
total = 0

while target < 255:
    ip = "192.168.0." + str(target)
    total += 1

    if is_host_up(ip):
        print(f"Host {ip} is online")
        up += 1
    else:
        print(f"Host {ip} is offline or unavailable")
        down += 1

    target += 1

print("A total of", total, "hosts were scanned.")
print(str(up), "hosts were alive, and", str(down), "hosts were unreachable.")
quit()