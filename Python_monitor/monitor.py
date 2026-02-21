import psutil
import time
import subprocess
import matplotlib.pyplot as plt
from logger import log_usage

cpu_data = []
memory_data = []

plt.ion()
fig, ax = plt.subplots()

def get_usage():
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    return cpu, memory

def process_with_cpp(cpu, memory):
    # Calls the C++ processor
    try:
        result = subprocess.run(
            ["../cpp_engine/processor.exe", str(cpu), str(memory)],
            capture_output=True,
            text=True
        )
        print(result.stdout)
    except FileNotFoundError:
        print("C++ processor.exe not found. Skipping C++ alerts.")

while True:
    cpu, memory = get_usage()
    
    cpu_data.append(cpu)
    memory_data.append(memory)

    log_usage(cpu, memory)
    process_with_cpp(cpu, memory)

    ax.clear()
    ax.plot(cpu_data, label="CPU Usage (%)")
    ax.plot(memory_data, label="Memory Usage (%)")
    ax.legend()
    ax.set_title("Real-Time System Monitoring")
    
    plt.pause(0.1)
    time.sleep(2)