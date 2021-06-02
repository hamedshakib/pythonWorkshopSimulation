from Functions import *
#******************************#
#****define Event Functions****#
#******************************#
def event_EnterPieceForMachineA():
    print("event Enter Machine A:")
    piece=HandelEnterOfNewPieceEntered(TypeOfPieces.PieceType1)
    AddEventToFEL(Event.EnterPieceForMachineA,DetermineTimeOfEnterOfNextPiece(TypeOfPieces.PieceType1));
    #ToDo continue
    if(isMachineNotBusy(MachineA)):
        #ToDo start prossed by machie1
        MachineA.ChangeMachineStatus(MachineStatus.Serving);
        MachineA.StartProssesOnPieceByMachine(piece)
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineA);
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineA)
        AddEventToFEL(Event.CompletionOfServiceOfMachineA,CalculteTimeOfCompletionService(serviceDeuration));
        print("*!compliteAService:",CalculteTimeOfCompletionService(serviceDeuration))
        if(isNowInSetupTime()==False):
            MachineA.add_NumberOfPieceStartedProssesByMachine();

    elif(isMachineServing(MachineA)):
        print("-*-")
        QueueOfEnterToMachineA.AppendPieceToQueue(piece);
        piece.ChangePieceStatus(PieceStatus.InQueueOfMachineA);
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineA)
    elif(isMachineRepairing(MachineA)):
        QueueOfEnterToMachineBType1.AppendPieceToQueue(piece);
        piece.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType1)
  
    RemoveEventFromFEL(0);








def event_EnterPieceForMachineB():
    print("event Enter Machine B:")
    piece=HandelEnterOfNewPieceEntered(TypeOfPieces.PieceType2);
    AddEventToFEL(Event.EnterPieceForMachineB,DetermineTimeOfEnterOfNextPiece(TypeOfPieces.PieceType2));
    if(isMachineNotBusy(MachineB)):
        MachineB.ChangeMachineStatus(MachineStatus.Serving);
        MachineB.StartProssesOnPieceByMachine(piece);
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineB);
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece2ByMachineB);
        AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineB.add_NumberOfPieceStartedProssesByMachine();

    else:
        QueueOfEnterToMachineBType2.AppendPieceToQueue(piece)
        piece.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType2);
    RemoveEventFromFEL(0);






def event_OccurrenceOfMachineFailureA():
    print("event Failure A:")
    #DurationOfReaparing=DetermineDurationOfReaparing(TypeOfMachine.MachineTypeA);
    MachineA.ChangeMachineStatus(MachineStatus.Repairing);
    if(IsThereComplitionEventForMachineInFEL(TypeOfMachine.MachineTypeA)):
        RemoveEventFromFEL(FindIndexOfFELCompletionOfService(TypeOfMachine.MachineTypeA));
        if(isMachineNotBusy(MachineB)):
            MachineB.ChangeMachineStatus(MachineStatus.Serving);
            MovePieceThatWasProssesingByMachineAToMachineB();
        MoveQueueOfMachineAToQuereMachineB();
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType1);

    print("YYYYYYY");
    durationOfRepairing=DetermineDurationOfReaparing(TypeOfMachine.MachineTypeA);
    MachineA.add_DurationOfFailures(durationOfRepairing);
    AddEventToFEL(Event.FinishMachineRepairingA,DetermineFinishOfReaparing(durationOfRepairing));
    print("Y12Y");
    if(isNowInSetupTime()==False):
        MachineA.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineA.Calculate_ServiceTimeForMachineInNonSetupTime());

    RemoveEventFromFEL(0);






def event_OccurrenceOfMachineFailureB():
    print("event Failure B:")
    MachineB.ChangeMachineStatus(MachineStatus.Repairing);
    if(IsThereComplitionEventForMachineInFEL(TypeOfMachine.MachineTypeB)):
        RemoveEventFromFEL(FindIndexOfFELCompletionOfService(TypeOfMachine.MachineTypeB));
    print("YYYYYYY");
    durationOfRepairing=DetermineDurationOfReaparing(TypeOfMachine.MachineTypeB);
    MachineB.add_DurationOfFailures(durationOfRepairing);
    AddEventToFEL(Event.FinishMachineRepairingB,DetermineFinishOfReaparing(durationOfRepairing));
    print("Y12Y");
    if(isNowInSetupTime()==False):
        MachineB.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineB.Calculate_ServiceTimeForMachineInNonSetupTime());
    #ToDo for prosses of Que
    MovePieceThatWasProssesingByMachineBToQueueB();
    ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType2);
    
    RemoveEventFromFEL(0);







def event_FinishMachineRepairingA():
    print("event finish repair A:")
    MachineA.ChangeMachineStatus(MachineStatus.NotBusy);
    AddEventToFEL(Event.OccurrenceOfMachineFailureA,DetermineTimeOfNextOfOccurrenceFailureMachine(TypeOfMachine.MachineTypeA));
    RemoveEventFromFEL(0);






def event_FinishMachineRepairingB():
    print("event finish repair B:")
    MachineB.ChangeMachineStatus(MachineStatus.NotBusy);
    AddEventToFEL(Event.OccurrenceOfMachineFailureB,DetermineTimeOfNextOfOccurrenceFailureMachine(TypeOfMachine.MachineTypeB));
    RemoveEventFromFEL(0);






def event_CompletionOfServiceOfMachineA(): 
    print("event Completion Machine A:")
    if(isNowInSetupTime()==False):
        MachineA.add_NumberOfPieceComplitedProcessByMachine();
        MachineA.Add_JustUsefulServiceTimeForEachMachine(MachineA.Calculate_ServiceTimeForMachineInNonSetupTime())
        MachineA.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineA.Calculate_ServiceTimeForMachineInNonSetupTime())
    #ToDo
    if(isMachineNotBusy(MachineC)):
        MachineC.ChangeMachineStatus(MachineStatus.Serving);
        piece1=MachineA.LastPieceThatMachineStartedToProsses;
        MachineC.StartProssesOnPieceByMachine(piece1);
        piece1.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceByMachineC);
        AddEventToFEL(Event.CompletionOfServiceOfMachineC,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineC.add_NumberOfPieceStartedProssesByMachine();
    else:
        MovePieceToQueueOfEnterToMachineC_FromMachineA();
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineC_FromMachineA);


    if(QueueOfEnterToMachineA.isQueueEmpty()==False):
        piece2=QueueOfEnterToMachineA.popPieceFromQueue();
        MachineA.StartProssesOnPieceByMachine(piece2)
        piece2.ChangePieceStatus(PieceStatus.InProcessingByMachineA)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineA);
        AddEventToFEL(Event.CompletionOfServiceOfMachineA,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineA.add_NumberOfPieceStartedProssesByMachine();

    else:
        MachineA.ChangeMachineStatus(MachineStatus.NotBusy)
    RemoveEventFromFEL(0);









def event_CompletionOfServiceOfMachineB():
    print("event Completion Machine B:")
    if(isNowInSetupTime()==False):
        MachineB.add_NumberOfPieceComplitedProcessByMachine();
        MachineB.Add_JustUsefulServiceTimeForEachMachine(MachineB.Calculate_ServiceTimeForMachineInNonSetupTime())
        MachineB.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineB.Calculate_ServiceTimeForMachineInNonSetupTime())
    #ToDo
    if(isMachineNotBusy(MachineC)):
        MachineC.ChangeMachineStatus(MachineStatus.Serving);
        piece1=MachineB.LastPieceThatMachineStartedToProsses;
        piece1.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        MachineC.StartProssesOnPieceByMachine(piece1);
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceByMachineC);
        AddEventToFEL(Event.CompletionOfServiceOfMachineC,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineC.add_NumberOfPieceStartedProssesByMachine();
    else:
        MovePieceToQueueOfEnterToMachineC_FromMachineB();
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineC_FromMachineB);

    if(QueueOfEnterToMachineBType1.isQueueEmpty()==False):
        piece2=QueueOfEnterToMachineBType1.popPieceFromQueue();
        MachineB.StartProssesOnPieceByMachine(piece2)
        piece2.ChangePieceStatus(PieceStatus.InProcessingByMachineB)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineB);
        AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineB.add_NumberOfPieceStartedProssesByMachine();

    elif(QueueOfEnterToMachineBType2.isQueueEmpty()==False):
        piece2=QueueOfEnterToMachineBType2.popPieceFromQueue();
        MachineB.StartProssesOnPieceByMachine(piece2)
        piece2.ChangePieceStatus(PieceStatus.InProcessingByMachineB)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineB);
        AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineB.add_NumberOfPieceStartedProssesByMachine();

    else:
        MachineB.ChangeMachineStatus(MachineStatus.NotBusy)
    RemoveEventFromFEL(0);







def event_CompletionOfServiceOfMachineC():
    print("event Completion Machine C:")
    ProssesForExitOfLastPieceThatCompliteServiceByLastMachineOfSystem();
    if(isNowInSetupTime()==False):
        MachineC.add_NumberOfPieceComplitedProcessByMachine();
        MachineC.Add_JustUsefulServiceTimeForEachMachine(MachineC.Calculate_ServiceTimeForMachineInNonSetupTime())
        MachineC.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineC.Calculate_ServiceTimeForMachineInNonSetupTime())
        add_NumberOfPieceThatExitedFromSystemInNonSetupTime(MachineC.LastPieceThatMachineStartedToProsses.type);



    if(QueueOfEnterToMachineC_FromMachineA.isQueueEmpty()==False):
        piece=QueueOfEnterToMachineC_FromMachineA.popPieceFromQueue();
        MachineC.StartProssesOnPieceByMachine(piece)
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceByMachineC);
        AddEventToFEL(Event.CompletionOfServiceOfMachineC,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineC.add_NumberOfPieceStartedProssesByMachine();

    elif(QueueOfEnterToMachineC_FromMachineB.isQueueEmpty()==False):
        piece=QueueOfEnterToMachineC_FromMachineB.popPieceFromQueue();
        MachineC.StartProssesOnPieceByMachine(piece)
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceByMachineC);
        AddEventToFEL(Event.CompletionOfServiceOfMachineC,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineC.add_NumberOfPieceStartedProssesByMachine();
    
    else:
        MachineC.ChangeMachineStatus(MachineStatus.NotBusy)
    RemoveEventFromFEL(0);
