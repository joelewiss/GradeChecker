import sys, time
import telnetlib as tn
from modules import Config

def output(grades):
    config = Config.getConfig()
    prefix = config["Graphite"]["Prefix"]
    metrictime = time.time()
    output = ""

    #Formats grades for transmittion to graphite
    for grade in grades:
        output += prefix + "."
        
        #Only includes the first two words (split on spaces) in the metric name
        title = grade.title.split(" ")
        output += title[0].strip().lower() + title[1].strip().lower()
        
        output += " " + str(grade.score) + " "
        output += str(int(metrictime))
        output += "\n"

    print(output)

    host = config["Graphite"]["Host"].split(":")
    port = host[1]
    host = host[0]
   
    try: 
        connection = tn.Telnet(host, port)
        print("established connection")
    except ConnectionRefusedError:
        #I really need a console printing system 
        print("Error: Could not establish connection")
        return

    print("writing data...")
    connection.write(output.encode("ascii"))
    connection.close()

    print("\ndone!")
