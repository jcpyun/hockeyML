from threading import Thread
import urllib
import re
import json
import time
import math

hockeyPlayers = open("LAPlayers.txt").read()
editedPlayers = open("edited.txt").read()
editedPlayers = hockeyPlayers.replace(" ","-").split()

positive = []
negative = []
counter = 0
def th(ur):

    htmlfile=urllib.urlopen("http://www.fanbase.com/"+ur)
    #regex = '<div class="team_name"><a href="/Los-Angeles-Kings">Los Angeles Kings</a><span class="meta small_text" style="margin-left: 10px;">Defender</span></div>'

    #regex = '<a href="/New-York-Rangers">New York Rangers</a>'
    #regex = '<a href="/New-York-Rangers">(.+?)</a>'
    #regex = '<a href="/(.+?)">(.+?)</a>'
    #regex ='<div class="team_name"><a href="/New-York-Rangers">New York Rangers<\a>'
    #regex = '<div class="team_name"><a href="/Los-Angeles-Kings">Los Angeles Kings</a><span class="meta small_text" style="margin-left: 10px;">Defender</span></div>'

    regex = '<div class="team_name"><a href="/New-York-Rangers">New York Rangers</a><span class="meta small_text" style="margin-left: 10px;">Defender</span></div>'

    pattern = re.compile(regex)

    htmltext= htmlfile.read()
    titles= re.search(pattern,htmltext)
    if titles:
        positive.append(ur)
        print "+++++++++++++++ POSITIVE MATCH DETECTED ++++++++++++++++++"
        print ur
    else:
        negative.append(ur)
        print "-------------- NEGATIVE MATCH DETECTED ------------------"
        print ur
threadlist = []

for u in editedPlayers:
    t = Thread(target = th, args=(u,))
    t.start()
    threadlist.append(t)

for b in threadlist:
    b.join()

def generate():
    print "Positive Matches:", positive
    print "Negative Matches:", negative
    var = len(positive)
    varneg = len(negative)
    print var, "Positive Matches found"
  #  print "Negative Matches", negative
    print varneg, "Negative Matches"

generate()
