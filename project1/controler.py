from EventFunctions import *
from Functions import *


#Function about Events
def TransitionToEvent(code):
    if(code==Event.EnterPieceForMachineA):
        event_EnterPieceForMachineA();
    elif(code==Event.EnterPieceForMachineB):
        event_EnterPieceForMachineB();
    elif(code==Event.CompletionOfServiceOfMachineA):
        event_CompletionOfServiceOfMachineA();
    elif(code==Event.CompletionOfServiceOfMachineB):
        event_CompletionOfServiceOfMachineB();
    elif(code==Event.CompletionOfServiceOfMachineC):
        event_CompletionOfServiceOfMachineC();
    elif(code==Event.OccurrenceOfMachineFailureA):
        event_OccurrenceOfMachineFailureA();
    elif(code==Event.OccurrenceOfMachineFailureB):
        event_OccurrenceOfMachineFailureB();
    elif(code==Event.FinishMachineRepairingA):
        event_FinishMachineRepairingA();
    elif(code==Event.FinishMachineRepairingB):
        event_FinishMachineRepairingB();
    else:
        print("Error")




#Controler
for NumberOfSimulation in range(0,10):
    initializationOfVariables(NumberOfSimulation);
    while(isFinishedTime()==False):
        DeterminingFEL();
        MoveTimeToFEL();
        TransitionToEvent(SpecifyCodeNumber())

    #show result
    print("Result of",NumberOfSimulation+1,"th Simulation:")
    print("___________________________")
    ShowResult()
    SaveResult()
    print("\n\n\n\n\n\n\n\n\n\n\n\n");


ShowEstimationOfMean()
DrawAllPlots()