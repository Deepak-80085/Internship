import time
from pysnmp.hlapi import (
    SnmpEngine, # handles SNMP protocol operations
    CommunityData, #acts like a password for SNMP v1 and v2c
    UdpTransportTarget, # specifies the device address and port
    ContextData, # context information for SNMP operations
    ObjectType, # specifies the object type 
    ObjectIdentity, # specifies the object identifier
    getCmd, # takes SNMP data
)

def fetch_snmp_data(target, community, port, oid):
    # Collect SNMP data from the target device
    iterator = getCmd(
        SnmpEngine(),  # SNMP engine
        CommunityData(community),  # Community data
        UdpTransportTarget((target, port)),  # Target device address and port
        ContextData(),  # Context data
        ObjectType(ObjectIdentity(oid)),  # Object type to fetch
    )
    errorIndication, errorStatus, varBinds = next(iterator)
    if errorIndication:
        print(f"Error: {errorIndication}")
        return None
    elif errorStatus:
        print(f"Error: {errorStatus.prettyPrint()}")
        return None
    else:
        for varBind in varBinds:
            return f"{varBind[0]} = {varBind[1]}"

def log_snmp_data(runtime, log_interval):
    # Log SNMP data for a specific runtime, creating a new log file every interval
    start_time = time.time()
    end_time = start_time + runtime
    log_file_index = 1
    log_file_name = f"snmp_logs_{log_file_index}.txt"
    while time.time() < end_time:
        current_time = time.time()
        if current_time - start_time >= log_interval * 60:
            log_file_index += 1
            log_file_name = f"snmp_logs_{log_file_index}.txt"
            start_time = current_time
        with open(log_file_name, "a") as file: 
            
            snmp_data = fetch_snmp_data(snmp_target, community_string, snmp_port, oid)
            if snmp_data:
                timestamp = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
                file.write(f"{timestamp} - {snmp_data}\n")
                file.flush()
        time.sleep(1)

# SetUp of the program
snmp_target = "192.168.1.1"  # Target device IP address to get SNMP data 
community_string = "public"  # Community string for authentication 
snmp_port = 161  # Port number
oid = "1.3.6.1.2.1.2.2.1.16"  # Object identifier for network interfaces
runtime = 3600  # 1 hour in seconds
log_interval = 1  # Log interval in minutes

# Start logging SNMP data
log_snmp_data(runtime, log_interval)