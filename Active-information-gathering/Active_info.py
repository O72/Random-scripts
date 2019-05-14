import sys
import nmap
import time

scan = nmap.PortScanner()
print('\nRunning... \n')

scanner = scan.scan(sys.argv[1], '80', arguments=' -O')

host_is_up = "The host is: " + scanner['scan'][sys.argv[1]]['status']['state'] + ".\n"
port_open = "The port 80 is: " + scanner['scan'][sys.argv[1]]['tcp'][80]['state'] + ".\n"
method_scan = "The method of scanning is: " + scanner['scan'][sys.argv[1]]['tcp'][80]['reason'] + ".\n"
guessed_os = "There is a  %s percent chance that the host is running %s"\
             %(scanner['scan'][sys.argv[1]]['os match'][0]['accuracy'],
               scanner['scan'][sys.argv[1]]['os match'][0]['name']) + ".\n"

with open("%s.txt"%sys.argv[1], 'w') as f:
    f.write(host_is_up + port_open + method_scan + guessed_os)
    local_time = time.localtime()
    f.write("\n Report generate " + time.strftime("%Y-%m%d_%H:%M:%S EST", local_time))

print("/n Finished...")
