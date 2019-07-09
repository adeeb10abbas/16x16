# -*- coding: utf-8 -*-

""" CLI for 16x16 matrix """

import argparse
from lxd_commands import *

def get_args():
    """ Get args from command line """

    parser = argparse.ArgumentParser(description='CLI for 16x16 switch matrix')
    parser.add_argument('-p', '--position',
                        dest='position',
                        default=int(1),
                        #action='store_true',
                        help='Set the postion(1-16)')
    parser.add_argument('-s', '--switch',
                        dest='switch',
                        default= int(1),
                        help='Set the switch(1-16)')
    parser.add_argument( "-r",'--reset',
                        dest='reset',
                        default=False, 
                        action='store_true',
                        help=' Reset all the switches, positions and attenuations')
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
    
    args = parser.parse_args()

    return(args)


def main():
    args = get_args()
    if args.view:
        view(args.view)
    if args.switch:
        set_position(args.position, args.switch)
    if args.position:
        set_position(args.position, args.switch)
    if args.reset:
        reset_to_default()
    if float(args.attenuation)!=0:
        attenuation(args.attenuation, args.switch, args.position)

    # elif args.gridnode:
    #     if args.gridnode in grid_nodes:
    #         # Do stuff
    #         if args.start:
    #             # Check if image source is provided
    #             if args.image:
    #                 print("\nStarting container on {}".format(args.gridnode))
    #                 start_container(args.gridnode, args.image)
    #             else:
    #                 print("\nImage source not provided. Use -i or --image to"\
    #                        "provide a source image from DWSL radio image server\n")
    #         elif args.stop:
    #             # Grid node is already provided, so run function
    #             stop_delete_container(args.gridnode)
    #         elif args.ipaddresscheck:
    #             # Print container IP address on gridnode
    #             print(ip_check_container(args.gridnode))
    #         else:
    #             # Neither start nor stop provided
    #             print("\nOperation on grid node not provided. Use --start or"\
    #                     "--stop to start or stop a container on a grid node\n")
    #     else:
    #         print("\n{} is not a valid grid node.\n".format(args.gridnode))
    # else:
    #     print("Grid node not provided. Use -gn or --gridnode")
