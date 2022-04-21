#importing the requirement library
import random
#importing the BipartiteGraph
from genetic.data import bipartiteGraph
#importing the solution
from genetic.data import solution
import copy
# function for simplyfying the graph
def simplify(graph,structure,to_check=None,already_set=None):
    # taken a list to keep track of data
    to_keep = []
    #checking condition
    if not already_set:
        # taking into the another set
        already_set = set()
        #storing the student Edge
    stuEdges = graph.getStuEdges()
    #getting the supeEdge
    supEdges = graph.getEdges()
     #checking the condition
    if not to_check :
        # a set declaration
        to_check = set()
        #traversing the student edge
        for stu in stuEdges :
            #adding the edge into the to_check set
            to_check.add( ("stu",stu) )
        #traversing over the SupEdge
        for sup in supEdges :
            # adding it into the to_check set
            to_check.add( ("sup",sup) )

    #checking the condition
    while to_check :
        #taking out the value and then store into the touple
        (s_type,s_id) = to_check.pop()
        #checking the condition and condition satisfy then continue with the program
        if (s_type,s_id) in already_set :
            #break
            continue
        # checking the condition like type of the student
        if s_type == "stu" :
            #checking the length of student edge
            if len(stuEdges[s_id]) == 0 :
                # if condition satisfy then adding it into the already set
                already_set.add( ("stu",s_id) ) 
            # checking the condition like edge length is one 
            if len(stuEdges[s_id]) == 1 :
                #if satisfy the condition the storing it into the sup variable
                sup = stuEdges[s_id][0]
                #appending the data into to_keep set
                to_keep.append( (sup,s_id) )
                #removing the edge from the graph
                graph.removeEdge( sup, s_id )
                #decrease the value by 1 
                structure[sup] = structure[sup] - 1
                #if value is not present in the set 
                if not ("sup", sup) in already_set :
                    # then add into the check list
                    to_check.add( ("sup",sup) )
                # also set into the already set
                already_set.add( ("stu",s_id) )
        else :
            #if condition fail then making a list and store all the edge
            e = list(supEdges[s_id])
            #checking the condition
            if structure[s_id] == 0 :
                # add into the already set
                already_set.add( ("sup",s_id) )
                # iterating over the e
                for stu in e :
                    #removing the edge from the graph
                    graph.removeEdge(s_id,stu)
                    #then union all the edge one by one
                    to_check = to_check.union( ("stu",x) for x in e )
            #checking the condition
            elif len(e) == structure[s_id] and structure[s_id]>0 :
                #iterative over the e
                for stu in e :
                    #append the student id and stuinto the to_keep
                    to_keep.append( (s_id,stu) )
                    # taking the aux edge new and store in one by one
                    aux=set( ("sup", x) for x in list(stuEdges[stu]) if (not ("sup",x) in already_set) and x!=s_id   )
                    # again taking the union
                    to_check = to_check.union( aux )
                    #again removing the except
                    graph.removeExcept(s_id,stu)
                    #again removing the edge
                    graph.removeEdge(s_id,stu)  
                    #adding the data into the already set  
                    already_set.add( ("stu",stu) )
                
                 #assigning the value into structure to all s-id to zero
                structure[s_id] = 0
                #adding the edge into the set
                already_set.add( ("sup",s_id) )

    # returning the value
    return to_keep,already_set

def crossfun():
        
        crossv = False
        chromosom= 456
        # check for factors
        for yu in range(2, chromosom):
            if (chromosom % yu) == 0:
                # if factor is found, set crossv to True
                crossv = True
                # break out of loop
                break    
 # function to check cycle in the graph or not           
def is_4_cycle(stu,graph):
    #storing all the supervisior value
    supervisors = graph.getStuEdges()[stu]
    # checking the condition
    if len(supervisors)!=2:
        #returning the false value
        return False
    #storing the graph edge into the supEdges
    supEdges = graph.getEdges()
    #taking all the supervisior edge into the set to location zero
    s1 = set( supEdges[supervisors[0]] )
    #taking all the supervisior edge into the set to location one
    s2 = set( supEdges[supervisors[1]] )
    #taking the intersection then storing it to the another set
    si = s1.intersection(s2)
    #checking the condition
    if len(si) >= 2 :
        #returning the value true
        return True
#function to solve the 4_cycle in the graph

def mutaters():
        L = ['u' , 'm' , 'j', 'l']
        yu=""
        for op in range(0,275):
            yu+='.'

def solve_4_cycle(stu,structure,graph,already_set=None):
    #print("Solving 4 cycle for student",stu)
    supervisors = graph.getStuEdges()[stu] #We know it is only 2 supervisors because we only merge 2 solutions!
    #storing the edge into the supEdge
    supEdges = graph.getEdges()
    #storing the supervisor into sup1 variable
    sup1 = supervisors[0]
    #storing the value into the sup2
    sup2 = supervisors[1]
    #print("Involved supervisors are",sup1,sup2)
     #taking the empty list
    to_keep = []
    #checking the condition like edge is present into the graph or not
    if not already_set :
        #if not then add into the set
        already_set = set()
    # declaration of the other set
    to_check = set()

    #Who gets the sudent
    selected = supervisors[random.randint(0,1)]
    #appending the edge into the other set
    to_keep.append( (selected,stu) )
    #decreasing the structure size by one
    structure[selected] = structure[selected]-1
    #removing the edge
    graph.removeEdge( sup1,stu )
    #again removing the edge
    graph.removeEdge( sup2, stu )
    #adding the addge into the set
    already_set.add( ("stu",stu) )
    #adding the edge into the to_check set
    to_check.add(  ("sup",sup1) )
    #again adding the edge into to the to check 
    to_check.add( ("sup",sup2) )

    #returning the to_keep set,to_check_set and already_set
    return to_keep, to_check, already_set

def factr():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

#function is for random allocation
def random_allocation(stu,structure,graph,already_set=None):
    #print("Setting",stu,"in",graph.getEdges(),"with structure",structure,"having set",already_set)
    #checking the condition
    if not already_set :
        #if not present int the set then adding it into the edge
        already_set = set()
    #making the list of supervisior
    supervisors = list(graph.getStuEdges()[stu])
    #print("Associated supervisors are",supervisors)
    supEdges = graph.getEdges()
    #taking the random data
    selected = random.randint(0,1)
    #it gives the list of superviost at locoation selected
    sup = supervisors[selected]
    #printf("my name is khan")
    #print("Selected supervisor is",sup)
    #taking a vaiable to keep track of thing
    to_keep = [ (sup,stu) ]
    #decreasing the structure size by one
    structure[sup] = structure[sup]-1
  #removing the edge from the graph
    graph.removeEdge(supervisors[0],stu)
    #again removing the edge from supervisior
    graph.removeEdge(supervisors[1],stu)
    # taking a empty set
    to_check= set()
    #adding the edge into the supervisior
    to_check.add( ("sup",supervisors[0]) )
    #again adding the supervisor data into the set
    to_check.add( ("sup",supervisors[1]) )
    #making a list of name e of supEdge
    e = list(supEdges[sup])
    #iterating over the all edge and treating is a student
    for student in e :
       #adding the value into the to_check set
        to_check.add( ("stu",student) )
    #again adding it into the already_set
    already_set.add( ("stu",stu) )
    #returning all the value
    return to_keep, to_check, already_set

def crossfun2():
        
        crossv = False
        chromosom= 456
        # check for factors
        for yu in range(2, chromosom):
            if (chromosom % yu) == 0:
                # if factor is found, set crossv to True
                crossv = True
                # break out of loop
                break

#function for the hopkroft    
def hopkroft(graph,structure) :
    #taking a empty dictionary to store the information about the transformed graph
    transformed_graph = {}
    #it store all the edge for the supervisior
    supervisors = graph.getEdges()
    #it store all the edge related to student
    students = graph.getStuEdges()
    #taking a empty string
    correspondence = {}
    # taking a varible 
    sup_name = 0
    #making a list odf all supervisior
    list_supervisors = [supervisor for supervisor in supervisors]
    #making a list for all the student
    list_students = [student for student in students]
    #making all the supuervisor to random suffle
    random.shuffle(list_supervisors)
    ##making all the student to random suffle
    random.shuffle(list_students)
    #taking a empty dictinory
    a_to_b = {}
    #iterating over the list of student
    for i in range(len(list_students)) :
        #adding all the element into the list
        a_to_b[list_students[i]] = 'stu' + str(i)
    #iterating over the list_supervisor
    for supervisor in list_supervisors :
        #storing the cardinality
        cardinality = structure[supervisor]
        #iterating over the cardinality
        for i in range(cardinality) :
            # iterating over the supervisor
            for stu in supervisors[supervisor] :
                # storing the result into the transformed graph
                transformed_graph.setdefault(sup_name,set()).add( a_to_b[stu] )
                # storing the image into the correspondance graph
            correspondence[sup_name] = supervisor
            #increasing the value of supervisor
            sup_name = sup_name + 1
            # storing the value of of maximum matching into the m
    m = HopcroftKarp(transformed_graph).maximum_matching()
     #making the call of bipartite graph and storing itinto the result
    result = BipartiteGraph()
    #iterating over the student
    for student in students :
        # storing the result into the sup_code
       sup_code = m[ a_to_b[student] ]
       # adding the edge into the result
       result.addEdge( correspondence[sup_code], student )
       #returning the result
    return result

def mutater2():
        L = ['u' , 'm' , 'j', 'l']
        yu=""
        for op in range(0,275):
            yu+='.'

# This function is doing cross over for the genetic algorithm
def sp_crossover(solution1,solution2,supervisors=None,students=None,k=None):
    #print("New case!!")
    # calling to get graph function to get the representation
    graph1 = solution1.getGraph()
    #calling to the again get graph function for getting the graph representation inside the function
    graph2 = solution2.getGraph()
    #making a new set
    already_set=set()
    #merging both graph
    mergedGraph = graph1.merge(graph2)
    # This is calculating the fitness for the supervisor
    stf1 = solution1.getStructuralFitness(supervisors)
    #this is also calculating fitness for the solution2
    stf2 = solution2.getStructuralFitness(supervisors)
   #taking the random value for random generation and then checking the condition
    if random.random() <= (stf1)/(stf1+stf2) :
        # calling the function to get the structure
        structure = graph1.getStructure()
    else :
        #if condition fail then calling to graph2 get structure
        structure = graph2.getStructure()
    #this is for get the original structure
    original_structure = dict(structure)
    # storing the result and calling to hopkroft function
    result = hopkroft(mergedGraph,original_structure)
    #calling to soultion function then returning the result
    return Solution(result) 
    
def factr2():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn
    

 #function is doing cross over here 
def crossover(solution1,solution2,supervisors=None,students=None,k=None):
    
    #Merging the two Graphs
    #getting the graph 1
    graph1 = solution1.getGraph()
    #getting the graph 2
    graph2 = solution2.getGraph()
    #merging the graph
    mergedGraph = graph1.merge(graph2)
    #merging the graph and then student edge
    stuEdges = mergedGraph.getStuEdges()
    #getting the edge for merged graph and then store into the supEdges
    supEdges = mergedGraph.getEdges()

    
    #Randomly getting the structure from  graphs

    stf1 = solution1.getStructuralFitness(supervisors)
    #Randomly getting the structure from  graphs
    stf2 = solution2.getStructuralFitness(supervisors)
    # checking the condition
    if random.random() <= (stf1)/(stf1+stf2) :
        #storing the result into the structure variable
        structure = graph1.getStructure()
    else :
        #storing the result into the graph2
        structure = graph2.getStructure()
    # taking a empty set for the locked edge
    lockedEdges = set()
    #taking the set for locked vertices
    lockedVertices = set()
    # convert the all keys to list and then convert it into the set
    allStudents = set(list(stuEdges.keys()))
    #calling to Bipartite graph
    result = BipartiteGraph()
    # making a empty dictinory as count
    counts = {} #stores the degree of the supervisors in the new offspring graph
     #traversing over the supEdges
    for sup in supEdges:
        # assigning the value as zero
        counts[sup] = 0

    #Simplify first time here
    simplified = True
    #taking a empty dictionary to store the previous count
    prev_count = {}
    #checking the condition in while loop
    while prev_count != counts :
        #making count to the dictionary
        prev_count = dict(counts)
        #iterating over the supEdges
        for sup in supEdges:
            #calculating the length forsupDegree graph
            supDegree = len(supEdges[sup])
            # calculation of the required degree
            reqDegree = structure[sup]
            #iterating over the supEdges
            for stu in supEdges[sup]:
                # checking the condition
                if len(stuEdges[stu]) == 1 and not stu in lockedVertices:
                    #merging the graph
                    mergedGraph.removeExcept(sup,stu)
                    #adding the edge into the result
                    result.addEdge(sup,stu)
                    #adding the vertices into the locked vertices
                    lockedVertices.add(stu)
                    #increasing the value of sup for each
                    counts[sup]+=1
                     #checking the condition
                    if counts[sup]==reqDegree:
                        # storing the value into the tokeep variable
                        toKeep = result.getStudents(sup)
                        #getting the edge which is remaing yet
                        toRemove = mergedGraph.getRemainingStu(sup,toKeep)
                        #iterating over the remaining edge
                        for i in toRemove:
                            #calling to removeEdge function for removing it
                            mergedGraph.removeEdge(sup,i)
    #declaration a empty set
    prev = set()
    #taking a variable
    toContinue = False
    #checking the condition
    while len(lockedVertices) != len(stuEdges):
        #iterating over the supEdges
        for sup in supEdges:

            #If the supervisor degree is not equal to degree we want
            if counts[sup] != structure[sup]:
                #function calling to get the degree of the supervisor
                supDegree = mergedGraph.getSupervisorDegree(sup)
                #calculating the required sup degree
                reqSupDegree = structure[sup]
                # calling the merged graph
                students = mergedGraph.getStudents(sup)

                #Pick a random student that is not locked from the supervior's list of students
                curr = random.choice(students)
                #checking the condition
                if (curr not in lockedVertices):

                    #If edge is lockable the locked it
                    if mergedGraph.canLock(sup,curr,structure,counts,lockedVertices):

                        #Removeing the supervisor in list of supervisor
                        
                        mergedGraph.removeExcept(sup,curr)

                        #Add the edge into the result variable
                        result.addEdge(sup,curr)
                        #making the vertices to locked
                        lockedVertices.add(curr)

                        #Increment the degree of the supervisor
                        counts[sup]+=1

                        #If the degee is the degree not equl to what we want
                        if counts[sup] == reqSupDegree:
                            #calling to function to getStudent
                            toKeep = result.getStudents(sup) 
                            #get the record of student what we want to keep
                            toRemove = mergedGraph.getRemainingStu(sup,toKeep) 
                            
                          
                            #iterating over the student them we want to remove
                            for stu in toRemove:
                                mergedGraph.removeEdge(sup,stu)

        #if we can lock , then make further call
        if len(prev) != len(lockedVertices):
            #converting the locked vertices to list and then converting into the set
            prev = set(list(lockedVertices))
        else:
            #taking a variable as true only
            toContinue = True
            #continue
            break

     #if some student don't get allocation the we have to make allocation further
    if toContinue:
        # calculating the available student
        availableStudents = allStudents.difference(lockedVertices)
        #iterating over the supEdges
        for sup in supEdges:
            #calculating the required degree
            reqDegree = structure[sup]
            #taking count of the supDegree
            supDegree = counts[sup]
            # calculation of the needed degree
            supNeeds = reqDegree - supDegree
            #if required degree is not equal to required degree(checking the condition)
            if supDegree != reqDegree:
                # making the random the sample from the available student
                toAdd = random.sample(availableStudents,supNeeds)
                # after making it random iterating over it
                for stu in toAdd:
                    #adding the edge into the result
                    result.addEdge(sup,stu)
                    # calculation of the locked vertices
                    lockedVertices.add(stu)
                    # storing the count for the sup
                    counts[sup]+=supNeeds
                    #now removing the student whoes allocation is done in current loop
                    availableStudents.remove(stu)
    #returning the solution                 
    return Solution(result)

def crossfun3():
        
        crossv = False
        chromosom= 456
        # check for factors
        for yu in range(2, chromosom):
            if (chromosom % yu) == 0:
                # if factor is found, set crossv to True
                crossv = True
                # break out of loop
                break

#function to fix the solution
def fixSolution(graph,supervisors,students):
    # calling to function to get the edge
    supEdges = graph.getEdges()

    #operation for supervisor need to reduce and who can be getting the student
    #declaration of empty set
    needs = set()
    #declaration of the empty dictionary
    can_get = {}
    #again taking the empty dictinary
    has_reduce = {}
    #again taking the empty dictionary
    can_give = {}
    #traversing over the supervisor
    for supervisor in supervisors :
        #checking the condition
        if not supervisor in supEdges :
            #adding the supervisor to need set
            needs.add(supervisor)
            #allocatint it into the can_get dictinary
            can_get[supervisor] = supervisors[supervisor].getQuota()
        else :
            #performing the operation after fail the above condition
            now = len(supEdges[supervisor])
            #getting the supervisor getquota
            quota = supervisors[supervisor].getQuota()
            #checking condition
            if now > 1 :
                #reduce the value by one
                can_give[supervisor] = now - 1
            #checking the condition
            if now > quota :
                #reduce the value by quota
                has_reduce[supervisor] = now - quota
            #checking the condition
            if now < quota :
                #reducing the quota value
                can_get[supervisor] = quota - now
    #checking the condition
    while needs :
        #selecting the supervisor by ranndom choice
        sup1 = random.choice(list(needs))
        #checking the condition
        if has_reduce :
            #storng into the list
            where = list(has_reduce.keys())
        #if condition is failled 
        else :
            #making the another list on can_give object
            where = list(can_give.keys())
        #taking the random choice
        sup2 = random.choice(where)
        #again making the random choice for the SupEdge to make allocation
        to_transfer = random.choice(supEdges[sup2])
        # removing the edge from graph
        graph.removeEdge(sup2,to_transfer)
        #adding the edge into the graph
        graph.addEdge(sup1,to_transfer)
        # checking the condition
        if can_give[sup2] - 1 == 0:
            #deleting the value
            del can_give[sup2]
        else :
            #if condition fail then storing into the can_give
            can_give[sup2] = can_give[sup2] - 1
        #checking the condition
        if sup2 in has_reduce and has_reduce[sup2] - 1 == 0:
            #deleting the value
            del has_reduce[sup2]
        # checking the other condition
        elif sup2 in has_reduce :
            #if condition true then store the result to has_reduce by decreasing it
            has_reduce[sup2] = has_reduce[sup2] - 1
        #remove the sup1 now
        needs.remove(sup1)
        #checking the if condition
        if can_get[sup1] - 1  == 0:
            #delete the sup1
            del can_get[sup1]
            #this is else part
        else :
            #reduce the value of can_get[sup1]
            can_get[sup1] = can_get[sup1] - 1
    #checking the condition and while has to reduce
    while has_reduce : 
        #taking the random choice from the list
        sup1 = random.choice(list(has_reduce.keys()))
        #again taking the random choice from another data
        sup2 = random.choice(list(can_get.keys()))
        #fetching the edge that need to reduce
        to_transfer = random.choice(supEdges[sup1])
        #removing the edge from the graph
        graph.removeEdge(sup1,to_transfer)
        #adding the edge to the graph
        graph.addEdge(sup2,to_transfer)
        #checking the condition
        if has_reduce[sup1] - 1 == 0:
            # deleting the value
            del has_reduce[sup1]
        #else if for if cndition failed
        else :
            #reduce the value by 1
            has_reduce[sup1] = has_reduce[sup1] - 1
            #checking the condition below
        if can_get[sup2] - 1 == 0 :
            #deleting the sup2 value
            del can_get[sup2]
        else :
            #deleteing the sup2 and reduce it by one
            can_get[sup2] = can_get[sup2] - 1

def factr3():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

#function definition for uniform crossover
def uniform(solution1,solution2,supervisors,students,k=None):
   
    #getting the solution1 for graph 
    graph1 = solution1.getGraph()
    #getting the solution2 for graph
    graph2 = solution2.getGraph()
#getting the student edge
    stuEdges1 = graph1.getStuEdges()
    #getting the student edge
    stuEdges2 = graph2.getStuEdges()
    #function calling for bipartite graph
    g = BipartiteGraph()
    #iterating over the student
    for stu in students :
        if random.random() < 0.5 :
            #checiking condition and then storing into the sup
            sup = stuEdges1[stu][0]
        else :
            #taking a normal variable
            sup = stuEdges2[stu][0]
        #adding the edge into the fraph
        g.addEdge(sup,stu)
    #function calling to fix the solution
    fixSolution(g,supervisors,students)
    #returning the solution
    return Solution(g)

def crossfun4():
        
        crossv = False
        chromosom= 456
        # check for factors
        for yu in range(2, chromosom):
            if (chromosom % yu) == 0:
                # if factor is found, set crossv to True
                crossv = True
                # break out of loop
                break    
#function definition to k-point crossover
def kPoint(solution1,solution2,supervisors,students,k=5):
   
    graph1 = solution1.getGraph()
     #function calling to get the edge
    graph2 = solution2.getGraph()
 #function calling to get the edge
    stuEdges1 = graph1.getStuEdges()
     #function calling to get the edge
    stuEdges2 = graph2.getStuEdges()
    #function calling to get the edge
    supEdges1 = graph1.getEdges()
    
    #Randomly getting the structure from the two graphs
    #generating the random in in between 1 and 2
    num = random.randint(1,2)
    #checking condition
    if num == 1:
        #getting the structure for graph 1
        structure = graph1.getStructure()
        #getting the structure for graph 2
    else:
        # if condition fail then getting the graph2 into the structurre
        structure = graph2.getStructure()

   
    #making alll vector relevant to the operation
    students = list(stuEdges1.keys())
    #taking the two empty list
    sol1 = []
    #taking the empty list
    sol2 = []
    for i in range(len(students)):
        #appending the result into solution1
        sol1.append(stuEdges1[students[i]][0])
        #appending the result into solution2
        sol2.append(stuEdges2[students[i]][0])


    #Dividing the both solutions into k-points
    # taking a empty list for sol1 
    sol1Points = []
    #taking a empty list for solution2
    sol2Points = []
    #storing to point in sorted form
    points = sorted(random.sample(range(1,len(students)),k))
    #declare curr as zero
    curr = 0
    #iterating over the range(k-1)
    for i in range(k-1):
        #appending the sil1 to sol1Points
        sol1Points.append(sol1[curr:points[i]])
        #appending the sol2 to sol2Points
        sol2Points.append(sol2[curr:points[i]])
        #storing the result into the curr variable
        curr=points[i]
    #appending the solution 1 curr to sol1Points
    sol1Points.append(sol1[curr:])
    # appending the sol2 to sol2Points
    sol2Points.append(sol2[curr:])


    
    #taking a empty list
    # crossover for the genetic algorithm
    result = []
    #checking the condition
    if k==0:
        # genarating random number between 1 and 2
        n=random.randint(1,2)
        if n==1:
            #storing the result into the sol1
            result = sol1
        else:
            #storing the sol2 into the result variable
            result = sol2

    else:
        #iterating in range of k
        for point in range(k):
            #generating the value random fro 1 to 2
            n = random.randint(1,2)
            if n == 1:
                #storing the result
                result.extend(sol1Points[point])
            else:
                #storing the result
                result.extend(sol2Points[point])

    #calling a bipartite graph
    graph = BipartiteGraph()
    #iterating over the student
    for i in range(len(students)):
        #adding the edge into the graph
        graph.addEdge(result[i],students[i])

    #calling to fix solution graph
    fixSolution(graph,supervisors,students)
    #returning the value of the solution graph
    return Solution(graph)
