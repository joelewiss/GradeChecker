import sys, time
from modules import Config

def output(grades):
    config = Config.getConfig()
    prefix = config["Graphite"]["Prefix"]
    metrictime = time.time()
    output = ""

    #Good lord what is this
    for grade in grades:
        output += prefix + "."
        title = grade.title.split(" ")
        output += title[0].strip().lower() + title[1].strip().lower()
        output += " " + str(grade.score) + " "
        output += str(metrictime)
        output += "\n"

    print(output)

    #ToDo: write tcp connection logic
