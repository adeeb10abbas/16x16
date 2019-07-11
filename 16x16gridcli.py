# -*- coding: utf-8 -*-
#!/usr/bin/ python3
""" CLI for 16x16 matrix """
import argparse
import urllib3
import requests
import json
import pickle
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

def reset_to_defaultA(x):
    adata = {}
    adata["attenuation"] = float(x)
    json_adata = json.dumps(adata)
    #print(json_adata)
    for i in range(1,17):
        response = requests.post("http://10.248.102.11//v2/attenuators/"+str(i),headers = headers, data=json_adata)
    print("Attenuation(default value:",x,") values has been reset!")
def reset_to_defaultS():
    data ={}
    data["position"] = int(1)
    json_data = json.dumps(data)

    for i in range(1,17):
        response = requests.post('http://10.248.102.11/v2/switches/'+str(i), headers=headers, data=str(json_data))
    print("The switches and the positions have been reset!")

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
    print("Switch", switch,"at position", position, "has an attenuation of", attenuation) 
    print()
def get_args():
    """ Get args from command line """

    parser = argparse.ArgumentParser(description='CLI for 16x16 switch matrix')
    parser.add_argument('-p', '--position',
                        dest='position',
                        default=int(1),
                        
                        help='Set the postion(1-16)')
    parser.add_argument('-s', '--switch',
                        dest='switch',
                        default= int(1),
                        help='Set the switch(1-16)')
    parser.add_argument( "-rA",'--resetA',
                        dest='resetA',
                        default=False, 
                        action='store_true',
                        help=' Reset all the attenuations to the default value')
    parser.add_argument( "-rS",'--resetS',
                        dest='resetS',
                        default=False, 
                        action='store_true',
                        help=' Reset all the switches and positions')
    parser.add_argument( "-rAll",'--resetAll',
                        dest='resetAll',
                        default=False, 
                        action='store_true',
                        help=' Reset all the switches and positions and attenuations')                      
    parser.add_argument('-v' ,'--view',
                        dest='view',
                        default=False,
                        action='store_true',
                        help='Stop & delete a container on specified gridnode')
    parser.add_argument('-a', '--attenuation',
                        default= float(0),
                        dest='attenuation',
                        #action='store_const',
                        help='Set an attenuation(1-92)')
    parser.add_argument('-cda','--changedefaultattenuation',
                        default = float(0),
                        dest= 'SetAttDef',
                        
                        help=argparse.SUPPRESS
                        )
    
    args = parser.parse_args()

    return(args)
def main():
    listy=[50.0]
    args = get_args()
    if args.view:
        view(args.view)
    if args.switch:
        set_position(args.position, args.switch)
    if args.position:
        set_position(args.position, args.switch)
    if args.resetAll:
        with open ('def_attenuation_value', 'rb') as fp:
            listy = pickle.load(fp)
            reset_to_defaultA(float(listy[len(listy)-1]))
        reset_to_defaultS()

    if float(args.SetAttDef)!=0:
        listy.append(float(args.SetAttDef))
        with open('def_attenuation_value', 'wb') as fp:
            pickle.dump(listy, fp)
        reset_to_defaultA(args.SetAttDef)
    if args.resetA:
        with open ('def_attenuation_value', 'rb') as fp:
            listy = pickle.load(fp)
            reset_to_defaultA(float(listy[len(listy)-1]))
        print(listy[len(listy)-1])
    if args.resetS:
        reset_to_defaultS()
    if float(args.attenuation)!=0:
        attenuation(args.attenuation, args.switch, args.position)
if __name__ == "__main__":
    main()
    


