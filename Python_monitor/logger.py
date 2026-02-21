import csv
import os
from datetime import datetime

LOG_FILE = "../logs/usage_log.csv"

def log_usage(cpu, memory):
    os.makedirs(os.path.dirname(LOG_FILE), exist_ok=True)
    file_exists = os.path.isfile(LOG_FILE)

    with open(LOG_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Timestamp", "CPU (%)", "Memory (%)"])
        writer.writerow([datetime.now(), cpu, memory])