from modules import Config, Connection, Grades
import sys, argparse


"""Main Script file for Joe's Grade Checker

Joe Lewis 2019 (c)
MIT Licence
Does all the fancy stuff contained in the modules diectory in a central location
The script is intended to be scheduable by something like chron and customizable in the config file
"""

if __name__ == "__main__":
    
    #First, setup the argument parser
    args = argparse.ArgumentParser(description="Connects to ParentConnect and outputs grades in multiple formats")
    args.add_argument("-c", "--config", nargs=1, type=str, metavar="path",  help="path for configuration file")
    args = args.parse_args()

    #Load configuration options from file
    if args.config:
        #TODO: implement fancy path evaluation
        pass
    else:
        config = Config.getConfig()
    
    #Start connection to parent connect
    Connection.readGrades(config)
