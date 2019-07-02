import click
import requests
import json
@click.command()
@click.option('--position', '-p', default = 1, help = "input the position(1-16)", type = int)
@click.option('--switch', '-s', default = 1, help = "input the switch (1-16)", type = int)
@click.option('--reset', '-r', is_flag = False ,default = False, help = "True sets everything to default")
@click.option('--view', '-v', is_flag = False, default = False, help = "Use this to see the current status of the matrix")
def main(switch, position, reset, view):
    headers = {
    'Content-Type': 'application/json',
    }
    data = {}
    data["position"] = int(position)
    json_data = json.dumps(data)
    # print(json_data)

    response = requests.post('http://10.248.102.11//v1/switch/'+str(switch), headers=headers, data=str(json_data))
    click.echo(response.text)
    #print(reset)

    if reset:
        response = requests.post("http://10.248.102.11//v1/switches/default-positions ",headers = headers, data= str(json_data))
             
    if view:
        print("Current Status")
        response = requests.get('http://10.248.102.11//v1/switches/', headers= headers)
        print(response.content)
if __name__ == "__main__":
    main()
    