import numpy
import pandas
from enum import Enum
from scipy.stats import t
from scipy.stats import sem
import seaborn as sns
import matplotlib.pyplot as plt

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
        for i in range(0,len(AnotherQueue.ListOfpiecesInQueue)):
            self.ListOfpiecesInQueue.append(AnotherQueue.popPieceFromQueue())




    def ResetToInitial(self):
        self.MaxOfQueue = 0;
        self.ListOfpiecesInQueue=[]



class Piece:
    ListOfComplitedServicesOnPiece=[]
    def __init__(self, type,LoginTime):
        self.type = type
        self.LoginTime=LoginTime;
        self.LogoutTime="";
        self.PieceStatus=""

        self.TimeInQueueOfMachineA=""
        self.TimeInQueueOfMachineB=""
        self.TimeInQueueOfMachineC_FromMachineA=""
        self.TimeInQueueOfMachineC_FromMachineB=""
        self.TimeInProcessingByMachineA=""
        self.TimeInProcessingByMachineB=""
        self.TimeInProcessingByMachineC=""

    def add_LogoutTime(self, LogoutTime):
        self.LogoutTime=LogoutTime
        
    def CalculateResponseTimeForOnePiece(self):
        self.ResponseTime=self.LogoutTime-self.LoginTime


    def Append_LastComplitedServiceOnPieceToListOfComplitedServices(self,prossesType):
        ListOfComplitedServicesOnPiece.append(prossesType);

    def ChangePieceStatus(self,status):
        self.PieceStatus=status;

    def ApplyStartTimeOfNewPosion(self,status):
        data=str(round(CurrentTime,1));
        if(status==PieceStatus.InQueueOfMachineA):
            self.TimeInQueueOfMachineA=data
        if(status==PieceStatus.InQueueOfMachineB):
            self.TimeInQueueOfMachineB=data
        if(status==PieceStatus.InQueueOfMachineC_FromMachineA):
            self.TimeInQueueOfMachineC_FromMachineA=data
        if(status==PieceStatus.InQueueOfMachineC_FromMachineB):
            self.TimeInQueueOfMachineC_FromMachineB=data
        if(status==PieceStatus.InProcessingByMachineA):
            self.TimeInProcessingByMachineA=data
        if(status==PieceStatus.InProcessingByMachineB):
            self.TimeInProcessingByMachineB=data
        if(status==PieceStatus.InProcessingByMachineC):
            self.TimeInProcessingByMachineC=data

    def ApplyEndTimeOfLastPosion(self):
        data=str(round(CurrentTime,1));
        if(self.PieceStatus==PieceStatus.InQueueOfMachineA):
            self.TimeInQueueOfMachineA+='-'+data
        elif(self.PieceStatus==PieceStatus.InQueueOfMachineB):
            self.TimeInQueueOfMachineB+='-'+data
        elif(self.PieceStatus==PieceStatus.InQueueOfMachineC_FromMachineA):
            self.TimeInQueueOfMachineC_FromMachineA+='-'+data
        elif(self.PieceStatus==PieceStatus.InQueueOfMachineC_FromMachineB):
            self.TimeInQueueOfMachineC_FromMachineB+='-'+data
        elif(self.PieceStatus==PieceStatus.InProcessingByMachineA):
            self.TimeInProcessingByMachineA+='-'+data
        elif(self.PieceStatus==PieceStatus.InProcessingByMachineB):
            self.TimeInProcessingByMachineB+='-'+data
        elif(self.PieceStatus==PieceStatus.InProcessingByMachineC):
            self.TimeInProcessingByMachineC+='-'+data
        









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
NumberTotalSimulation=10;

ResultOfResponseTime=pandas.DataFrame(columns=['NumberSimulation','AvrageResponseTimePieceType1','AvrageResponseTimePieceType2','AvrageResponseTimeTotalPiece']);

ResultOfNumberOfPieceProducted=pandas.DataFrame(columns=['NumberSimulation','NumberOfPieceProductedType1','NumberOfPieceProductedType2']);
ResultOfTotalExplotionRate=pandas.DataFrame(columns=['NumberSimulation','TotalExplotionRateMachineA','TotalExplotionRateMachineB','TotalExplotionRateMachineC']);
ResultOfMachineFailureRate=pandas.DataFrame(columns=['NumberSimulation','MachineFailureRateMachineA','MachineFailureRateMachineB','MachineFailureRateMachineC']);

ResultOfPointEstimation=pandas.DataFrame(columns=['PieceType','Point Estimation'])
ResultOfIntervalEstimation=pandas.DataFrame(columns=['PieceType','Interval Estimation'])


sns.set_style('whitegrid')
sns.set_palette('Set2')







#define other Functions
#Function about generate Random
def GenerateRandomTimeBetweenTwoEnterA():
    return numpy.random.normal(20,3)


def GenerateRandomTimeBetweenTwoEnterB():
    time= numpy.random.normal(16,10)
    while(time<0):
        time=numpy.random.normal(16,10)
    return time

def GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineA():
    return numpy.random.normal(450,50)

def GenerateRandomTimeBetween_FinishRepair_OccurrenceFailure_MachineB():
    return numpy.random.normal(210,10)

def GenerateRandomTimeForRepairMachineA():
    return numpy.random.normal(25,4)

def GenerateRandomTimeForRepairMachineB():
    return numpy.random.normal(20,4)

def GenerateRandomTimeForServiceTimeMachineA():
    time= numpy.random.normal(15,9)
    while(time<0):
        time=numpy.random.normal(15,9)
    return time

def GenerateRandomTimeForServiceTimeMachineB():
    return numpy.random.normal(18,2)

def GenerateRandomTimeForServiceTimeMachineC():
    time= numpy.random.normal(10,4)
    while(time<0):
        time=numpy.random.normal(10,4)
    return time

def GenerateRandomTimeForServiceTime_OnMachineBForPiece1():
    return numpy.random.normal(40,9)

def DeterminingDurationOfService(service):
    if(service==TypeOfService.ServiceForPiece1ByMachineA):
        return GenerateRandomTimeForServiceTimeMachineA();
    elif(service==TypeOfService.ServiceForPiece2ByMachineB):
        return GenerateRandomTimeForServiceTimeMachineB();
    elif(service==TypeOfService.ServiceForPiece1ByMachineB):
        return GenerateRandomTimeForServiceTime_OnMachineBForPiece1();
    elif(service==TypeOfService.ServiceByMachineC):
        return GenerateRandomTimeForServiceTimeMachineC();
 
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
    NowIndexOfFEL=FEL[NowNumberSimulationTime][FirstMemberOfFEL]




def MoveTimeToFEL():
    global NowIndexOfFEL
    global CurrentTime
    indexOfTime=1
    CurrentTime=NowIndexOfFEL[indexOfTime];



def SortFEL():
    indexOfTime=1
    FEL[NowNumberSimulationTime].sort(key=lambda tup: tup[indexOfTime])


def AddEventToFEL(code,Time):
    FEL[NowNumberSimulationTime].append(tuple((code,Time)));


def RemoveEventFromFEL(indexOfFEL):
    FEL[NowNumberSimulationTime].remove(FEL[NowNumberSimulationTime][indexOfFEL])

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
    ListOfPieces[NowNumberSimulationTime].append(piece);
    return piece;

   
def MoveQueueOfMachineAToQuereMachineB():
    global QueueOfEnterToMachineA;

    if(len(QueueOfEnterToMachineA.ListOfpiecesInQueue)!=0):
        QueueOfEnterToMachineBType1.AppendAnotherListToThisList(QueueOfEnterToMachineA);
        for pieceInQueueOfEnterToMachineA in QueueOfEnterToMachineA.ListOfpiecesInQueue:
            pieceInQueueOfEnterToMachineA.ApplyEndTimeOfLastPosion();
            pieceInQueueOfEnterToMachineA.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
            pieceInQueueOfEnterToMachineA.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineB)


    QueueOfEnterToMachineA.ListOfpiecesInQueue=[]


def MovePieceThatWasProssesingByMachineAToQueueB():
    piece=MachineA.LastPieceThatMachineStartedToProsses;
    QueueOfEnterToMachineBType1.AppendPieceToQueue(piece);
    piece.ApplyEndTimeOfLastPosion();
    piece.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
    piece.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineB)

def MovePieceThatWasProssesingByMachineAToMachineB():
    LastPieceThatMachineAStartedToProsses=MachineA.LastPieceThatMachineStartedToProsses;
    MachineB.StartProssesOnPieceByMachine(LastPieceThatMachineAStartedToProsses);
    LastPieceThatMachineAStartedToProsses.ApplyEndTimeOfLastPosion();
    LastPieceThatMachineAStartedToProsses.ChangePieceStatus(PieceStatus.InProcessingByMachineB);
    LastPieceThatMachineAStartedToProsses.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineB);
    serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineB);
    AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));

def MovePieceThatWasProssesingByMachineBToQueueB():
    LastPieceThatMachineBStartedToProsses=MachineB.LastPieceThatMachineStartedToProsses;
    LastPieceThatMachineBStartedToProsses.ApplyEndTimeOfLastPosion();
    LastPieceThatMachineBStartedToProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
    LastPieceThatMachineBStartedToProsses.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineB)
    QueueOfEnterToMachineBType2.InsertPieceToQueue(LastPieceThatMachineBStartedToProsses);


def MovePieceToQueueOfEnterToMachineC_FromMachineA():
    LastPieceThatMachineAComplitedProsses=MachineA.LastPieceThatMachineStartedToProsses;
    LastPieceThatMachineAComplitedProsses.ApplyEndTimeOfLastPosion();
    LastPieceThatMachineAComplitedProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineC_FromMachineA)
    LastPieceThatMachineAComplitedProsses.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineC_FromMachineA)
    QueueOfEnterToMachineC_FromMachineA.AppendPieceToQueue(LastPieceThatMachineAComplitedProsses)
    LastPieceThatMachineAComplitedProsses.ApplyEndTimeOfLastPosion();
    LastPieceThatMachineAComplitedProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineC_FromMachineA)
    LastPieceThatMachineAComplitedProsses.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineC_FromMachineA)

def MovePieceToQueueOfEnterToMachineC_FromMachineB():
    LastPieceThatMachineBComplitedProsses=MachineB.LastPieceThatMachineStartedToProsses;
    QueueOfEnterToMachineC_FromMachineB.AppendPieceToQueue(LastPieceThatMachineBComplitedProsses)
    LastPieceThatMachineBComplitedProsses.ApplyEndTimeOfLastPosion();
    LastPieceThatMachineBComplitedProsses.ChangePieceStatus(PieceStatus.InQueueOfMachineC_FromMachineB)
    LastPieceThatMachineBComplitedProsses.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineC_FromMachineB)


def ProssesForDetermineMaxofQueue(queue):
    queue.DetermineMaxQueueLength();
    global MaxOfQueueOfAllTypePieceEnterToMachineB;
    if(queue==QueueOfEnterToMachineBType1 or queue==QueueOfEnterToMachineBType2):
        NowLengthQueueOfAllTypePieceEnterToMachineB=(len(QueueOfEnterToMachineBType1.ListOfpiecesInQueue)+len(QueueOfEnterToMachineBType2.ListOfpiecesInQueue))
        if(MaxOfQueueOfAllTypePieceEnterToMachineB<NowLengthQueueOfAllTypePieceEnterToMachineB):
            MaxOfQueueOfAllTypePieceEnterToMachineB=NowLengthQueueOfAllTypePieceEnterToMachineB;




def FindIndexOfFELCompletionOfService(machineType):
    numberOfIndexCompletionOfService=0
    indexOfCodeOfFEL=0
    for OneFutureEvent in FEL[NowNumberSimulationTime]:
        if(machineType==TypeOfMachine.MachineTypeA):
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineA):
                return int(numberOfIndexCompletionOfService);
        elif(machineType==TypeOfMachine.MachineTypeB):
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineB):
                return int(numberOfIndexCompletionOfService);
        
        numberOfIndexCompletionOfService+=1


def IsThereComplitionEventForMachineInFEL(machineType):
    indexOfCodeOfFEL=0
    for OneFutureEvent in FEL[NowNumberSimulationTime]:
        if(machineType==TypeOfMachine.MachineTypeA):
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineA):
                return True;
        elif(machineType==TypeOfMachine.MachineTypeB):
            if(OneFutureEvent[indexOfCodeOfFEL]==Event.CompletionOfServiceOfMachineB):
                return True;

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


    


def ProssesForExitOfLastPieceThatCompliteServiceByLastMachineOfSystem():
    piece=MachineC.LastPieceThatMachineStartedToProsses;
    piece.add_LogoutTime(CurrentTime);
    piece.CalculateResponseTimeForOnePiece();
    piece.ApplyEndTimeOfLastPosion();
    piece.ChangePieceStatus(PieceStatus.Exited)

def add_NumberOfPieceThatExitedFromSystemInNonSetupTime(type):
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType1;
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType2;
    if(type==TypeOfPieces.PieceType1):
            NumberOfPieceThatExitedFromSystemInNonSetupTimeType1+=1;
    elif(type==TypeOfPieces.PieceType2):
            NumberOfPieceThatExitedFromSystemInNonSetupTimeType2+=1;


def ShowResult():
    ResultOfpiecesTable = pandas.DataFrame(columns=['Type Of Piece','Status of piece','EnterTime', 'ExitTime','In Queue Of MachineA','In Queue Of MachineB','In Queue Of MachineC From MachineA','In Queue Of MachineC From MachineB','InProcessing By MachineA','InProcessing By MachineB','InProcessing By MachineC','ResponseTime'])
    for OnePiece in ListOfPieces[NowNumberSimulationTime][:]:
        if(OnePiece.PieceStatus==PieceStatus.Exited):
            if(OnePiece.LogoutTime>TotalSetupTime):
                ResultOfpiecesTable = ResultOfpiecesTable.append({
                    'Type Of Piece':OnePiece.type,
                    'Status of piece':OnePiece.PieceStatus,
                    'EnterTime': OnePiece.LoginTime,
                    'ExitTime': OnePiece.LogoutTime,
                    'In Queue Of MachineA':OnePiece.TimeInQueueOfMachineA,
                    'In Queue Of MachineB':OnePiece.TimeInQueueOfMachineB,
                    'In Queue Of MachineC From MachineA':OnePiece.TimeInQueueOfMachineC_FromMachineA,
                    'In Queue Of MachineC From MachineB':OnePiece.TimeInQueueOfMachineC_FromMachineB,
                    'InProcessing By MachineA':OnePiece.TimeInProcessingByMachineA,
                    'InProcessing By MachineB':OnePiece.TimeInProcessingByMachineB,
                    'InProcessing By MachineC':OnePiece.TimeInProcessingByMachineC,
                    'ResponseTime': OnePiece.ResponseTime
                    }, ignore_index=True)

        else:
            ResultOfpiecesTable = ResultOfpiecesTable.append({
                'Type Of Piece':OnePiece.type,
                'Status of piece':OnePiece.PieceStatus,
                'EnterTime': OnePiece.LoginTime,
                'In Queue Of MachineA':OnePiece.TimeInQueueOfMachineA,
                'In Queue Of MachineB':OnePiece.TimeInQueueOfMachineB,
                'In Queue Of MachineC From MachineA':OnePiece.TimeInQueueOfMachineC_FromMachineA,
                'In Queue Of MachineC From MachineB':OnePiece.TimeInQueueOfMachineC_FromMachineB,
                'InProcessing By MachineA':OnePiece.TimeInProcessingByMachineA,
                'InProcessing By MachineB':OnePiece.TimeInProcessingByMachineB,
                'InProcessing By MachineC':OnePiece.TimeInProcessingByMachineC
                }, ignore_index=True)


    
    print('------------------------------------------------------------------')
    print("Result for each piece:")
    print('\n')
    print(ResultOfpiecesTable)

    
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
    print("Result for each machine:")
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
    print("Result for each type of piece:")
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
    print("Result for max of each queue:")
    print('\n')
    print(ResultOfMaxOfQueueTable)

    print('\n')
    print("******************************************************************")
    print(DetermineBottlenecksQueue(),"is bottlenecks")
    print("******************************************************************")



def CalculatePointAndIntervalEstimationOfMean():
    global ResultOfPointEstimation;
    global ResultOfIntervalEstimation;
    MeanOfPieceType1=numpy.mean(ResultOfResponseTime['AvrageResponseTimePieceType1'])
    MeanOfPieceType2=numpy.mean(ResultOfResponseTime['AvrageResponseTimePieceType2'])
    MeanOfTotalPieces=numpy.mean(ResultOfResponseTime['AvrageResponseTimeTotalPiece'])



    IntervalestimationPieceType1=t.interval(alpha=0.95,  df=NumberTotalSimulation-1, loc=MeanOfPieceType1, scale=sem(ResultOfResponseTime['AvrageResponseTimePieceType1'])) 
    IntervalestimationPieceType2=t.interval(alpha=0.95,  df=NumberTotalSimulation-1, loc=MeanOfPieceType2, scale=sem(ResultOfResponseTime['AvrageResponseTimePieceType2'])) 
    IntervalestimationTotalPieces=t.interval(alpha=0.95, df=NumberTotalSimulation-1, loc=MeanOfTotalPieces, scale=sem(ResultOfResponseTime['AvrageResponseTimeTotalPiece'])) 




    ResultOfPointEstimation=ResultOfPointEstimation.append({
        'PieceType':'Type1',
        'Point Estimation':MeanOfPieceType1
        }, ignore_index=True)
    ResultOfPointEstimation=ResultOfPointEstimation.append({
        'PieceType':'Type2',
        'Point Estimation':MeanOfPieceType2
        }, ignore_index=True)
    ResultOfPointEstimation=ResultOfPointEstimation.append({
        'PieceType':'Total',
        'Point Estimation':MeanOfTotalPieces
        }, ignore_index=True)



    ResultOfIntervalEstimation=ResultOfIntervalEstimation.append({
        'PieceType':'Type1',
        'Interval Estimation':IntervalestimationPieceType1
        }, ignore_index=True)

    ResultOfIntervalEstimation=ResultOfIntervalEstimation.append({
        'PieceType':'Type2',
        'Interval Estimation':IntervalestimationPieceType2
        }, ignore_index=True)

    ResultOfIntervalEstimation=ResultOfIntervalEstimation.append({
        'PieceType':'Total',
        'Interval Estimation':IntervalestimationTotalPieces
        }, ignore_index=True)


  
    

def SaveResult():
    global ResultOfResponseTime
    global ResultOfNumberOfPieceProducted;
    global ResultOfTotalExplotionRate
    global ResultOfMachineFailureRate
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType1;
    global NumberOfPieceThatExitedFromSystemInNonSetupTimeType2;


    SumResponseTimePieceType1=0;
    SumResponseTimePieceType2=0;
    for piece in  ListOfPieces[NowNumberSimulationTime][:]:
        if(piece.LogoutTime!=""):
            if(piece.LogoutTime>TotalSetupTime):
                if(piece.type==TypeOfPieces.PieceType1):
                    SumResponseTimePieceType1+=piece.ResponseTime;
                if(piece.type==TypeOfPieces.PieceType2):
                    SumResponseTimePieceType2+=piece.ResponseTime;

    AvrageResponseTimePieceType1=SumResponseTimePieceType1/NumberOfPieceThatExitedFromSystemInNonSetupTimeType1;
    AvrageResponseTimePieceType2=SumResponseTimePieceType2/NumberOfPieceThatExitedFromSystemInNonSetupTimeType2;
    AvrageResponseTimeTotalPiece=(SumResponseTimePieceType1+SumResponseTimePieceType2)/(NumberOfPieceThatExitedFromSystemInNonSetupTimeType1+NumberOfPieceThatExitedFromSystemInNonSetupTimeType2)

    
    ResultOfResponseTime = ResultOfResponseTime.append({
        'NumberSimulation':NowNumberSimulationTime+1,
        'AvrageResponseTimePieceType1':AvrageResponseTimePieceType1,
        'AvrageResponseTimePieceType2':AvrageResponseTimePieceType2,
        'AvrageResponseTimeTotalPiece':AvrageResponseTimeTotalPiece
        }, ignore_index=True)

    ResultOfNumberOfPieceProducted=ResultOfNumberOfPieceProducted.append({
        'NumberSimulation':NowNumberSimulationTime+1,
        'NumberOfPieceProductedType1':NumberOfPieceThatExitedFromSystemInNonSetupTimeType1,
        'NumberOfPieceProductedType2':NumberOfPieceThatExitedFromSystemInNonSetupTimeType2
        },ignore_index=True)
    
    ResultOfTotalExplotionRate=ResultOfTotalExplotionRate.append({
        'NumberSimulation':NowNumberSimulationTime+1,
        'TotalExplotionRateMachineA':MachineA.UsefulAndUnusefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
        'TotalExplotionRateMachineB':MachineB.UsefulAndUnusefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime),
        'TotalExplotionRateMachineC':MachineC.UsefulAndUnusefulServiceTimeForEachMachine/(TotalSimulationTime-TotalSetupTime)
        },ignore_index=True)
    
    ResultOfMachineFailureRate=ResultOfMachineFailureRate.append({
        'NumberSimulation':NowNumberSimulationTime+1,
        'MachineFailureRateMachineA':MachineA.DurationOfFailures/(TotalSimulationTime-TotalSetupTime),
        'MachineFailureRateMachineB':MachineB.DurationOfFailures/(TotalSimulationTime-TotalSetupTime),
        'MachineFailureRateMachineC':MachineC.DurationOfFailures/(TotalSimulationTime-TotalSetupTime)
        },ignore_index=True)
    



def ShowEstimationOfMean():
    CalculatePointAndIntervalEstimationOfMean()
    print("Point Estimation Of the Whole Simulation Process")
    print('\n')
    print(ResultOfPointEstimation)
    print('\n')
    print('\n')
    print("Interval Estimation Of the Whole Simulation Process")
    print('\n')
    print(ResultOfIntervalEstimation)



def DrawAllPlots():
    Draw_ResultOfResponseTime();
    Draw_ResultOfTotalExplotionRate();
    Draw_ResultOfMachineFailureRate();
    Draw_ResultOfNumberOfPieceProducted();

def Draw_ResultOfResponseTime():
    plt.figure(figsize=(10,6))

    sns.lineplot(x ='NumberSimulation', y='AvrageResponseTimePieceType1', data=ResultOfResponseTime, label='Piece Type1', marker="o")
    sns.lineplot(x ='NumberSimulation', y='AvrageResponseTimePieceType2', data=ResultOfResponseTime, label='Piece Type2', marker="o")
    
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.title('Average ResponseTime For Each Type of Pieces Per Simulation', fontsize=14)
    plt.xlabel('Simulation Number', fontsize=12)
    plt.xticks(ticks=numpy.arange(1,11))
    plt.ylabel('Average Response Time', fontsize=12)
    plt.show()

def Draw_ResultOfTotalExplotionRate():
    plt.figure(figsize=(10,6))

    sns.lineplot(x ='NumberSimulation', y='TotalExplotionRateMachineA', data=ResultOfTotalExplotionRate, label='Machine A', marker="o")
    sns.lineplot(x ='NumberSimulation', y='TotalExplotionRateMachineB', data=ResultOfTotalExplotionRate, label='Machine B', marker="o")
    sns.lineplot(x ='NumberSimulation', y='TotalExplotionRateMachineC', data=ResultOfTotalExplotionRate, label='Machine C', marker="o")    
    
    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.title('Total Exploitation Rate For Each Machine Per Simulation', fontsize=14)
    plt.xlabel('Simulation Number', fontsize=12)
    plt.xticks(ticks=numpy.arange(1,11))
    plt.ylabel('Total Exploitation Rate', fontsize=12)

    plt.show()

def Draw_ResultOfMachineFailureRate():
    plt.figure(figsize=(10,6))

    sns.lineplot(x ='NumberSimulation', y='MachineFailureRateMachineA', data=ResultOfMachineFailureRate, label='Machine A', marker="o")
    sns.lineplot(x ='NumberSimulation', y='MachineFailureRateMachineB', data=ResultOfMachineFailureRate, label='Machine B', marker="o")
    sns.lineplot(x ='NumberSimulation', y='MachineFailureRateMachineC', data=ResultOfMachineFailureRate, label='Machine C', marker="o")    

    plt.legend(bbox_to_anchor=(1, 1), loc='upper left')
    plt.title('Machine Failure Rate For Each Machine Per Simulation', fontsize=14)
    plt.xlabel('Simulation Number', fontsize=12)
    plt.xticks(ticks=numpy.arange(1,11))
    plt.ylabel('Machine Failure Rate', fontsize=12)
    
    plt.show()

def Draw_ResultOfNumberOfPieceProducted():
    plt.figure(figsize=(10,6))

    # For a better result, unpivot "ResultOfNumberOfPieceProducted" dataframe
    ResultOfNumberOfPieceProducted_unpivoted = ResultOfNumberOfPieceProducted.melt(id_vars=['NumberSimulation'], var_name='TypeOfProducedPiece', value_name='NumberOfProducedPieces')
    ax = sns.barplot(data = ResultOfNumberOfPieceProducted_unpivoted, x='NumberSimulation', y='NumberOfProducedPieces'
                , hue='TypeOfProducedPiece')

    #Legend modifications
    labels=["Piece Type1", "Piece Type2"]
    h, l = ax.get_legend_handles_labels()
    ax.legend(h,labels, bbox_to_anchor=(1, 1), loc='upper left')
    
    
    plt.title('Number of Pieces Producted Per Simulation', fontsize=14)
    plt.xlabel('Simulation Number', fontsize=12)
    plt.xticks(ticks=numpy.arange(1,11))
    plt.ylabel('Number of Pieces', fontsize=12)
    plt.show()


