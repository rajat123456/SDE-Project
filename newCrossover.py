#importing the file
import randoM
#importing the Bipartite graph
from genetic.data import bipartiteGraph
# importing the solution
from genetic.data import solution
# importing the crossover

def rtwheel():
        
        thrshold=9
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

def crossover10(solution1,solution2):

    
    # doing all process for merging the two graphs
    # getting the first graph
    graph1 = solution1.getGraph()
    #getting the second graph
    graph2 = solution2.getGraph()
    # merging the graph
    mergedGraph = graph1.merge(graph2)
     #merging the student edge
    stuEdges = mergedGraph.getStuEdges()
    #getting the edge of the merged graph
    supEdges = mergedGraph.getEdges()
     #taking the empty list
    cycles = []
     #trversing over the student Edge
    for stu in stuEdges:
        #traversing over the stuEdge
        for stu2 in stuEdges:
            #checking the condition
            if stu != stu2:
                #converting the into set
                n1 = set(stuEdges[stu])
                #converting into the set
                n2 = set(stuEdges[stu2])
                 #checking the condition
                if len(n1.intersection(n2))==2:
                    # appending into the list after making into the touples
                    cycles.append((stu,stu2))
     #returning the final value
    return cycles

