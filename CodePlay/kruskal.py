from django.http import JsonResponse
from collections import OrderedDict

from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
INFINITY=10**18
visitedColour = "#FF0000"
defaultColour = "#11479e"
currentColour = "#bbbbbb"

snapArray=[]

snapArrayDefault = OrderedDict()
snapArrayDefault['style'] = [
            {'selector': 'node',
              'style': {
                'content': 'data(id)',
                'text-opacity': 0.5,
                'text-valign': 'center',
                'text-halign': 'right',
                'background-color': defaultColour
                }
            },

            {
              'selector': 'edge',
              'style':{
                'width': 3,
                'line-color': '#9dbaea',
                'curve-style': 'bezier'
                }
            }
        ]

def styleCreator(selector, color,type):
    returnStyle = OrderedDict()
    returnStyle['selector'] = selector
    returnStyle['style'] = OrderedDict()
    if (type=="node"):
        returnStyle['style']['background-color'] = color
    else:
        returnStyle['style']['line-color'] = color
    # print returnStyle
    return returnStyle

def createSelector(type,*elements):
    if(type=="node"):
        return "#n"+str(elements[0])
    else:
        return "#e"+str(elements[0])+str(elements[1])

def getNodes(nodes):
    nodesArray= []
    for i in range(0,nodes):
        nodesArray.append({'data':{'id':"n"+str(i+1)}})
    return nodesArray

def getEdge(nodes,grid):
    edgeArray = []
    for i in range(nodes):
        for j in range(i+1,nodes):
            if(grid[i][j]):
                edgeArray.append({'data':{'id':"e"+str(i+1)+str(j+1),'source':'n'+str(i+1),'target':'n'+str(j+1)}})
    return edgeArray

def elementCreator(nodes,grid):
    elements = OrderedDict()
    elements['nodes'] = getNodes(nodes)
    elements['edges'] = getEdge(nodes,grid)
    return elements




def snapshot(nodes , *arguments):
    returnData = OrderedDict()
    returnData['style'] = list(snapArrayDefault['style'])
    returnData['elements'] = elementCreator(nodes,arguments[0])
    returnData['line'] = arguments[1]
    
    try:
        if(len(arguments[4])>1):
            for i in arguments[4]:
                returnData['style'].append(styleCreator(createSelector("node",i + 1),visitedColour,"node"))
    except:
        pass

    try:
        if(arguments[5]):
            ResultantMst=arguments[5]
            for i in range(len(ResultantMst)):
                returnData['style'].append(styleCreator(createSelector("edge" , ResultantMst[i][0] + 1 , ResultantMst[i][1] + 1) , visitedColour , "edge"))
    except:
        pass
    rank = arguments[2]
    returnData['arr'] = []
    tempDict = {}
    tempDict['type'] = "1D"
    tempDict['name'] = "Rank"
    tempvis = []
    for i in range(nodes):
        tempvis.append(rank[i]+1)
    tempDict['content'] = list(tempvis)
    returnData['arr'].append(tempDict)
    
    parent = arguments[3]
    tempDict = {}
    tempDict['type'] = '1D'
    tempDict['name'] = 'Parent'
    tempvis = []
    for i in range(nodes):
        tempvis.append(parent[i]+1)
    tempDict['content'] = list(tempvis)
    returnData['arr'].append(tempDict)    

    return returnData


def FindParent(parent , key):
    if(parent[key] == key):
        return key
    return FindParent(parent , parent[ key ])

 
def Union(rank , parent , u , v):
    ParentU = FindParent(parent , u)
    ParentV = FindParent(parent , v)
    if(rank[ ParentU ] > rank[ ParentV ]):
        parent[ ParentU ] = ParentV
    elif(rank[ ParentV ] > rank[ ParentU ]):
        parent[ ParentV ] = ParentU
    else:
        parent[ ParentV ] = ParentU
        rank[ ParentU ] += 1


def ChangeGraph(grid , nodes):
    graph=[]
    for i in range( nodes ):
        for j in range( i ):
            if( grid[i][j] ):
                graph.append([j , i , grid[i][j] ])
    return graph


def KruskalMinimumSpanningTree(grid , nodes):
    rank = [0]*( nodes )
    parent = [0]*( nodes )
    global snapArray
    snapArray = []
    snapArray.append( snapshot ( nodes , grid , 0 , rank , parent) )
    returnResponse = OrderedDict()
    graph = ChangeGraph(grid , nodes)
    #print("nodes:",nodes)
    #print("change graph is:",graph)
    graph = sorted( graph , key = lambda item: item[2])
    
    ResultantMst = []
    for i in range( nodes ):
        parent[i] = i
    i = 0
    start = 0
    
    while(start < nodes-1):
        u,v,weight = graph[i]
        i = i + 1
        ParentU = FindParent(parent,u)
        ParentV = FindParent(parent,v)
        
        if(ParentU != ParentV):
            start = start + 1
            ResultantMst.append( [u , v , weight ] )
            Union(rank , parent , ParentU , ParentV)
        TempNodeArray = set()
        
        for fro , to , wie in ResultantMst:
            TempNodeArray.add( fro )
            TempNodeArray.add( to )

        snapArray.append( snapshot( nodes , grid , 0 ,rank , parent , TempNodeArray , ResultantMst))
    #print(ResultantMst)
    snapArray.append( snapshot( nodes , grid , 0 , rank , parent, TempNodeArray , ResultantMst))
    returnResponse[ 'error' ] = False
    returnResponse[ 'data' ] = snapArray
    return JsonResponse( returnResponse )