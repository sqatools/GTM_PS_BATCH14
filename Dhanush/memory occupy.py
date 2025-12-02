import psutil

for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
    try:
        print(proc.info)
    except:
        pass