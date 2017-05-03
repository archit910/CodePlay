from django.http import JsonResponse
from collections import OrderedDict

from django.http import HttpResponseRedirect, HttpResponse
import datetime
from django.views.decorators.csrf import csrf_exempt
INFINITY=10**18
def parseMatrix(request):
	nodes = int(request.POST.get('nodes'))
	matrix = []
	for i in range(nodes):
		row = []
		for j in range(nodes):
			variable = "matrix[" + str(i) + "][" + str(j)+"]"
			row.append(int(request.POST.get(variable)))
		matrix.append(row)
	# print(matrix)
	return matrix

visited = []
#nodes = 10
Queue=[]
#Colours
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
    #print("printing snapshot is:")
    parent=arguments[2]
    graph=arguments[0]
    TempNodeArray=set()
    for i in range(nodes):
        if(parent[i]!=-1):
            TempNodeArray.add(i)
            TempNodeArray.add(parent[i])
    #print("TempNodeArray is:",TempNodeArray)
    for i in TempNodeArray:
        returnData['style'].append(styleCreator(createSelector("node",i + 1),visitedColour,"node"))
    for i in range(nodes):
        if(parent[i]!=-1):
            #print(parent[i],i,graph[i][parent[i]])
            returnData['style'].append(styleCreator(createSelector("edge" , parent[i] + 1 , i + 1) , visitedColour , "edge"))
    #print("snapshot ended here!!")
    returnData['arr']=[]


    tempDict = {}
    tempDict['type'] = "1D"
    tempDict['name'] = "Parent"
    tempvis = []
    for i in range(nodes):
        tempvis.append(parent[i]+1)
    tempDict['content'] = list(tempvis)
    returnData['arr'].append(tempDict)


    return returnData


def MinKey(key , MstSet , n):
    MinElement = INFINITY
    MinElementIndex = -1
    for i in range(n):
        if(MstSet[i] == 0 and key[i] < MinElement):
            MinElement = key[i]
            MinElementIndex = i
    return MinElementIndex


def PrimsMinimumSpanningTree(graph , nodes):
    #print(nodes)
    global snapArray
    snapArray = []
    returnResponse = OrderedDict() 
    parent = [-1] * nodes
    key = [INFINITY] * (nodes)
    MstSet = [0] * (nodes)
    key[0] = 0
    snapArray.append(snapshot(nodes , graph , 0 , parent))
    for i in range(nodes-1):
        u = MinKey(key , MstSet , nodes)
        MstSet[u] = 1
        for j in range(nodes):
            if(graph[u][j] and MstSet[j] == 0 and graph[u][j] < key[j]):
                parent[j] = u
                key[j] = graph[u][j]
                snapArray.append(snapshot(nodes , graph , 0 , parent))

    snapArray.append(snapshot(nodes , graph , 0 , parent))
    #print("final answer is:")
    #for i in range(1,nodes):
    #    print(parent[i],i,graph[i][parent[i]])
    returnResponse['error'] = False
    returnResponse['data'] = snapArray
    return JsonResponse(returnResponse)