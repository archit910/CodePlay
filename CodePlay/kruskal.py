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

def styleCreator(nodes,selector, color,type):
    print("in style creator function for type!!",type,color)
    returnStyle = OrderedDict()
    returnStyle['selector'] = selector
    returnStyle['style'] = OrderedDict()
    if (type=="node"):
        returnStyle['style']['background-color'] = color
    else:
        returnStyle['style']['line-color'] = color
    # print returnStyle
    return returnStyle

def createSelector(nodes,type,*elements):
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
			#print(i,j,nodes)
			if(grid[i][j]):
				edgeArray.append({'data':{'id':"e"+str(i+1)+str(j+1),'source':'n'+str(i+1),'target':'n'+str(j+1)}})
	return edgeArray

def elementCreator(nodes,grid):
    elements = OrderedDict()
    elements['nodes'] = getNodes(nodes)
    elements['edges'] = getEdge(nodes,grid)
    return elements


def snapshot(nodes,graph,*arguments):
    returnData = OrderedDict()
    returnData['style']=list(snapArrayDefault['style'])
    returnData['elements'] = elementCreator(nodes,graph)
    returnData['line'] = arguments[0]
    #print("pro pro pro")
    #print(len(arguments))
    try:
        if(arguments[1]):
            temp=[]
            ResultantMst=arguments[1]
            print(ResultantMst)
            for i in range(len(ResultantMst)):
                #print(ResultantMst[i][0],ResultantMst[i][1])
                temp.append(ResultantMst[i][0])
                temp.append(ResultantMst[i][1])
                returnData['style'].append(styleCreator(nodes,createSelector(nodes,"edge",ResultantMst[i][0]+1,ResultantMst[i][1]+1),visitedColour,"edge"))
            print(temp)
            for i in temp:
                returnData['style'].append(styleCreator(nodes,createSelector(nodes,"node",i+1),currentColour,"node"))
    except:
        pass
    returnData['arr'] = []
    return returnData

def ChangeGraph(graph , nodes):
    grid=[]
    for i in range(nodes):
        for j in range(nodes):
            if( graph[i][j]):
                grid.append( [i , j , graph[i][j] ])
    return grid


def FindParent(parent , key):
    if(parent[key] == key):
        return key
    return FindParent(parent , parent[ key ])


def FindUnion(rank , parent , u , v):
    ParentU=FindParent(parent , u)
    ParentV=FindParent(parent , v)
    if(rank[ParentU] > rank[ParentV]):
        parent[ParentU] = ParentV
    elif(rank[ParentV] > rank[ParentU]):
        parent[ParentV] = ParentU
    else:
        parent[ParentV] = ParentU
        rank[ParentU] += 1


def KruskalMinimumSpanningTree(grid , nodes):
    #print(graph[1],graph[2],graph[3])
    global snapArray
    snapArray = []
    returnResponse = OrderedDict() 
    snapArray.append(snapshot(nodes , grid , 0))
    graph = ChangeGraph(grid , nodes)
    graph = sorted(graph , key = lambda item : item[2])
    rank = [0] * (nodes+1)
    parent = [0] * (nodes+1)
    ResultantMst = []
    start = 0
    for i in range(nodes+1):
        parent[i] = i
    #print(rank)
    #print(parent)
    i=0
    while(start < nodes-1):
        #print("here for ",i,graph[i])
        u , v , weight = graph[i]
        i = i + 1
        #print("i is:",i)
        ParentU = FindParent(parent , u)
        ParentV = FindParent(parent , v)
        #print("i is:",i)
        if(ParentU != ParentV):
            start = start+1
            ResultantMst.append( [ u , v , weight ] )
            FindUnion(rank , parent , ParentU , ParentV)
    #print(ResultantMst) 
    snapArray.append(snapshot(nodes , grid , 0 , ResultantMst))
    returnResponse['error'] = False
    returnResponse['data'] = snapArray
    print("I am in kruskal return response!!")
    print(len(returnResponse))
    print("end of return response")
    return JsonResponse(returnResponse)