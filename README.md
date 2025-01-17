# PowerLogger

PowerLogger is a Python application designed to track power usage by applications on Windows devices. It logs CPU and memory usage for each running application, helping you optimize energy consumption.

## Features

- Monitors CPU and memory usage of running applications.
- Logs data at specified intervals.
- Outputs logs to a CSV file for easy analysis.

## Getting Started

### Prerequisites

- Python 3.x
- `psutil` library (install using `pip install psutil`)

### Installation

1. Clone the repository or download the `power_logger.py` file.
2. Make sure you have Python 3.x installed on your system.
3. Install the required `psutil` library using pip:
   ```bash
   pip install psutil
   ```

### Usage

Run the script using Python:

```bash
python power_logger.py
```

The program will start logging power usage data every 60 seconds (default interval) to `power_usage_log.csv`.

### Configuration

- You can change the logging interval by modifying the `log_interval` parameter when creating an instance of `PowerLogger`:
  ```python
  logger = PowerLogger(log_interval=120)  # Logs every 120 seconds
  ```

## Contributing

Feel free to submit issues or pull requests if you find any bugs or have suggestions for improvements.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.