# PySNMP Network Monitoring System
=====================================

## Overview
--------

This project uses the popular PySNMP library to create a simple network monitoring system that can collect data
from SNMP-enabled devices and store it in a log.

## Requirements
------------

* Python 3.8+
* PySNMP 5.0+
* Logging library (built-in Python)

## Installation
------------

To install this project, run the following command:

```bash
pip install pysnmp
```

Usage
-----

### Configuration

Create a configuration file `config.py` with the following format:
```python
# config.py

# Device IP addresses and SNMP credentials
devices = {
    'device1': {'ip': '192.168.1.100', 'community_string': 'public'},
    'device2': {'ip': '192.168.1.101', 'community_string': 'private'}
}

# Log file name and directory
log_file_name = 'network_monitor.log'
log_directory = '/path/to/log/directory'
```

### Running the script

Run the following command to start collecting data from devices:

```bash
python network_monitor.py
```

This will start a thread that periodically checks each device for new data, logs it to the specified log file, and
waits for 30 seconds before checking again.

Logging Configuration
--------------------

The logging configuration can be customized in the `config.py` file. The following options are available:

*   `log_file_name`: Specify the name of the log file.
*   `log_directory`: Specify the directory where the log file should be saved.

### Example Log Entry

Here's an example of what a log entry might look like:
```
2023-02-20 14:30:00,000 - Device 'device1' returned value 1.3.6.1.2.1.1.5.0 from OID 'sysUpTime'
2023-02-20 14:30:01,000 - Device 'device1' returned value 1.3.6.1.2.1.1.4.0 from OID 'sysName'
```

This log entry shows the timestamp, device name, and two log messages with SNMP response values.

Troubleshooting
---------------

*   Check the PySNMP library for any known issues or bugs.
*   Verify that your devices are correctly configured to accept SNMP queries.
*   Check the log file for any error messages that might indicate a problem.
