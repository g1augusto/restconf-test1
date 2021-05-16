import requests
import urllib3

urllib3.disable_warnings()

credentials = ("developer","C1sco12345")

headers = {"Accept":"application/yang-data+json","Content-Type":"application/yang-data+json"}

host = "10.10.20.48"
port = "443"
yang_model_ifc = "ietf-interfaces"
container_ifc = "interfaces"
url = f"https://{host}:{port}/restconf/data/{yang_model_ifc}:{container_ifc}"

payload = '''
{{
    "ietf-interfaces:interface": {{
        "name": "{name}",
        "description": "{description}",
        "type": "iana-if-type:softwareLoopback",
        "enabled": true,
        "ietf-ip:ipv4": {{
            "address": [
                {{
                    "ip": "{ip}",
                    "netmask": "255.255.255.255"
                }}
            ]
        }},
        "ietf-ip:ipv6": {{}}
    }}
}}
'''
int_number = 5
for x in range(int_number):
    response = requests.post(url,
            auth=credentials,
            headers=headers,
            data=payload.format(name="Loopback123"+str(x),description="Added with PYTHON",ip="1.2.3."+str(x)),
            verify=False)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")


