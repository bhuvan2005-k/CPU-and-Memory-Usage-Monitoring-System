# Real-Time System Monitor

This project monitors your computer’s "CPU and memory usage" in real time using Python, and provides alerts using a C++ program. It also logs the data into a CSV file and shows a live graph.

## Files

1. python_monitor/monitor.py – Main program that reads CPU and memory usage, logs it, sends it to the C++ processor, and plots a live graph.  
2. python_monitor/logger.py – Handles logging of CPU and memory usage into `logs/usage_log.csv`.  
3. cpp_engine/processor.cpp – Processes CPU and memory values and shows alerts if usage is high.  
4. logs/usage_log.csv – CSV file where usage data is stored. Starts empty and fills when the monitor runs.

## Features

1. Monitor "CPU" and "memory" in real time.  
2. Log data into a CSV file.  
3. Show alerts when CPU > 85% or memory > 80%.  
4. Display a live graph of usage with matplotlib.  

## How to Use

1. Compile the C++ processor  
   Go to the "cpp_engine" folder and compile:

   Windows:
   ```bash
   g++ processor.cpp -o processor.exe
`
   Linux/macOS:
   ```bash
   g++ processor.cpp -o processor
```
2. Run the Python monitor
    Go to the python_monitor folder and run:
    python monitor.py

3. You will see:

   Real-time CPU and memory usage graph
   Alerts from the C++ processor in the console
   Logged usage data in logs/usage_log.csv
