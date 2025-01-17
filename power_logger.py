import psutil
import time
import csv
from datetime import datetime

class PowerLogger:
    def __init__(self, log_interval=60):
        self.log_interval = log_interval  # in seconds
        self.log_file = "power_usage_log.csv"

    def get_power_usage(self):
        power_usage_data = []
        for proc in psutil.process_iter(['pid', 'name', 'cpu_percent', 'memory_info']):
            try:
                usage = {
                    'time': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                    'pid': proc.info['pid'],
                    'name': proc.info['name'],
                    'cpu_percent': proc.info['cpu_percent'],
                    'memory_rss': proc.info['memory_info'].rss
                }
                power_usage_data.append(usage)
            except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
                pass
        return power_usage_data

    def log_power_usage(self):
        with open(self.log_file, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Time', 'PID', 'Name', 'CPU_Usage(%)', 'Memory_Usage(RSS)'])

            while True:
                power_usage_data = self.get_power_usage()
                for usage in power_usage_data:
                    writer.writerow([usage['time'], usage['pid'], usage['name'], usage['cpu_percent'], usage['memory_rss']])
                time.sleep(self.log_interval)

if __name__ == "__main__":
    logger = PowerLogger(log_interval=60)
    print(f"Starting PowerLogger. Logging power usage data every {logger.log_interval} seconds.")
    logger.log_power_usage()