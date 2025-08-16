import json

with open("hacker.json") as f,\
     open("new.json", "w") as f_out:
     active_hosts = []
     data = json.load(f)
     for host in data["hosts"]:
         port_list = [port["port"] for port in host["ports"] if port["status"] == "open" ]
         print(f'Host {host["ip"]} ({host["os"]}): open ports -> {"".join(str(port_list))}')
         data_hosts = {
             "ip": host["ip"], "open_ports": "".join(str(port_list))
         }
         active_hosts.append(data_hosts)
     final_data = {"active_hosts": active_hosts}
     json.dump(final_data,f_out,indent=4)
