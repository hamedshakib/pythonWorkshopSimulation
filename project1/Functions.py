import numpy
import pandas
from enum import Enum

class Event(Enum):
    EnterPieceForMachineA = 1;
    EnterPieceForMachineB =2;
    CompletionOfServiceOfMachineA=3
    CompletionOfServiceOfMachineB=4
    CompletionOfServiceOfMachineC=5
    OccurrenceOfMachineFailureA=6;
    OccurrenceOfMachineFailureB=7;
    FinishMachineRepairingA=8;
    FinishMachineRepairingB=9;

class MachineStatus(Enum):
    NotBusy=0
    Serving=1
    Repairing=2

class PieceStatus(Enum):
    InProcessingByMachineA=0;
    InProcessingByMachineB=1;
    InProcessingByMachineC=2;
    InQueueOfMachineA=3;
    InQueueOfMachineB=4;
    InQueueOfMachineC_FromMachineA=5;
    InQueueOfMachineC_FromMachineB=6;
    Exited=7;


class TypeOfService(Enum):
    ServiceForPiece1ByMachineA=1;
    ServiceForPiece2ByMachineB=2;
    ServiceForPiece1ByMachineB=3;
    ServiceByMachineC=4;

class TypeOfMachine(Enum):
    MachineTypeA=1
    MachineTypeB=2
    MachineTypeC=3

class TypeOfPieces(Enum):
    PieceType1=1
    PieceType2=2

class Queue:
    #ListOfpiecesInQueue=[]
    def __init__(self):
        self.MaxOfQueue = 0;
        self.ListOfpiecesInQueue=[]
        
    def SetMaxOfQueue(self,maxValue):
        self.MaxOfQueue=maxValue;

    def AppendPieceToQueue(self,piece):
        self.ListOfpiecesInQueue.append(piece);

    def InsertPieceToQueue(self,piece):
        firstIndex=0
        self.ListOfpiecesInQueue.insert(firstIndex,piece);

    def IsLongerThanMaxQueueLength(self,length):
        if(self.MaxOfQueue<length):
            return True;
        else:
            return False;

    def DetermineMaxQueueLength(self):
        length=len(self.ListOfpiecesInQueue)
        if(self.IsLongerThanMaxQueueLength(length)):
            self.SetMaxOfQueue(length);

    def isQueueEmpty(self):
        if(len(self.ListOfpiecesInQueue)==0):
            return True;
        else:
            return False;

    def popPieceFromQueue(self):
        firstIndex=0
        return self.ListOfpiecesInQueue.pop(firstIndex);

    def AppendAnotherListToThisList(self,AnotherQueue):
        print("hhh")
        print(":::",len(AnotherQueue.ListOfpiecesInQueue))
        print("/",AnotherQueue.ListOfpiecesInQueue)
        for i in range[0,len(AnotherQueue.ListOfpiecesInQueue)]:
            print("sss")
            self.ListOfpiecesInQueue.append(AnotherQueue.pop())
        #self.ListOfpiecesInQueue.extend(AnotherQueue);
        print("succ")

    def ResetToInitial(self):
        self.MaxOfQueue = 0;
        self.ListOfpiecesInQueue=[]



class Piece:
    ListOfComplitedServicesOnPiece=[]
    def __init__(self, type,LoginTime):
        self.type = type
        self.LoginTime=LoginTime;
        self.LogoutTime="";

    def add_LogoutTime(self, LogoutTime):
        self.LogoutTime=LogoutTime
        
    def CalculateResponseTimeForOnePiece(self):
        print("CalcRes LogoutTime:",self.LogoutTime)
        print("CalcRes LoginTime:",self.LoginTime)
        print("ResponseTime:",self.LogoutTime-self.LoginTime)
        self.ResponseTime=self.LogoutTime-self.LoginTime


    def Append_LastComplitedServiceOnPieceToListOfComplitedServices(self,prossesType):
        ListOfComplitedServicesOnPiece.append(prossesType);

    def ChangePieceStatus(self,status):
        self.PieceStatus=status;









class Machine:
    def __init__(self, type):
        self.type = type
        self.status=MachineStatus.NotBusy
        self.NumberOfPieceStartedProssesByMachine=0;
        self.NumberOfPieceComplitedProcessbyMachine=0;
        self.UsefulAndUnusefulServiceTimeForEachMachine=0;
        self.JustUsefulServiceTimeForEachMachine=0;
        self.DurationOfFailures=0


    def ChangeMachineStatus(self,status):
        self.status=status

    def add_NumberOfPieceStartedProssesByMachine(self):
        self.NumberOfPieceStartedProssesByMachine+=1


    def add_NumberOfPieceComplitedProcessByMachine(self):
        self.NumberOfPieceComplitedProcessbyMachine+=1;

    def Set_LastTimeMachineStartToProsses(self,time):
        self.LastTimeMachineStartToProsses=time;
        
    def Set_LastPieceThatMachineStartedToProsses(self,piece):
        self.LastPieceThatMachineStartedToProsses=piece;

    def Add_UsefulAndUnusefulServiceTimeForEachMachine(self,duration):
        self.UsefulAndUnusefulServiceTimeForEachMachine+=duration;

    def Add_JustUsefulServiceTimeForEachMachine(self,duration):
        self.JustUsefulServiceTimeForEachMachine+=duration;

    def Calculate_ServiceTimeForMachineInNonSetupTime(self):
        if(self.LastTimeMachineStartToProsses<TotalSetupTime):
            return CurrentTime-TotalSetupTime;
        else:
            return CurrentTime-self.LastTimeMachineStartToProsses;

    def StartProssesOnPieceByMachine(self,piece):
        print("StartedProsses that Entere at:",piece.LoginTime)
        self.Set_LastPieceThatMachineStartedToProsses(piece)
        self.Set_LastTimeMachineStartToProsses(CurrentTime);


    def add_DurationOfFailures(self,duration):
        self.DurationOfFailures+=duration;

    def ResetToInitial(self):
        self.status=MachineStatus.NotBusy
        self.NumberOfPieceStartedProssesByMachine=0;
        self.NumberOfPieceComplitedProcessbyMachine=0;
        self.UsefulAndUnusefulServiceTimeForEachMachine=0;
        self.JustUsefulServiceTimeForEachMachine=0;
        self.DurationOfFailures=0





MachineA = Machine(TypeOfMachine.MachineTypeA);
MachineB = Machine(TypeOfMachine.MachineTypeB);
MachineC = Machine(TypeOfMachine.MachineTypeC);

QueueOfEnterToMachineA = Queue();
QueueOfEnterToMachineBType1 = Queue();
QueueOfEnterToMachineBType2 = Queue();
QueueOfEnterToMachineC_FromMachineA = Queue();
QueueOfEnterToMachineC_FromMachineB = Queue();


CurrentTime=0;
TotalSimulationTime=10*60;
TotalSetupTime=1*60;
FEL=[];
NowIndexOfFEL=tuple();
ListOfPieces=[];
NowNumberSimulationTime=0;
MaxOfQueueOfAllTypePieceEnterToMachineB=0;





#define other Functions
#Function about generate Random
def GenerateRandomTimeBetweenTwoEnterA():
    return numpy.random.normal(20,(3/3))

def GenerateRandomTimeBetweenTwoEnterB():
    return numpy.random.normal(16,(10/3))

def GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineA():
    return numpy.random.normal(450,(50/3))

def GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineB():
    return numpy.random.normal(210,(10/3))

def GenerateRandomTimeForRepairMachineA():
    return numpy.random.normal(25,(4/3))

def GenerateRandomTimeForRepairMachineB():
    return numpy.random.normal(20,(4/3))

def GenerateRandomTimeForServiceTimeMachineA():
    return numpy.random.normal(15,(9/3))

def GenerateRandomTimeForServiceTimeMachineB():
    return numpy.random.normal(18,(2/3))

def GenerateRandomTimeForServiceTimeMachineC():
    return numpy.random.normal(10,(4/3))

def GenerateRandomTimeForServiceTime_OnMachineBForPiece1():
    return numpy.random.normal(40,(9/3))

def DeterminingDurationOfService(service):
    if(service==TypeOfService.ServiceForPiece1ByMachineA):
        return GenerateRandomTimeForServiceTimeMachineA();
    elif(service==TypeOfService.ServiceForPiece2ByMachineB):
        return GenerateRandomTimeForServiceTimeMachineB();
    elif(service==TypeOfService.ServiceForPiece1ByMachineB):
        return GenerateRandomTimeForServiceTime_OnMachineBForPiece1();
    elif(service==TypeOfService.ServiceByMachineC):
        return GenerateRandomTimeForServiceTimeMachineC();
#!
def CalculteTimeOfCompletionService(serviceDuration):
    global CurrentTime;
    return serviceDuration+CurrentTime;

def DetermineTimeOfEnterOfNextPiece(pieceType):
    global CurrentTime;
    if(pieceType==TypeOfPieces.PieceType1):
        return GenerateRandomTimeBetweenTwoEnterA()+CurrentTime;
    elif(pieceType==TypeOfPieces.PieceType2):
        return GenerateRandomTimeBetweenTwoEnterB()+CurrentTime;

def DetermineDurationOfReaparing(machineType):
    if(machineType==TypeOfMachine.MachineTypeA):
        return GenerateRandomTimeForRepairMachineA();
    elif(machineType==TypeOfMachine.MachineTypeB):
        return GenerateRandomTimeForRepairMachineB();

def DetermineFinishOfReaparing(duration):
    global CurrentTime;
    return duration+CurrentTime;


def DetermineTimeOfNextOfOccurrenceFailureMachine(machineType):
    if(machineType==TypeOfMachine.MachineTypeA):
        return GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineA()+CurrentTime;
    elif(machineType==TypeOfMachine.MachineTypeB):
        return GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineB()+CurrentTime;


#Function About FEL
def DeterminingFEL():
    global NowIndexOfFEL
    SortFEL();
    FirstMemberOfFEL=0
    #NowIndexOfFEL;
    NowIndexOfFEL=FEL[NowNumberSimulationTime][FirstMemberOfFEL]
    print("")
    print("NowNumberSimulationTime:",NowNumberSimulationTime)
    print("Feom DeterminingFEL:",FEL)



def MoveTimeToFEL():
    global NowIndexOfFEL
    global CurrentTime
    indexOfTime=1
    #print(NowIndexOfFEL[0])
    befCur=CurrentTime;
    CurrentTime=NowIndexOfFEL[indexOfTime];
    aftCur=CurrentTime;
    print("**--",befCur," ",aftCur)
    print("Current:",CurrentTime)
    print("From MoveTimeToFEL:",FEL)


def SortFEL():
    indexOfTime=1
    FEL[NowNumberSimulationTime].sort(key=lambda tup: tup[indexOfTime])
    print("")
    print("From SortFEL:",FEL)

def AddEventToFEL(code,Time):
    #ToDo Edit
    FEL[NowNumberSimulationTime].append(tuple((code,Time)));
    print("")
    print("From AddEventToFEL:",FEL)

def RemoveEventFromFEL(indexOfFEL):
    print("index in romeve FEL:",indexOfFEL)
    FEL[NowNumberSimulationTime].remove(FEL[NowNumberSimulationTime][indexOfFEL])
    print("From RemoveEventFromFEL:",FEL)

#other
def isFinishedTime():
    if(CurrentTime<=TotalSimulationTime):
        return False;
    elif(CurrentTime>TotalSimulationTime):
        return True;
    else:
        print("Error")
 
def isNowInSetupTime():
    if(CurrentTime<TotalSetupTime):
        return True;
    else:
        return False;




def isMachineNotBusy(machine):
    print("Status machne:",machine.status)
    if(machine.status==MachineStatus.NotBusy):
        return True;
    else:
        return False;

def isMachineServing(machine):
    if(machine.status==MachineStatus.Serving):
        return True;
    else:
        return False;

def isMachineRepairing(machine):
    if(machine.status==MachineStatus.Repairing):
        return True;
    else:
        return False;


def SpecifyCodeNumber():
    global NowIndexOfFEL
    indexOfCode=0
    return NowIndexOfFEL[indexOfCode];

def HandelEnterOfNewPieceEntered(pieceType):
    return AddPieceToListOfPieces(CreateNewPieceEntered(pieceType))

def CreateNewPieceEntered(pieceType):
    global CurrentTime
    piece=Piece(pieceType,CurrentTime);
    return piece;

def AddPieceToListOfPieces(piece):
    #ListOfPieces[NowNumberSimulationTime].append(piece);
    print("***1")
    ListOfPieces[NowNumberSimulationTime].append(piece);
    print("***2")
    return piece;

   
def MoveQueueOfMachineAToQuereMachineB():
    print("did*")
    #global QueueOfEnterToMachineBType1;
    global QueueOfEnterToMachineA;
    #QueueOfEnterToMachineBType1+=QueueOfEnterToMachineA
    print("L:",QueueOfEnterToMachineA.ListOfpiecesInQueue)
    if(len(QueueOfEnterToMachineA.ListOfpiecesInQueue)!=0):
        QueueOfEnterToMachineBType1.AppendAnotherListToThisList(QueueOfEnterToMachineA);
        for pieceInQueueOfEnterToMachineA in QueueOfEnterToMachineA.ListOfpiecesInQueue:
            pieceInQueueOfEnterToMachineA.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
    print("did**")
    QueueOfEnterToMachineA.ListOfpiecesInQueue=[]

def MovePieceThatWasProssesingByMachineAToMachineB():
    print("&1")
    LastPieceThatMachineAStartedToProsses=MachineA.LastPieceThatMachineStartedToProsses;
    print("&2")
    MachineB.StartProssesOnPieceByMachine(LastPieceThatMachineAStartedToProsses);
    LastPieceThatMachineAStartedToProsses.ChangePieceStatus(PieceStatus.InProcessingByMachineB);
    print("&3")
    serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineB);
    print("&4")
    AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));

def MovePieceThatWasProssesingByMachineBToQueueB():
    LastPieceThatMachineBStartedToProsses=MachineB.LastPieceThatMachineStartedToProsses;
    LastPieceThatMachineBStartedToProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
    print("did")
    QueueOfEnterToMachineBType2.InsertPieceToQueue(LastPieceThatMachineBStartedToProsses);
    print("did5")


def MovePieceToQueueOfEnterToMachineC_FromMachineA():
    LastPieceThatMachineAComplitedProsses=MachineA.LastPieceThatMachineStartedToProsses;
    LastPieceThatMachineAComplitedProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineC_FromMachineA)
    QueueOfEnterToMachineC_FromMachineA.AppendPieceToQueue(LastPieceThatMachineAComplitedProsses)
    LastPieceThatMachineAComplitedProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineC_FromMachineA)


def MovePieceToQueueOfEnterToMachineC_FromMachineB():
    LastPieceThatMachineBComplitedProsses=MachineB.LastPieceThatMachineStartedToProsses;
    QueueOfEnterToMachineC_FromMachineB.AppendPieceToQueue(LastPieceThatMachineBComplitedProsses)
    LastPieceThatMachineBComplitedProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineC_FromMachineB)



def ProssesForDetermineMaxofQueue(queue):
    #print(len(queue.ListOfpiecesInQueue))
    #lenof=len(queue.ListOfpiecesInQueue)
    queue.DetermineMaxQueueLength();
    global MaxOfQueueOfAllTypePieceEnterToMachineB;
    if(queue==QueueOfEnterToMachineBType1 or queue==QueueOfEnterToMachineBType2):
        NowLengthQueueOfAllTypePieceEnterToMachineB=(len(QueueOfEnterToMachineBType1.ListOfpiecesInQueue)+len(QueueOfEnterToMachineBType2.ListOfpiecesInQueue))
        if(MaxOfQueueOfAllTypePieceEnterToMachineB<NowLengthQueueOfAllTypePieceEnterToMachineB):
            MaxOfQueueOfAllTypePieceEnterToMachineB=NowLengthQueueOfAllTypePieceEnterToMachineB
            print("*$$$$$!!!!")

    #queue.DetermineMaxQueueLength(len(queue.ListOfpieces));


def FindIndexOfFELCompletionOfService(machineType):
    print("Errrrrrrrrrrrrr")
    #ToDo complite bug mabye
    i1=0
    print("//**//",machineType)
    indexOfCodeOfFEL=0
    for OneFutureEvent in FEL[NowNumberSimulationTime]:
        print("...")
        if(machineType==TypeOfMachine.MachineTypeA):
            print(999)
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineA):
                print("+",OneFutureEvent[indexOfCodeOfFEL])
                print(i1)
                return int(i1);
        elif(machineType==TypeOfMachine.MachineTypeB):
            print(888)
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineB):
                print("-",OneFutureEvent[indexOfCodeOfFEL])
                print(i1)
                return int(i1);
        
        i1=i1+1
        print("i++")

    print("No FEL of Complite there isn't");

def IsThereComplitionEventForMachineInFEL(machineType):
    indexOfCodeOfFEL=0
    for OneFutureEvent in FEL[NowNumberSimulationTime]:
        if(machineType==TypeOfMachine.MachineTypeA):
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineA):
                return True;
        elif(machineType==TypeOfMachine.MachineTypeB):
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineB):
                return True;



    print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    return False;


def DetermineBottlenecksQueue():
    ListOfMaxOfQueue=[QueueOfEnterToMachineA.MaxOfQueue,MaxOfQueueOfAllTypePieceEnterToMachineB,QueueOfEnterToMachineC_FromMachineA.MaxOfQueue,QueueOfEnterToMachineC_FromMachineB.MaxOfQueue];
    if(QueueOfEnterToMachineA.MaxOfQueue==max(ListOfMaxOfQueue)):
        return "Queue Of Enter To Machine A "
    elif(MaxOfQueueOfAllTypePieceEnterToMachineB==max(ListOfMaxOfQueue)):
        return "Queue Of Enter To Machine B "
    elif(QueueOfEnterToMachineC_FromMachineA.MaxOfQueue==max(ListOfMaxOfQueue)):
        return "Queue Of Enter To Machine C From Machine A"
    elif(QueueOfEnterToMachineC_FromMachineB.MaxOfQueue==max(ListOfMaxOfQueue)):
        return "Queue Of Enter To Machine C From Machine B"


def initializationOfVariables(NumberOfSimulation1):
    global CurrentTime;
    global TotalSimulationTime
    global NowNumberSimulationTime;
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType1;
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType2;
    global MaxOfQueueOfAllTypePieceEnterToMachineB;
    
    CurrentTime=0;
    TotalSimulationTime=10*60;
    NowNumberSimulationTime=NumberOfSimulation1;
    NumberOfPieceThatExitedFromSystemInNonSetupTimeType1=0;
    NumberOfPieceThatExitedFromSystemInNonSetupTimeType2=0;
    MaxOfQueueOfAllTypePieceEnterToMachineB=0;
    FEL.extend([[]]);
    AddEventToFEL(Event.EnterPieceForMachineA,GenerateRandomTimeBetweenTwoEnterA());
    AddEventToFEL(Event.EnterPieceForMachineB,GenerateRandomTimeBetweenTwoEnterB());
    AddEventToFEL(Event.OccurrenceOfMachineFailureA,GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineA())
    AddEventToFEL(Event.OccurrenceOfMachineFailureB,GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineB())
    ListOfPieces.extend([[]]);


    MachineA.ResetToInitial();
    MachineB.ResetToInitial();
    MachineC.ResetToInitial();

    QueueOfEnterToMachineA.ResetToInitial();
    QueueOfEnterToMachineBType1.ResetToInitial();
    QueueOfEnterToMachineBType2.ResetToInitial();
    QueueOfEnterToMachineC_FromMachineA.ResetToInitial();
    QueueOfEnterToMachineC_FromMachineB.ResetToInitial();




def ShowResultOfOneTimeSimulations():

   
    #print("TypeOfPiece:",ListOfPieces[0][0].type)
    #print("Status:",ListOfPieces[0][0].PieceStatus)
    #print("LoginTime:",ListOfPieces[0][0].LoginTime)
    #print("LogoutTime:",ListOfPieces[0][0].LogoutTime)
    #if(ListOfPieces[0][0].LogoutTime!=""):
    #    print("ResponseTime:",ListOfPieces[0][0].ResponseTime)


    #for i in ListOfPieces[0][0]:
    #    print("TypeOfPiece:",i[0].type)

    #if(NowNumberSimulationTime==1):
    #    print("List:",ListOfPieces)

    ListOfPieces[NowNumberSimulationTime][0].LoginTime
    print("1 th piece",ListOfPieces[NowNumberSimulationTime][0].type,"Status:",ListOfPieces[NowNumberSimulationTime][0].PieceStatus,"ResponseTime:",ListOfPieces[NowNumberSimulationTime][0].ResponseTime);
    ListOfPieces[NowNumberSimulationTime][1].LoginTime
    print("2 th piece",ListOfPieces[NowNumberSimulationTime][1].type,"Status:",ListOfPieces[NowNumberSimulationTime][1].PieceStatus,"ResponseTime:",ListOfPieces[NowNumberSimulationTime][1].ResponseTime);
    ListOfPieces[NowNumberSimulationTime][2].LoginTime
    print("3 th piece",ListOfPieces[NowNumberSimulationTime][2].type,"Status:",ListOfPieces[NowNumberSimulationTime][2].PieceStatus,"ResponseTime:",ListOfPieces[NowNumberSimulationTime][2].ResponseTime);
    ListOfPieces[NowNumberSimulationTime][3].LoginTime
    print("4 th piece",ListOfPieces[NowNumberSimulationTime][3].type,"Status:",ListOfPieces[NowNumberSimulationTime][3].PieceStatus,"ResponseTime:",ListOfPieces[NowNumberSimulationTime][3].ResponseTime);

    


def ProssesForExitOfLastPieceThatCompliteServiceByLastMachineOfSystem():
    print("R%R")
    piece=MachineC.LastPieceThatMachineStartedToProsses;
    piece.add_LogoutTime(CurrentTime);
    piece.CalculateResponseTimeForOnePiece();
    piece.ChangePieceStatus(PieceStatus.Exited)

def add_NumberOfPieceThatExitedFromSystemInNonSetupTime(type):
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType1;
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType2;
    if(type==TypeOfPieces.PieceType1):
            NumberOfPieceThatExitedFromSystemInNonSetupTimeType1+=1;
    elif(type==TypeOfPieces.PieceType2):
            NumberOfPieceThatExitedFromSystemInNonSetupTimeType2+=1;


def Exemine_ShowResult():
    ResultOfpiecesTable = pandas.DataFrame(columns=['Type Of Piece','Status of piece','EnterTime', 'ExitTime', 'ResponseTime'])
    for OnePiece in ListOfPieces[NowNumberSimulationTime][:]:

        if(OnePiece.PieceStatus==PieceStatus.Exited):
            ResultOfpiecesTable = ResultOfpiecesTable.append({
                'Type Of Piece':OnePiece.type,
                'Status of piece':OnePiece.PieceStatus,
                'EnterTime': OnePiece.LoginTime,
                'ExitTime': OnePiece.LogoutTime,
                'ResponseTime': OnePiece.ResponseTime
                }, ignore_index=True)

        else:
            ResultOfpiecesTable = ResultOfpiecesTable.append({
                'Type Of Piece':OnePiece.type,
                'Status of piece':OnePiece.PieceStatus,
                'EnterTime': OnePiece.LoginTime,
                }, ignore_index=True)


    print('------------------------------------------------------------------')
    print('\n')
    print(ResultOfpiecesTable)

    #ToDo Complite
    ResultOfMachineTable = pandas.DataFrame(columns=['Machine Type','# of Piece Started Prosses By Machine In NonSetupTime','# of Piece Complited Prosses By Machine In NonSetupTime','Useful Exploitation rate','Total Exploitation rate', 'Machine Failure rate']);
    ResultOfMachineTable = ResultOfMachineTable.append({
                'Machine Type':"Machine A",
                '# of Piece Started Prosses By Machine In NonSetupTime':MachineA.NumberOfPieceStartedProssesByMachine,
                '# of Piece Complited Prosses By Machine In NonSetupTime': MachineA.NumberOfPieceComplitedProcessbyMachine,
                'Useful Exploitation rate': MachineA.JustUsefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
                'Total Exploitation rate': MachineA.UsefulAndUnusefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
                'Machine Failure rate': MachineA.DurationOfFailures/(TotalSimulationTime-TotalSetupTime)
                }, ignore_index=True)
    ResultOfMachineTable = ResultOfMachineTable.append({
                'Machine Type':"Machine B",
                '# of Piece Started Prosses By Machine In NonSetupTime':MachineB.NumberOfPieceStartedProssesByMachine,
                '# of Piece Complited Prosses By Machine In NonSetupTime': MachineB.NumberOfPieceComplitedProcessbyMachine,
                'Useful Exploitation rate': MachineB.JustUsefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
                'Total Exploitation rate': MachineB.UsefulAndUnusefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
                'Machine Failure rate': MachineB.DurationOfFailures/(TotalSimulationTime-TotalSetupTime)
                }, ignore_index=True)
    ResultOfMachineTable = ResultOfMachineTable.append({
                'Machine Type':"Machine C",
                '# of Piece Started Prosses By Machine In NonSetupTime':MachineC.NumberOfPieceStartedProssesByMachine,
                '# of Piece Complited Prosses By Machine In NonSetupTime': MachineC.NumberOfPieceComplitedProcessbyMachine,
                'Useful Exploitation rate': MachineC.JustUsefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
                'Total Exploitation rate': MachineC.UsefulAndUnusefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
                'Machine Failure rate': 0
                }, ignore_index=True)

    print('------------------------------------------------------------------')
    print('\n')
    print(ResultOfMachineTable)


    SumResponseTimePieceType1=0;
    
    SumResponseTimePieceType2=0;

    for piece in  ListOfPieces[NowNumberSimulationTime][:]:
        if(piece.LogoutTime!=""):
            if(piece.LogoutTime>TotalSetupTime):
                if(piece.type==TypeOfPieces.PieceType1):
                    SumResponseTimePieceType1+=piece.ResponseTime;
                if(piece.type==TypeOfPieces.PieceType2):
                    SumResponseTimePieceType2+=piece.ResponseTime;


    ResultOfResponseTimeTable = pandas.DataFrame(columns=['Piece Type','Number of pieces producted','Avrage of ResponseTime']);
    ResultOfResponseTimeTable = ResultOfResponseTimeTable.append({
            'Piece Type':"Piece Type 1",
            'Number of pieces producted':NumberOfPieceThatExitedFromSystemInNonSetupTimeType1,
            'Avrage of ResponseTime':(SumResponseTimePieceType1/NumberOfPieceThatExitedFromSystemInNonSetupTimeType1)
            }, ignore_index=True)
    ResultOfResponseTimeTable = ResultOfResponseTimeTable.append({
            'Piece Type':"Piece Type 2",
            'Number of pieces producted':NumberOfPieceThatExitedFromSystemInNonSetupTimeType2,
            'Avrage of ResponseTime':(SumResponseTimePieceType2/NumberOfPieceThatExitedFromSystemInNonSetupTimeType2)
            }, ignore_index=True)

    print('------------------------------------------------------------------')
    print('\n')
    print(ResultOfResponseTimeTable)
    



    ResultOfMaxOfQueueTable = pandas.DataFrame(columns=['Queue Type','Max of Queue']);
    ResultOfMaxOfQueueTable = ResultOfMaxOfQueueTable.append({
            'Queue Type':"Queue Of Enter To Machine A",
            'Max of Queue':QueueOfEnterToMachineA.MaxOfQueue
            }, ignore_index=True)
    ResultOfMaxOfQueueTable = ResultOfMaxOfQueueTable.append({
            'Queue Type':"Queue Of Enter To Machine B",
            'Max of Queue':MaxOfQueueOfAllTypePieceEnterToMachineB
            }, ignore_index=True)
    ResultOfMaxOfQueueTable = ResultOfMaxOfQueueTable.append({
            'Queue Type':"Queue Of Enter To Machine C From Machine A",
            'Max of Queue':QueueOfEnterToMachineC_FromMachineA.MaxOfQueue
            }, ignore_index=True)
    ResultOfMaxOfQueueTable = ResultOfMaxOfQueueTable.append({
            'Queue Type':"Queue Of Enter To Machine C From Machine B",
            'Max of Queue':QueueOfEnterToMachineC_FromMachineB.MaxOfQueue
            }, ignore_index=True)


    print('------------------------------------------------------------------')
    print('\n')
    print(ResultOfMaxOfQueueTable)

    print('\n')
    print("******************************************************************")
    print(DetermineBottlenecksQueue(),"is bottlenecks")
    print("******************************************************************")
