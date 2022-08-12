#!/bin/python

from audioop import add
from pyModbusTCP.server import ModbusServer, DataBank
from time import sleep
from random import uniform

from pyModbusTCP.client import ModbusClient, DataBank

# Create an instance of ModbusServer
server = ModbusServer("127.0.0.1", 12345, no_block=True)
client = ModbusClient(host = '127.0.0.1',port = 12345)
try:
    print("Start server...")
    server.start()
    print("Server is online")
    state = [0]
    db=DataBank()
    db.set_holding_registers(address=3,word_list=[int(uniform(0, 100))])
    while True:
        
        if state != db.get_holding_registers(address=3):
            state = db.get_holding_registers(address=3)
            print("Value of Register 1 has changed to " +str(state))
        sleep(0.5)

except:
    print("Shutdown server ...")
    server.stop()
    print("Server is offline")
client.read_holding_registers()
