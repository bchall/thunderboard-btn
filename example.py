# Using Thunderboard with Python
import pexpect
import time
 
DEVICE = "00:0B:57:0C:71:CD"
 
# Run gatttool interactively.
child = pexpect.spawn("gatttool -I")
 
# Connect to the device.
child.sendline("connect {0}".format(DEVICE))
child.expect("Connection successful", timeout=5)
 
while True:
     child.sendline("char-read-hnd 0x0022")
     child.expect("Characteristic value/descriptor: ", timeout=10)
     child.expect("\r\n", timeout=10)
     print(child.before)
