#!/usr/bin/python3
import struct
import time
device_path = "/dev/input/js0"

# unsigned long, short, unsigned char, unsigned char
EVENT_FORMAT = "LhBB";
EVENT_SIZE = struct.calcsize(EVENT_FORMAT)

with open(device_path, "rb") as device:
  event = device.read(EVENT_SIZE)
  while event:
    (ds3_time, ds3_val, ds3_type, ds3_num) = struct.unpack(EVENT_FORMAT, event)
    print( "{0}, {1}, {2}, {3}".format( ds3_time, ds3_val, ds3_type, ds3_num ) )
    
    event = device.read(EVENT_SIZE)
