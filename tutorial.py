from pymem import *
from pymem.process import *

pm=Pymem('ac_client.exe')

gameModule=module_from_name(pm.process_handle,'ac_client.exe').lpBaseOfDll
# gameModule=4194304

def GetPtrAddr(base,offsets):
    addr=pm.read_int(base)
    for i in range(len(offsets)-1):
        addr=pm.read_int(addr+offsets[i])
    return addr+offsets[len(offsets)-1]

while True:
    address1=GetPtrAddr(gameModule+0x000FAD90,[0x44,0x44,0x44,0x0,0x18,0xC4,0x418])
    pm.write_int(address1,500)

