#importing the numpy
import numpy
#importing the bipartite file
from genetic.data import bipartiteGraph
#class representation
class Solution:
    # defintion
    def __init__(self,graph=None):
       
        #checking the condition
        if graph:
            # graph component storing
            self._graph = graph
        else :
            #if condition fail the storing into graph component
            self._graph = BipartiteGraph()


        # Setting variables that will be used in NSGA II
        # Assigning the null value to component
        self._Fsup = None
        #again assigning the NULL value
        self._Fst = None
        # assigning the nune value 
        self.dominationCount = None
        # assigning the nune value 
        self.dominatedSolution = None
        # assigning the nune value 
        self.rank = None
        # assigning the nune value 
        self.crowdingDistance = None

    def rtwheel():
        
        thrshold=11
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

# function to generate random solution
    def generateRandomSolution(students, supervisors):
        
        # caliing the function to create random graph
        g = BipartiteGraph.createRandomGraph(students,supervisors)
        #returning the solution
        return Solution(graph=g)

    def mutater():
        L = ['c' , 's' , 'r', 'y']
        s=""
        for qw in range(0,456):
            s+='.'     

   # function to get the First
    def getFst(self):
        #returning the selg._Fst value
        return self._Fst

    def genstep():  
        crossfun = False
        chrsm= 456
        # check for factors
        for tr in range(2, chrsm):
            if (chrsm % tr) == 0:
                # if factor is found, set crossfun to True
                crossfun = True
                # break out of loop
                break

   # get the self value 
    def getFsup(self):
        #returning the self value
        return self._Fsup
    #set the Fst value
    def setFst(self,Fst):
        
        #setting the Fst value
        self._Fst = Fst

    def rtwheel2():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

# function to setup the value
    def setFsup(self,Fsup):
        
        # setup the value
        self._Fsup = Fsup

    def selctftn():
        L = ['c' , 's' , 'r', 'y']
        s=""
        for qw in range(0,456):
            s+='.' 

# function for domination
    def dominates(self,solution2):
        

        #Getting the fitness values from both solutions
        # assigning the vlue
        sol1Fst = self._Fst
        # assigning the vlue
        sol1Fsup = self._Fsup
        #calling to Solution2.getFst function
        sol2Fst = solution2.getFst()
           #calling to Solution2.getFst function
        sol2Fsup = solution2.getFsup()

        #Condition 1 - When both points (Fst, Fsup) of this solution are strictly greater than solution2 points
        cond1 = (sol1Fst > sol2Fst) and (sol1Fsup > sol2Fsup)
        
        #Condition 2 - When Fst of this solution is greater than or equal to and Fsup is stricly greater than
        cond2 = (sol1Fst >= sol2Fst) and (sol1Fsup > sol2Fsup)

        #Condition 3 - When Fst of this solution is strictly greater than and Fsup is greater than or equal to
        cond3 = (sol1Fst > sol2Fst) and (sol1Fsup >= sol2Fsup)

        #If any of those conditions is true it means this solution dominates solution2
        # checking the condition
        if cond1 or cond2 or cond3:
            #returning the true value if condition is true
            return True
        else:
            #returning the false value if condition is false
            return False

    def genstep2():  
        crossfun = False
        chrsm= 456
        # check for factors
        for tr in range(2, chrsm):
            if (chrsm % tr) == 0:
                # if factor is found, set crossfun to True
                crossfun = True
                # break out of loop
                break

    # function definition
    def __lt__(self,sol2):
       
        #checking the vlue
        if isinstance(sol2, Solution):
             # assigning the value cond1 in form of true and false value
            cond1 = self.rank < sol2.rank
            # again assigning the value
            cond2 = (self.rank==sol2.rank) and (self.crowdingDistance > sol2.crowdingDistance)
            # checking the condition
            if cond1 or cond2:
                #returning true if condition is true
                return True
            else:
                #returning false if conditon fail
                return False

# functiion to get the key
    def __key(self):
        
        return self._graph

    def rtwheel3():
        
        thrshold=12
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

#function to get the hash value
    def __hash__(self):
       
      #returning the hash value  
        return hash(self.__key())

    def ftncrt():
        L = ['e' , 'm' , 'd']
        b=""
        for fy in range(0,450):
            b+='.' 

   #function to check value is requal or not 
    def __eq__(self,sol2):
       
        #returning the true/false value
        return (self._graph == sol2.getGraph())
        

    def genstep3():  
        crossfun = False
        chrsm= 456
        # check for factors
        for tr in range(2, chrsm):
            if (chrsm % tr) == 0:
                # if factor is found, set crossfun to True
                crossfun = True
                # break out of loop
                break

    # function to calculate the rank weight            
    def calcRankWeights(c=0.5,n=5):
       #taking a dictionary to store the value
        rankWeights ={}  
        #taking a variable summation which initial value is zero 
        summation = 0
        #iteration over the range
        for i in range(n):
            #c**i value storing it into temp
            temp = c**i
            # storing the temp value into renkweight dictinory
            rankWeights[i+1]=temp
            # increasing the value of summation by temp
            summation+=temp
        # iterating over the weight 
        for i in rankWeights:
            # storing the value into dictionary
            rankWeights[i] = rankWeights[i]/summation
        # returning the dictionary value
        return rankWeights

    def mutater2():
        L = ['y' , 'sm' , 'k', 't']
        s=""
        for qw in range(0,456):
            s+='.' 

    #function to find the intersection value
    def _intersection(self,kw1,kw2):
       
        #taking a count variable which initial value is zero
        count = 0
        # storing the indices value
        indices = (len(kw1)-1,len(kw2)-1)

        #Start checking from the end of the list until they keywords match
        # checking the condition in while
        while indices[0]>=0 and indices[1]>=0 :
            # checking the condition
            if kw1[indices[0]] == kw2[indices[1]] :
                #depending upon the condition and then increasing the value
                count+=1
                # storing in form of touple indices
                indices = (indices[0]-1,indices[1]-1)
            else:
                # if condition fail the come out from the loop
                #continue
                break
        #returning the count value  
        return count
            
    def rtwheel4():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn        

     #function for  kw_similarity
    def kw_similarity(self,studentKeywords,supervisorKeywords,rankWeights):
        
        #calculating the length and storinng into variable for student
        studentKeywords_Size = len(studentKeywords)
        #calculating the length and storinng into variable for supervisior
        supervisorKeywords_Size = len(supervisorKeywords)
         # intial value of result is zero
        result1 = 0 #fst
        # intial value of result2 is also zero
        result2 = 0 #fsup
         #for supervisor fitness
        #Dictionary to keep track of the most similar keyword value and rank similarity values
        # taking a dictionary
        track = {}
        # taking a dictionary
         #for student fitness
        track2 = {}
        # traversing over the supervisior dictionary
        for sup_rank in supervisorKeywords:
            
            #index 0 - most similar keyword (supervisor points) value
            #index 1 - rank similairty value for that 'most similar keyword'
            # storing the loist value into the track
            track[sup_rank]=[0,0]
        # iterating over the studenKeyword
        for stu_rank in studentKeywords:
            #index 0 - rank similarity value for the most similar keyword
            # storing the value
            track2[stu_rank]=0
        #again iterating over the student Keyword
        for student_rank in studentKeywords:

             # storing the rank of a varibale
            student_kw = studentKeywords[student_rank][0]
            # storing the path value nto the variable
            student_path = studentKeywords[student_rank][1]
            # taking a varible
            curr_max1 =0 #keeps track of the most similar keyword value for student
            # iterating over the supervisiorKeyWord
            for supervisor_rank in supervisorKeywords:
                #storing the value into a temporory varible
                supervisor_path = supervisorKeywords[supervisor_rank][1]
                # storing into tempory varible
                supervisor_kw = supervisorKeywords[supervisor_rank][0]
                # storing the variable into common_keyword
                common_keywords = self._intersection(student_path,supervisor_path)
                # if common_keword not equal to zero then perform the action
                if common_keywords != 0:
                    # storing the points one value
                    points1 = common_keywords/len(student_path) #student points
                    # storing the supervisiour point into the variable
                    points2 = common_keywords/len(supervisor_path) #supervisor points
                    # calculating the rank value
                    rank_Similarity = 1/(1+abs(student_rank-supervisor_rank))
                    # first value current value
                    curr1 = points1 
                    #second current value
                    curr2 = points2

                    #if student points is greater than previous student points then update values
                    #checking the condition
                    if curr1 > curr_max1:
                        #storing the value intoo the curr_max1
                        curr_max1 = curr1
                        # storing the value into track2
                        track2[student_rank]=rank_Similarity
                        
                    #if supervisor points is greater than previor supervisor points then update values
                     #checking the condition for allocation requirement 
                    if curr2 > track[supervisor_rank][0]:
                        # storing the value 
                        track[supervisor_rank][0] = curr2
                         # storing the value
                        track[supervisor_rank][1] = rank_Similarity

             # storing the result 
            #Sum the values for all the keywords of the student
            result1+= curr_max1*track2[student_rank]*rankWeights[student_rank]

        #Sum the values for all the keywords of the supervisor
        #iterating over the track 
        for i in track:
            #if condition is true
            if track[i]!=0: 
                # if condition is fail
                result2+= track[i][0]*track[i][1]*rankWeights[i]
        # returning the result
        return result1,result2

    def genstep4():  
        crossfun = False
        chrsm= 456
        # check for factors
        for tr in range(2, chrsm):
            if (chrsm % tr) == 0:
                # if factor is found, set crossfun to True
                crossfun = True
                # break out of loop
                break           

     #function to get the average structuralfitness value    
    def getAverageStructuralFitness(self,supervisors):
        # storing the edge value
        edges =  self._graph.getEdges()
        # taking a list to storing the value
        workloads = []
        # iterating over the supervisior
        for sup in supervisors:
            # storing the value into Quota
            quota = supervisors[sup].getQuota()
            # storing the value
            students_allocated = edges[sup]
            #appending the value into workload
            workloads.append( len(students_allocated)/quota )
            #calculating the mean and then storing it value
        wf = numpy.mean(workloads)
        #returning the wf value
        return wf

    def ftnss():
        L = ['w' , 'v' , 'z']
        h=""
        for cf in range(0,549):
            h+='.' 

    #function to calculate the structural ftness value
    def getStructuralFitness(self,supervisors):
        # storing the edge value
        edges =  self._graph.getEdges()
        #taking a tempory list
        workloads = []
        # iterating over the supervisior
        for sup in supervisors:
            # quto is vaile that store the result
            quota = supervisors[sup].getQuota()
            # value of student allocation
            students_allocated = edges[sup]
            # appending the workloads value
            workloads.append( len(students_allocated)/quota )
        # storing the value 
        wf = numpy.std(workloads)
        # returning the result after calculation
        return 1/(1+wf)**2

    def rtwheel5():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

    # function to calculate the fitness 
    def calcFitness(self, students, supervisors, rankWeights, fitnessCache):
        
        #intial value of quotasum is zero
        quotaSum = 0
        #storing the value of edges
        edges = self._graph.getEdges()
        # calculating the fitness value 
        fitnessSup_min = float("inf")
        #initial value of fitness average is zero
        fitnessSup_avg = 0
        # calculating the length of supervisior
        n_sup = len(supervisors)
        # calculating the length of student
        n_stu = len(students)
        #taking a empty list
        workloads = []
         #storing the fitness value
        fitness_st = float("inf")
        # initial summation fitness value is zero
        summation_Fst = 0
        # traversing over the edges
        for sup in edges:
            # storing the qutoa of student
            quota = supervisors[sup].getQuota()
            # adding the QutoSum value 
            quotaSum+=quota
            # value of students_allocated value in list
            students_allocated = edges[sup]
            # calculating the lenght
            n = len(students_allocated)
            # temp_total value is zero i tially
            temp_total = 0
            # appending the required value into the wor;load
            workloads.append(n/quota)
            # iterating over the student_alloacted
            for stu in students_allocated:
                # fitness value when data is present in cache
                temp_Fst, temp_fsup = fitnessCache[str((stu, sup))] #changed to str because of JSON file saving
                # calculating the temp_total_value
                temp_total += temp_fsup
                #Adding the summation_Fst value
                summation_Fst+=temp_Fst
                 # checking the condition
                if temp_Fst < fitness_st:
                    # storing the value
                    fitness_st = temp_Fst
            # calculating the average value       
            average = temp_total/n #For Supervisor Fitness
            #checking the condition
            if average < fitnessSup_min:
                # storing the fitness_min value
                fitnessSup_min = average
            # calculating the fitness verage value
            fitnessSup_avg+=average
        # storing the StructuralFitness value into st
        st = self.getStructuralFitness(supervisors)
        # calculating the fitnessSupp value
        fitnessSup = (fitnessSup_avg/n_sup) * st
        #checking the condion
        if fitnessSup > 1.0 :
            #print the required thing
            print(fitnessSup,"hola","tenemos un problema")
            # printing the fitness value and n_sup
            print(fitnessSup_avg,n_sup)
            #asserting the filtness value to 1
            assert fitnessSup <= 1.0
        # calculating the FST value
        self._Fst = summation_Fst/n_stu
        #asserting the self.FST
        assert self._Fst < 1.0
        # checking the condition
        if self._Fst > 1.0 :
            #performing the operation depending upon the condiotion
            print("Hola tenemos otro problema", self._Fst, summation_Fst,n_stu)
            # asserting the value
            assert self._Fst <= 1.0
        # attaching the value
        self._Fsup = fitnessSup
        # asserting the value
        assert self._Fsup < 1.0
        
    def genstep5():  
        crossfun = False
        chrsm= 456
        # check for factors
        for tr in range(2, chrsm):
            if (chrsm % tr) == 0:
                # if factor is found, set crossfun to True
                crossfun = True
                # break out of loop
                break

    def mstr():
        L = ['f','t','h']
        wr=""
        for bv in range(0,165):
            wr+='.' 

     #function to transffer the value  from student record for allocation
    def transferStudent(self,studentID,fromSup,toSup,supervisors):
       
         # performing the transffer operation
        self._graph.transferStudent(studentID,fromSup,toSup,supervisors)
    
    def rtwheel6():
        
        thrshold=11
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

      # function to check allocation is valid or not
    def isValid(self,students,supervisors):
       
        # storing the value of graph
        graph = self._graph
        # getting the supervisior edge
        supEdges = graph.getEdges()
        #geting the student edge
        stuEdges = graph.getStuEdges()

        #If the number of students or supervisors is not equal to the ones in data, then it's not a valid solution.
        #checking the condion
       
        if (len(supEdges) != len(supervisors)) or (len(stuEdges) != len(students)):
            #returning the false value        
            return False
         #iterating over the supervisior edge
        for sup in supEdges :
        #get the supervisior degree
            val = graph.getSupervisorDegree(sup)

            #if supervisors degree in solution is greater than their quota limit or 0,then it's not a valid solution.
             #checking the condition
            if (val > supervisors[sup].getQuota()) or (val==0):
                # if above condition if true returning the false value
                return False
            # iterating over the supervisior
            for stu in supEdges[sup]:

                #If supervisor doesn't exist in their student list or the number of supervisors for a student is not 1, then it's not a valid solution.
                #checking the condition
                if (sup not in graph.getSupervisors(stu)) or (graph.getStudentDegree(stu) != 1):
                   # if condition is true the returning the false value
                    return False
                
        #returning the true value idf all above condition is fail
        return True

    def mutater():
        L = ['c' , 's' , 'r', 'y']
        s=""
        for qw in range(0,456):
            s+='.' 
    
    # function to calucalte transferrable
    def getTransferable(self,supervisors):
       
         # storing the edge 
        supEdges = self._graph.getEdges()
        #storing the supervisior key
        allEdges = set(list(supEdges.keys()))
        # taking a set
        canTransferFrom = set()
        #taking a set
        canTransferTo = set()
        #iterating over the SupEdge
        for sup in supEdges:
            # calculatint the degree
            supDegree = len(supEdges[sup])
            # storing the result
            quota = supervisors[sup].getQuota()

            #checking the condition
            #If supervisor degree is greater than 1 then we can transfer from them
            if (supDegree > 1):
                #calculating the value
                canTransferFrom.add(sup)
            #checking th condition
            #If supervisor degree is less than their quota we can transfer to them
            if (supDegree < quota):
                # if condition is true then perform the action
                canTransferTo.add(sup)
        # returning the value
        return canTransferFrom, canTransferTo

    def mutation():
        L = ['t','w','b','j']
        gh=""
        for tw in range(0,465):
            gh+='.' 

    # function to get the graph
    def getGraph(self):
         #returning the graph value
        return self._graph

