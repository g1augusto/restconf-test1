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

payload = {
  "ietf-interfaces:interface": {
    "name": "",
    "description": "",
    "type": "iana-if-type:softwareLoopback",
    "enabled": True,
    "ietf-ip:ipv4": {
      "address": [
        {
          "ip": "",
          "netmask": "255.255.255.255"
        }
      ]
    },
    "ietf-ip:ipv6": {}
  }
}

int_number = 5
for x in range(int_number):
    payload["ietf-interfaces:interface"]["name"] = "Loopback123"+str(x)
    payload["ietf-interfaces:interface"]["description"] = "Added with PYTHON"
    payload["ietf-interfaces:interface"]["ietf-ip:ipv4"]["address"][0]["ip"] = "1.2.3."+str(x)
    #print(payload.format(name="Loopback123"+str(x),description="Added with PYTHON",ip="1.2.3."+str(x)))
    response = requests.post(url,
            auth=credentials,
            headers=headers,
            json=payload,
            verify=False)
    print(f"Status Code: {response.status_code}")
    print(f"Response Text: {response.text}")

int_number = 5
for x in range(int_number):
    response = requests.delete(f"{url}/interface=Loopback123{str(x)}",auth=credentials,headers=headers,verify=False)
    print(f"Status: Code: {response.status_code}")
    print(f"Response Text: {response.text}")

