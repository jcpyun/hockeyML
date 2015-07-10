from threading import Thread
import urllib
import re
import json
import time
import math

hockeyPlayers = open("LAPlayers.txt").read()
editedPlayers = open("edited.txt").read()
editedPlayers = hockeyPlayers.replace(" ","-").split()

target="New York Rangers"
regex = '<title>(.+?)</title>'
#regex = '<a href="/New-York-Rangers">New York Rangers</a>'
#regex = '<a href="/New-York-Rangers">(.+?)</a>'
#regex = '<a href="/(.+?)">(.+?)</a>'
#regex ='<div class="team_name"><a href="/New-York-Rangers">New York Rangers<\a>'

#regex = '<div class="team_name"><a href="/Los-Angeles-Kings">Los Angeles Kings</a><span class="meta small_text" style="margin-left: 10px;">Defender</span></div>'

regex = '<div class="team_name"><a href="/New-York-Rangers">New York Rangers</a><span class="meta small_text" style="margin-left: 10px;">Defender</span></div>'

pattern = re.compile(regex)
positive=[]
def generate():
    counter = 0
    for first in editedPlayers:
        htmlfile=urllib.urlopen("http://www.fanbase.com/"+first)
        htmltext= htmlfile.read()
        titles= re.findall(pattern,htmltext)
        if titles == []:
            print first, "-----Negative Match"
        else:
            positive.append(first)
            print first, "++++++++++++++++++++++++Positive Match"

    print positive
generate()
