from subprocess import call
import csv
import subprocess
import re


def createtest(list):
    results = []
    for line in list:
        call(" echo " + line + "|" + "./mkvcalcproba" + " statfile" + ">" + "output.txt", shell=True)
        with open('output.txt') as f:
            lines = f.readlines()
            for line in lines:
                line = re.split('\s+', line)
                Markov = line[2]
                MarkovMax= int(line[3]) * 255
                Finalstatement= "Markov Score for: " + str(line[0]) + " is " + str(Markov) + " out of " + str(MarkovMax)
                results.append(Finalstatement)

    for result in results:
        print result

def createstats(list):
    call(" touch " + " temporarystats.txt", shell=True)
    thefile = open('temporarystats.txt', 'w')
    for item in list:
        thefile.write("%s\n" % item)


def openexcel(filename):
    list2=[]
    list3=[]
    count=0
    with open(filename, 'r') as f:
        csv_reader = csv.reader(f, delimiter='"')

        for row in csv_reader:
           list3.append(row[0])




        createstats(list3)
        call(" ./calc_stat " + "temporarystats.txt" + " statfile", shell=True)







print "Feed me a csv file (example: ninjas.csv)"
x = raw_input("File:")
openexcel?



dirtyset=["blcauxgxksnjrdpi.eu","dusbourwwfnjrdpi.eu","oypuasanwowlqxth.eu","wlpdqyutiemfhqco.eu","tdccjwtetv.com","psnsmtvpmuj.com","gbghkwmforpewx.com","vgtblplqgu.com","abijetqgk.com","benprwwiosbrlad.com"]
cleanset=["google.com","amazon.com","facebook.com","twitter.com","linkedin.com","wordpress.org","instagram.com","pinterest.com","wikipedia.org","blogspot.com","apple.com"]
mixedset=["googla.com","amazan.com","fecebook.com","twatter.com","lankedin.com","wardpress.org","onstagram.com","panterest.com","wokipedia.org","blygspot.com","spple.com"]

createtest(mixedset)