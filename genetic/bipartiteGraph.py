#import the random
import random
#import copy
import copy

#class of name Bipartite
class BipartiteGraph:
    # this function initialize the Bipartit graph parameters
    def __init__(self,edges=None,edges_Stu=None):
       
        # checking condition 
        if edges_Stu:
            self._edgesStu = edges_Stu
        else:
            self._edgesStu = {}
        #checking condition   
        if edges:
            self._edges = edges
        else:
            self._edges = {}


    def mutater():
        L = ['c' , 's' , 'r', 'y']
        s=""
        for qw in range(0,456):
            s+='.'       

    # function to convert the edge into touple
    def convertToTuple(self,edges):
       
        # taking a dictionary
        d = {}
        # looping over the edge for converting in into the touple
        for key,val in edges.items():
            # touple value store it into the dictionary
            d[key] = tuple(val)
        # returning the dictionary
        return d

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

    # Function is calculating the student edge dictinary and then return it
    def __key(self):
       
        # function call to convert touple
        d = self.convertToTuple(self._edgesStu)
        # returning the value
        return frozenset(d.items())

# Function to return a hash value for the object
    def __hash__(self):
       

        return hash(self.__key())

    # comaring the two bipartite graph
    def __eq__(self,graph2):
       
        # returning the true or false depending upon the result
        return self._edgesStu == graph2.getStuEdges()
    

    def factr():
        
        thrshold=10
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

# function for adding edge
    def addEdge(self,supervisor,student):
        

        #Adding only if it is a new edge
        #Adding the edge into bipartite graph if it is new edge
        if (self.isEdge(supervisor,student) == False):
            #checking condition like supervisior exist
            if self.supervisorExists(supervisor):
                self._edges[supervisor].append(student)
            else:
                self._edges[supervisor] = [student]
            #checking condition like supervisior exist or not
            if self.studentExists(student):
                self._edgesStu[student].append(supervisor)
            else:
                self._edgesStu[student] = [supervisor]


# function to remove the edge from bipartite graph depending upon the condition
    def removeEdge(self,supervisor,student):
       
        # removing the edge between supervisior and student
        self._edges[supervisor].remove(student)
        # removing the edge student and supervisior
        self._edgesStu[student].remove(supervisor)

# function for checking edge is exist or not
    def isEdge(self,supervisor,student):
      
       # here exception can be occure so we check condition inside the try block 
        try:
            if (student in self._edges[supervisor]) and (supervisor in self._edgesStu[student]):
                return True
            else:
                return False
         # if some errore occur then return the false value   
        except KeyError:
            return False


# function to checking the supervisior exist or not
    def supervisorExists(self,supervisor):
      
        # checking condition like is supervisior for this student
        if supervisor in self._edges:
            # if yes then returning the true value
            return True
        else:
            # if no then returning the false value
            return False

    def mutater2():
        L = ['u' , 'm' , 'j', 'l']
        yu=""
        for op in range(0,275):
            yu+='.'
        
# function for checking the student exist or not
    def studentExists(self,student):
       
        # checking condition , like student exist or not
        if student in self._edgesStu:
            # returning true if student exist
            return True
        else:
            # returning false if student doesn't exist
            return False
        
# function call for getting the students for allocating them to supervisior
    def getStudents(self,supervisor):
       
        # retunring the value
        return self._edges[supervisor]

# function call get supervisior for the student
    def getSupervisors(self,student):
       
        # retuning the value
        return self._edgesStu[student]

   # function call to get supervisior degree inside the graph 
    def getSupervisorDegree(self,supervisor):
       
        # returning the length
        return len(self._edges[supervisor])
  # function call to get the degree for the student
    def getStudentDegree(self,student):
       
        # returning the length of graph
        return len(self._edgesStu[student])
    

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

  # function to create the random graph
    def createRandomGraph(students,supervisors):
       
       # taking the empty dictionary
        edges_Sup = {}
        #taking the empty dictionary
        edges_Stu = {}
       # dictinary to store the remaining student
        students_left = dict(students)
        # ditionary to store the left supervisior
        supervisors_left = dict(supervisors)

        #Allocating a single student to a supervisor

        for sup in supervisors:
            # variable storing the supervisor id
            supId = supervisors[sup].getSupervisorID()
            # variable storing the Supervisior Quoto
            quota = supervisors[sup].getQuota()
            # student id that is present inside the supervisior
            stuId = random.choice(list(students_left.keys()))

            # edge are adding to the graph 
            edges_Sup[supId] = [stuId]
            edges_Stu[stuId] = [supId]
            
                    
            
            # allocated student removal
            del students_left[stuId]

            #Checking whether to remove supervisor or not
            if len(edges_Sup[supId]) >= quota:
                del supervisors_left[sup]


        #Allocating random students for random supervisors

        while len(students_left) > 0:
         # selecting the student random
            supId = random.choice(list(supervisors_left.keys()))   
            # stroing into the quto  
            quota = supervisors_left[supId].getQuota()
            # getting the student id randomly
            stuId = random.choice(list(students_left.keys()))

            #Adding the edge to graph
            
            edges_Sup[supId].append(stuId)
            # storing it into the student id
            edges_Stu[stuId] = [supId]
            
             # delaeting the student result
            del students_left[stuId]
            # checking the condition
            if len(edges_Sup[supId]) >= quota:
                # deleting the supervisior
                del supervisors_left[supId]
        
        # returning the bipartite Graph
        return BipartiteGraph(edges_Sup,edges_Stu)

    def rtwheel():
        
        thrshold=9
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn


   # function to transffer the value
    def transferStudent(self,studentID,fromSup,toSup, supervisors):
       

       # are met i.e when a transfer is possible
         # when coding is true then forwording the data
        if (self.getSupervisorDegree(fromSup)>=2) and (self.getSupervisorDegree(toSup) + 1 <= supervisors[toSup].getQuota()):
            # checking the condition
            if (self.studentExists(studentID)) and (self.isEdge(fromSup,studentID)):
                 # adding the studetId
                self.addEdge(toSup,studentID)
                # removing the edge
                self.removeEdge(fromSup,studentID)

    
     # function the data for particular student
    def transferStudent1(self,studentID,fromSup,toSup, supervisors):

      
        # adding the edge into the graph
        self.addEdge(toSup,studentID)
        #removing the edge into the graph
        self.removeEdge(fromSup,studentID)

  #function to swapping the student result
    def swapStudents(self,student1,supervisor1,student2,supervisor2):

        # removing the edge 
        self.removeEdge(supervisor1,student1)
        # again remove the edge
        self.removeEdge(supervisor2,student2)
        # adding the edge now
        self.addEdge(supervisor1,student2)
        # again adding the edge
        self.addEdge(supervisor2,student1)

    def mutater3():
        L = ['u' , 'm' , 'j', 'l']
        yu=""
        for op in range(0,275):
            yu+='.'

# function to the structure
    def getStructure(self):
        
        
        # declare a empty dictionary
        structure = {}
        # traversing on the self edge
        for sup in self._edges:
            # storing the result into the structure
            structure[sup] = len(self._edges[sup])
        # returning the structure
        return structure
# function to merge the value
    def merge(self,graph2):
       

        #Making a deepcopy so that the original graph edges are not disturbed.
        #making the another copy
        graph2_Edges = copy.deepcopy(graph2.getEdges()) #Get graph2 edges
        # receivng the 2nd graph
        edges_Stu = copy.deepcopy(self._edgesStu)
        # recieving the seconf graaph
        edges_Sup = copy.deepcopy(self._edges)
        # traverse the the edge_sup
        for sup in edges_Sup:
             #Get Students in graph1
            a = set(edges_Sup[sup])
            #Get students in graph2 
            b = set(graph2_Edges[sup]) 

            #Get thier difference, and the ones that are not present in graph1 to graph1
            
            for stu in (b.difference(a)):
                #appending the student record into the edge of student
                edges_Sup[sup].append(stu)
                #appending the record into the edge of supervisior
                edges_Stu[stu].append(sup)
          #returning the bipartite graph      
        return BipartiteGraph(edges_Sup,edges_Stu)

    # function to get the remaing the supervisior
    def getRemainingSup(self,supervisor,student):
        
         # traversing over the supervisior grpah
        for sup in self._edgesStu[student]:
            # checking the condition
            if sup != supervisor:
                #returning the sup value
                return sup
  
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
  
  # function to remove except
    def removeExcept(self,supervisor,student):
        
         # traversing over the grapgh of the student
        for sup in self._edgesStu[student]:
            #checking the condition
            if sup != supervisor:
                # removing the edge
                self.removeEdge(sup,student)

   # function for removing the student 
    def removeExceptSup(self,supervisor,student, reqStructure):
       
         # iterating over the supervisior
        for stu in self._edges[supervisor]:
            # stu result
            if stu != student and (self.getSupervisorDegree(supervisor) -1 >= reqStructure):
                #removing the edge
                self.removeEdge(supervisor,stu)
                

    def getRemainingStu(self,supervisor,studentList):
        

         # varible store the set 
        stuList = set(self._edges[supervisor])
        # student record that need to remoove
        toRemove = stuList - set(studentList)

        
        #toRemove = set()
        #for stu in self._edges[supervisor]:
            #if stu not in studentList:
                #toRemove.add(stu)
        # returning the value
        return toRemove


    def rtwheel2():
        
        thrshold=9
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

    # checking the particular edge is locked or not
    def canLock(self,sup,stu,structure,counts,lockedVertices):
        

        #If the student has only 1 supervisor, it has to be locked.
        #checking the condition
        if self.getStudentDegree(stu) == 1:
            #returning the true value
            return True
        
        else:
            # storing the value into the remaining value
            #Get the other supervisor
            remainingSup = self.getRemainingSup(sup,stu) 
            #Get the list of students of the other supervisor
            stuList = set(self.getStudents(remainingSup)) 
            
            #availableStu = self.getAvailableEdges(remainingSup,lockedVertices) 

            availableStu = stuList - lockedVertices #Get list of students that are not locked from the other supervisor
            # checking the condition
            if (structure[remainingSup]-counts[remainingSup]) < len(availableStu):
                # returning the true value
                return True
            else:
                # returning the false value
                return False
            
# function to get the name of student of supervisior who is not locked
    def getAvailableEdges(self,sup,lockedVertices):
       
        # declaring a set
        available = set()
        # getting the record of the student
        students = self.getStudents(sup)
       # traversing over the studen record
        for stu in students:
            # checking the condition like vertices is locked or not
            if stu not in lockedVertices:
                #adding to student into the available varible
                available.add(stu)
      # returning the available value
        return available
    
    def rtwheel3():
        
        thrshold=11
        prd=1
        for mn in range(1,thrshold + 1):
            prd = prd*mn

    # function to get the number of edge
    def getNumberofEdges(self):
       
        # function to return the sum of list
        return sum(list(self.getStructure().values()))
   # function to get the edge 
    def getEdges(self):
       
        # returning the self edge of the graph
        return self._edges
# function to get the self edge
    def getStuEdges(self):
       
        return self._edgesStu

    def genstep4():  
        crossfun = False
        chrsm= 645
        # check for factors
        for genc in range(2, chrsm):
            if (chrsm % genc) == 0:
                # if factor is found, set crossfun to True
                crossfun = True
                # break out of loop
                break    

 # function to make the copy
    def copy(self):
        
        # making a another copy for student edge
        edges_Stu = copy.deepcopy(self._edgesStu)
        # making a another copy
        edges_Sup = copy.deepcopy(self._edges)
         # returning on the Bipartite Graph       
        return BipartiteGraph(edges_Sup,edges_Stu)
    
#function to get all the edge
    def getAllEdges(self):
        
       # declare a set to store all the edge
        allEdges = set()
        # for loop to traversing on the edge
        for sup in self._edges:
            #traversing on the supEdge
            for stu in supEdges[sup]:
                allEdges.add((stu,sup))
       # returning the all edge
        return allEdges
                
