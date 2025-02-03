
import json
import sys


inventory = {
    "_meta": {
        "hostvars": {
            "server1": {"ansible_host": "192.168.1.10", "ansible_user": "admin"},
            "server2": {"ansible_host": "192.168.1.11", "ansible_user": "admin"}
        }
    },
    "webservers": {
        "hosts": ["server1"]
    },
    "dbservers": {
        "hosts": ["server2"]
    }
}

if len(sys.argv) == 2 and sys.argv[1]== "~list":
   print(json.dumps(inventory)) 
   sys.exit(0)

print(json.dumps(inventory))
sys.exit(1)
