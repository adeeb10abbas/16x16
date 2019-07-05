import click
import requests
import json

@click.command()
@click.option('--position', '-p', default = 1, help = "input the position(1-16).", type = int)
@click.option('--switch', '-s', default = 1, help = "input the switch (1-16).", type = int)
@click.option('--reset', '-r', is_flag = False ,default = False, help = "True sets everything to default.")
@click.option('--view', '-v', is_flag = False, default = False, help = "Use this to see the current status of the matrix.")
@click.option('--attenuation', '-a', default = 0, help = "Set attenuation(0.0 - 92.0)", type = float)
def main(switch, position, reset, view, attenuation):
    headers = {
    'Content-Type': 'application/json',
    }
    data = {}
    adata={}
    data["position"] = int(position)
    
    adata["attenuation"] = float(attenuation)
    json_data = json.dumps(data)
    json_adata = json.dumps(adata)
    

    response = requests.post('http://10.248.102.11/v2/switches/'+str(switch), headers=headers, data=str(json_data))
   
    print(response.text)
    if reset:
        adata["attenuation"] = 0.0
        data["position"] = int(1)
        

        response = requests.post("http://10.248.102.11//v2/defaults/switches ",headers = headers, data=str(json_data))
        
        json_adata = json.dumps(adata)
        for i in range(1,17):
               response = requests.post('http://10.248.102.11/v2/switches/'+str(i), headers=headers, data=str(json_data))
               response = requests.post("http://10.248.102.11//v2/attenuators/"+str(i),headers = headers, data=json_adata)
               response = requests.get("http://10.248.102.11//v2/attenuators/"+str(i))
               print(response.text)
        print("All switches and attenuation has been reset!")
            
    if view:
        print("<--------------Current Status------------>")
        response = requests.get('http://10.248.102.11//v1/switches/', headers= headers)
        a = str(response.text).split(',')
        print(a)
        print("<---------------------------------------->")
    if int(attenuation)!=0:
        response = requests.post("http://10.248.102.11//v2/attenuators/"+str(switch),headers = headers, data=json_adata)
        #print(response.text)
        print("Switch", switch,"at position", position, "has an attenuation of", attenuation) 
        print()
        for i in range(1,17):
               response = requests.get("http://10.248.102.11//v2/attenuators/"+str(i))
               print(response.text)


if __name__ == "__main__":
    main()
    
