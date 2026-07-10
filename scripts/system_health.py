import psutil
from datetime import datetime

CPU_THRESHOLD = 80
MEMORY_THRESHOLD = 80
DISK_THRESHOLD = 80

cpu = psutil.cpu_percent(interval=1)
memory = psutil.virtual_memory().percent
disk = psutil.disk_usage('/').percent
processes = len(psutil.pids())

print("=" * 50)
print("System Health Report")
print("Time:", datetime.now())
print("=" * 50)

print(f"CPU Usage      : {cpu}%")
print(f"Memory Usage   : {memory}%")
print(f"Disk Usage     : {disk}%")
print(f"Running Process: {processes}")

print("\nAlerts:")

alert = False

if cpu > CPU_THRESHOLD:
    print("High CPU Usage")
    alert = True

if memory > MEMORY_THRESHOLD:
    print("High Memory Usage")
    alert = True

if disk > DISK_THRESHOLD:
    print("Low Disk Space")
    alert = True

if not alert:
    print("System is Healthy")