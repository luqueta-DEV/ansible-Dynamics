
import json


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

print(json.dumps(inventory))

