#!/usr/bin/env python3

""" LXD Commands  """
from gridcli import *
import urllib3
import requests
import json
headers = {
    'Content-Type': 'application/json',
    }
def set_position(position, switch):
    headers = {
    'Content-Type': 'application/json',
    }
    data = {}
    data["position"] = int(position)
    json_data = json.dumps(data)
    response = requests.post('http://10.248.102.11/v2/switches/'+str(switch), headers=headers, data=str(json_data))

def reset_to_default():
    adata = {}
    data ={}
    adata["attenuation"] = 0.0
    data["position"] = int(1)
    json_adata = json.dumps(adata)
    json_data = json.dumps(data)

    response = requests.post("http://10.248.102.11//v2/defaults/switches ",headers = headers, data=str(json_data))
    
    json_adata = json.dumps(adata)
    for i in range(1,17):
        response = requests.post('http://10.248.102.11/v2/switches/'+str(i), headers=headers, data=str(json_data))
        response = requests.post("http://10.248.102.11//v2/attenuators/"+str(i),headers = headers, data=json_adata)
        response = requests.get("http://10.248.102.11//v2/attenuators/"+str(i))
        #print(response.text)
    print("All switches and attenuation has been reset!")
def view(view):
    print("<-------------- Status------------>")
    for i in range(1,17):
        response = requests.get('http://10.248.102.11//v2/switches/'+str(i), headers= headers)
        response2 = requests.get("http://10.248.102.11//v2/attenuators/"+str(i))
        a = response.text.split(',')
        ab = response2.text.split(',')
        
        print("switch"+a[0][5:], a[1][12:], ab[1][12:])
    print("<---------------------------------------->")
def attenuation(attenuation, switch, position):
    headers = {
    'Content-Type': 'application/json',
    }
    adata = {}
    adata["attenuation"] = float(attenuation)
    json_adata = json.dumps(adata)
    response = requests.post("http://10.248.102.11//v2/attenuators/"+str(switch),headers = headers, data=json_adata)
    #print(response.text)
    print("Switch", switch,"at position", position, "has an attenuation of", attenuation) 
    print()
    # for i in range(1,17):
    #     response = requests.get("http://10.248.102.11//v2/attenuators/"+str(i))
    #     print(response.text.split(' '))


if __name__ == "__main__":
    main()
    







































# # Suppress urllib3 insecure request warning (https://github.com/influxdata/influxdb-python/issues/240)
# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

# # List of active grid nodes (as of June 2018)
# grid_nodes = ["grid01",
#         "grid03",
#         "grid04",
#         "grid05",
#         "grid06",
#         "grid07",
#         "grid08",
#         "grid09",
#         "grid10",
#         "grid11",
#         "grid12",
#         "grid13",
#         "grid14",
#         "grid15",
#         "grid16",
#         "grid17",
#         "grid18",
#         "grid19",
# ]

# # Cert & Key location
# certfile = '/opt/client.crt'
# keyfile = '/opt/client.key'

# def show_free_nodes():
#     """ Return list of nodes with zero containers running on them """
#     # Create empty dict
#     node_num_container = dict()

#     print("\nAvailable Nodes:")
#     print("===============\n")

#     # Check for all active grid nodes
#     for node in grid_nodes:
#         try:
#             client = Client(endpoint='https://{}.maas:8443'.format(node),
#                         cert=(certfile, keyfile),
#                         verify=False)
#         except Exception as e:
#             #print('Unable to connect to {}'.format(e))
#             continue
#         containers = client.containers.all()
#         num = sum(1 for container in containers)
#         if num == 0:
#             print(node)

#     print("\n")


# def check_gridnode_free(gridnode):
#     """ Check if gridnode has no containers and is available for use """
#     """ Note that this function does not check whether a container is running
#     or not. It only checks whether a container exists on the node """

#     # Init connection
#     try:
#         client = Client(endpoint='https://{}.maas:8443'.format(gridnode),
#                     cert=(certfile, keyfile),
#                     verify=False)
#     except Exception as e:
#         print('Unable to connect to {}'.format(e))

#     # Get container info
#     containers = client.containers.all()

#     num = sum(1 for container in containers)
#     if num == 0:
#         # print("\nGrid node is free")
#         return True
#     else:
#         # print("\nGrid node is not free")
#         return False


# def start_container(gridnode, imagesource):
#     """ Start a container on gridnode using imagesource """

#     # Init connection
#     try:
#         client = Client(endpoint='https://{}.maas:8443'.format(gridnode),
#                     cert=(certfile, keyfile),
#                     verify=False)
#     except Exception as e:
#         print('Unable to connect to {}'.format(e))

#     # Check if node is free before starting container
#     if check_gridnode_free(gridnode) == True:
#         # Container config
#         config = {
#                   'name': 'my-container',
#                   'source':
#                     {
#                      'type': 'image',
#                      "mode": "pull",
#                      "server": "https://dwslgrid.ece.drexel.edu:8443",
#                      "protocol": "lxd",
#                      "certificate": "-----BEGIN CERTIFICATE-----\nMIIFVTCCAz2gAwIBAgIQeq43aT8IDaeLLaH5Zhlw7TANBgkqhkiG9w0BAQsFADA3\nMRwwGgYDVQQKExNsaW51eGNvbnRhaW5lcnMub3JnMRcwFQYDVQQDDA5yb290QGR3\nc2wtbWFhczAeFw0xODA4MTAyMDEzMDNaFw0yODA4MDcyMDEzMDNaMDcxHDAaBgNV\nBAoTE2xpbnV4Y29udGFpbmVycy5vcmcxFzAVBgNVBAMMDnJvb3RAZHdzbC1tYWFz\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEArkGYuPuD9RzNuJk1g6ek\nwZO6wPcp8EZfyfVF7lhahD2dpe6gfa1rH18GG+WwG5j6aArI1CJ9tMufwghwRw8Q\nVAyPtq3E7g9yLPi+NtYskTHBpqGMQ44EWq/xc3TALQpHYVRsDtRdYxNB/+HUdRuR\n6RQfu3gaEQOgXa339OWyb00bx83Meb0s9p2RXHUsacYSNHcW/iulN/GJBDNEs1Ue\nDY6YgKXSnl7JtEazMmx/wiO96J6m07liAXmzLLdZuv2eN1/Ute9+8i06bVRrJ8MN\ntfisbLUC61Inx6sEXAvM2o732soWbK5fqvZamuCXAWWVnQ9wLSB0/KfgTindmb7s\nkNzoTjOW+R9WYYXf/cgk/kdc61dj2FiKBOmD+yo0pcqXL6SalGbUpBQfl2CrFnHG\nmwuerwI2tuuKRQDRWU46QiJw7/Y4gU1Govfbq3SMYyxz4GjYEFna65UKgrCAxGNt\n8kHD4E3UAkJbz92Q+GhGphyP2wQpy9/CGhBlAvUkw6T+EqwsBGQNryUaf90nZNYs\n4GfOyObXkbs6iGYWpcVq+NeZO98+4yGRE2kIF+rWonc7zexptYr9PJ06hy/+I1AR\ntRG9yf4kPgya7ll3qqcp6Pl9MWy7prd32nAFEXo20KP3R5sZFxWiVecHapZIRvGj\np57nrabQhuMn8ZQiEMXezl8CAwEAAaNdMFswDgYDVR0PAQH/BAQDAgWgMBMGA1Ud\nJQQMMAoGCCsGAQUFBwMBMAwGA1UdEwEB/wQCMAAwJgYDVR0RBB8wHYIJZHdzbC1t\nYWFzhwQK+Ge1hwTAqAEBhwSsEQABMA0GCSqGSIb3DQEBCwUAA4ICAQAzLxiTZkPC\nCiDCl38gNmrM7kCWuXZPZTuTa9mP0jDP9xG8BVjQEA5vTanm/w9AaFYX86Z66aMb\nZfeWnQO8DSwhBxGULuaYmQ03Ts3an+ul/AtZ8V9xcDUsVNg+BSda5HbIQx6J0FGA\noDqqiiUzGIfMcDKKVnJjguyiLhmeViD5pBQ3rS8bGwOxzUr4+7NUURPM44vNvCjl\nUsAVWCn2hW2YR5VjFzv8NcYBTGRAqgjxPRcDwFfNKuDfOqd4iiZVEA8JwuCRZi1L\nNGMZbsp+tg/qgkeB3tSXj1waZlSYpo1RuUxdOkN9+srSpJklBo+3MjOjAUaA5cQh\nq3yDasYQUtSsuc/KMVqRSilvi6XsVBSPJWcZ5N2HUadeLUfHi8+cROWVwdEqsQw8\nR1VHynY4X3xYbE+yZxo95N9xxe8sXZRyb1PD09R0ASN3JOXu2UNNWw6QfbmXsMPa\neX8Gq0+9anVY1mKVVsGlqPF9Ig31hEmRap5AlucaGlRmyhNPObdcvboAZN8Vb1jB\n3wGwSbNwj/4fchzwROxOCndpFNeU+FuvknVcIIg6AJQRbgqvqU1EAFa8ogSGh+zU\nDdBq06Y//0hpFnk6Q0inssgPnBNPC+P74ih9VRxl1A96OMvtznYtRGLyzEwa1n0w\nz2QuXUwci7SU50zusbP1w0kSsIzQNObg6A==\n-----END CERTIFICATE-----\n",
#                      'alias': imagesource # pe2-20181107-f443697e # This can be image alias or fingerprint
#                     },
#                   'profiles': ['gridclibridge']
#                  }
#         container = client.containers.create(config, wait=True)

#         # Start container
#         container.start()
#         print("Container started on {}\n".format(gridnode))
#     else:
#         # gridnode is not free
#         print("\n{} is not available."\
#         " Select another grid node.\n".format(gridnode))


# def stop_delete_container(gridnode):
#     """ Stop and delete a container running on gridnode """

#     # Init connection
#     try:
#         client = Client(endpoint='https://{}.maas:8443'.format(gridnode),
#                                 cert=(certfile, keyfile),
#                                                     verify=False)
#     except Exception as e:
#         print('Unable to connect to {}'.format(e))

#     # Stop & delete if gridnode is not free
#     if check_gridnode_free(gridnode) == False:
#         # Stop & Delete
#         containers = client.containers.all()
#         print("\nStopping & deleting container on {}".format(gridnode))
#         for container in containers:
#             container.stop()
#             container.delete()
#         print("\nContainer on {} stopped & deleted\n".format(gridnode))
#     else:
#         print('\nThere are no containers running on {}\n'.format(gridnode))


# def ip_check_container(gridnode):
#     """ Return IP address of container on gridnode """

#     # Init connection
#     try:
#         client = Client(endpoint='https://{}.maas:8443'.format(gridnode),
#                                 cert=(certfile, keyfile),
#                                                     verify=False)
#     except Exception as e:
#         print('Unable to connect to {}'.format(e))

#     if check_gridnode_free(gridnode) == False:
#         containers = client.containers.all()

#         # Iterate through this even though only one container should be running
#         for container in containers:
#             ip_address = container.state().network['eth0']['addresses'][0]['address']

#         return ip_address
#     else:
#         print("There are no containers running on {}".format(gridnode))


# if __name__ == "__main__":
#     #sys.exit(main())  # pragma: no cover
#     #show_free_nodes()
#     # start_container("grid12", "pe2-20181107-f443697e")
#     #print(check_gridnode_free("grid12"))
#     print(ip_check_container("grid12"))
