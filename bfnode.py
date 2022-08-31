#!/share/apps/anaconda3/bin/python
# by jtyang 2020/6/30
import os
import time
import re

class node:
    def __init__(self,name):
        self.name= name
        self.totCore= 12
        self.usedCore= 0
        self.pState= "R"
        self.state=""
    def qNode(self):
        print(' {:12s}{:>2d}/{:02d}       {:8s}'.format(self.name, self.usedCore, self.totCore, self.pState) )

# get used core number
def getUsedCore(line):
    # print(line)
    nUsedCore=0
    tmpList=[]
    words= re.findall(r"[ \,](.+?)/\d+\.master?",line)
    if "jobs" in line[0:11]:
        words[0]=words[0][11:]
        # print(words)
        # print("its a job line")
        # get core one by one
        for i in range(len(words)):
            if "-"  in words[i]:
                tmpList= re.findall(r"(\d+)-(\d+)",words[i])
                for j in range(len(tmpList)):
                    nUsedCore= nUsedCore+ int(tmpList[0][1])- int(tmpList[0][0])
            nUsedCore= nUsedCore+ words[i].count(",") +1
        return nUsedCore
    else:
        return nUsedCore

def getAllNodeList():
    import os
    import re
    import time
    nodeList=[]
    username = os.popen('whoami').readline()[:-1]
    #tmpfile="/tmp/"+username+"tmpqnodes"
    # tmpfile="qnodes.txt"
    stream = os.popen("qnodes")
    #lines= stream.read()
    lines = re.split('\n', stream.read())
    #time.sleep(0.1) # write file delay
    # print(tmpfile)
    #finObj=open(tmpfile)
    # analysis the file
    ## if node info
    for i in range(len(lines)):
        #line=finObj.readline()
        line = lines[i]
        if line[0:6]== "master" or line[0:4]== "node":
            #print(line)
            # init
            nTmp= node(line)
            # state
            line= lines[i+1]
            #print(line,'state')
            nTmp.state= str.split(line)[2]
            # power state
            line= lines[i+2]
            #print(line,'pstate')
            nTmp.pState= str.split(line)[2][0]
            if nTmp.pState== 'R' : nTmp.pState= 'r'
            # tot core
            line= lines[i+3]
            #print(line,'totCore')
            nTmp.totCore= int(str.split(line)[2])
            # ntype
            line= lines[i+4] # ntype
            # status or jobs
            line= lines[i+5] 

            ### get usedCore
            nTmp.usedCore= getUsedCore(line)

            nodeList.append(nTmp)

    # finObj.close()
    return nodeList

def getEmptyNodeList( nList='all', age='all'):
    """return list of nodes which are with 0 used cores and not master"""

    allEmptyList= [i for i in getAllNodeList() if i.usedCore == 0 and i.pState == 'r' and i.name != 'master' ]
    if age == 'all':
        emptyList = allEmptyList
    elif age == 'new':
        emptyList = [ n for n in allEmptyList if n.totCore == 32 ]
    elif age == 'old':
        emptyList = [ n for n in allEmptyList if n.totCore == 28 ]
    else:
        emptyList=[]

    if nList != 'all': emptyList = emptyList[:nList]
    return emptyList

# a brief way to show node info
def bfNode():
    nodeList=getAllNodeList()
    print(" name       used/tot    stat")
    for i in range(len(nodeList)):
        print("--------    --------    ----")
        nodeList[i].qNode()
    print("--------    --------    ----")

#def getFreeNodeList():
#    import pandas as pd
#    pass

#nodeList= getAllNodeList()
#for i in nodeList:
#    print(i.name)
# nodeList= getEmptyNodeList()
#for i in nodeList:
#    print(i.name)

def main():
    bfNode()
    print('all nodes:', [i.usedCore for i in getAllNodeList()])
    print('empty nodes:', [i.name for i in getEmptyNodeList()])

if __name__ == "__main__":
    main()
