from Functions import *
#******************************#
#****define Event Functions****#
#******************************#
def event_EnterPieceForMachineA():
    piece=HandelEnterOfNewPieceEntered(TypeOfPieces.PieceType1)
    AddEventToFEL(Event.EnterPieceForMachineA,DetermineTimeOfEnterOfNextPiece(TypeOfPieces.PieceType1));

    if(isMachineNotBusy(MachineA)):
        MachineA.ChangeMachineStatus(MachineStatus.Serving);
        MachineA.StartProssesOnPieceByMachine(piece)
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineA);
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineA)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineA)
        AddEventToFEL(Event.CompletionOfServiceOfMachineA,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineA.add_NumberOfPieceStartedProssesByMachine();

    elif(isMachineServing(MachineA)):
        QueueOfEnterToMachineA.AppendPieceToQueue(piece);
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InQueueOfMachineA);
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineA)
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineA)
    elif(isMachineRepairing(MachineA)):
        QueueOfEnterToMachineBType1.AppendPieceToQueue(piece);
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineB)
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType1)
  
    RemoveEventFromFEL(0);








def event_EnterPieceForMachineB():
    piece=HandelEnterOfNewPieceEntered(TypeOfPieces.PieceType2);
    AddEventToFEL(Event.EnterPieceForMachineB,DetermineTimeOfEnterOfNextPiece(TypeOfPieces.PieceType2));
    if(isMachineNotBusy(MachineB)):
        MachineB.ChangeMachineStatus(MachineStatus.Serving);
        MachineB.StartProssesOnPieceByMachine(piece);
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineB);
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineB)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece2ByMachineB);
        AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineB.add_NumberOfPieceStartedProssesByMachine();

    else:
        QueueOfEnterToMachineBType2.AppendPieceToQueue(piece)
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InQueueOfMachineB);
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InQueueOfMachineB)
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType2);
    RemoveEventFromFEL(0);






def event_OccurrenceOfMachineFailureA():
    MachineA.ChangeMachineStatus(MachineStatus.Repairing);
    if(IsThereComplitionEventForMachineInFEL(TypeOfMachine.MachineTypeA)):
        RemoveEventFromFEL(FindIndexOfFELCompletionOfService(TypeOfMachine.MachineTypeA));
        if(isMachineNotBusy(MachineB)):
            MachineB.ChangeMachineStatus(MachineStatus.Serving);
            MovePieceThatWasProssesingByMachineAToMachineB();
        else:
            MovePieceThatWasProssesingByMachineAToQueueB();
        MoveQueueOfMachineAToQuereMachineB();
        ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType1);

    durationOfRepairing=DetermineDurationOfReaparing(TypeOfMachine.MachineTypeA);
    MachineA.add_DurationOfFailures(durationOfRepairing);
    AddEventToFEL(Event.FinishMachineRepairingA,DetermineFinishOfReaparing(durationOfRepairing));
    if(isNowInSetupTime()==False):
        MachineA.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineA.Calculate_ServiceTimeForMachineInNonSetupTime());

    RemoveEventFromFEL(0);






def event_OccurrenceOfMachineFailureB():
    MachineB.ChangeMachineStatus(MachineStatus.Repairing);

    if(IsThereComplitionEventForMachineInFEL(TypeOfMachine.MachineTypeB)):
        RemoveEventFromFEL(FindIndexOfFELCompletionOfService(TypeOfMachine.MachineTypeB));

    durationOfRepairing=DetermineDurationOfReaparing(TypeOfMachine.MachineTypeB);
    MachineB.add_DurationOfFailures(durationOfRepairing);
    AddEventToFEL(Event.FinishMachineRepairingB,DetermineFinishOfReaparing(durationOfRepairing));

    if(isNowInSetupTime()==False):
        MachineB.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineB.Calculate_ServiceTimeForMachineInNonSetupTime());
    MovePieceThatWasProssesingByMachineBToQueueB();
    ProssesForDetermineMaxofQueue(QueueOfEnterToMachineBType2);
    
    RemoveEventFromFEL(0);







def event_FinishMachineRepairingA():
    MachineA.ChangeMachineStatus(MachineStatus.NotBusy);
    AddEventToFEL(Event.OccurrenceOfMachineFailureA,DetermineTimeOfNextOfOccurrenceFailureMachine(TypeOfMachine.MachineTypeA));
    RemoveEventFromFEL(0);






def event_FinishMachineRepairingB():
    MachineB.ChangeMachineStatus(MachineStatus.NotBusy);
    AddEventToFEL(Event.OccurrenceOfMachineFailureB,DetermineTimeOfNextOfOccurrenceFailureMachine(TypeOfMachine.MachineTypeB));
    RemoveEventFromFEL(0);






def event_CompletionOfServiceOfMachineA(): 
    if(isNowInSetupTime()==False):
        MachineA.add_NumberOfPieceComplitedProcessByMachine();
        MachineA.Add_JustUsefulServiceTimeForEachMachine(MachineA.Calculate_ServiceTimeForMachineInNonSetupTime())
        MachineA.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineA.Calculate_ServiceTimeForMachineInNonSetupTime())

    if(isMachineNotBusy(MachineC)):
        MachineC.ChangeMachineStatus(MachineStatus.Serving);
        piece1=MachineA.LastPieceThatMachineStartedToProsses;
        MachineC.StartProssesOnPieceByMachine(piece1);
        piece1.ApplyEndTimeOfLastPosion();
        piece1.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        piece1.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineC)
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
        piece2.ApplyEndTimeOfLastPosion();
        piece2.ChangePieceStatus(PieceStatus.InProcessingByMachineA)
        piece2.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineA)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineA);
        AddEventToFEL(Event.CompletionOfServiceOfMachineA,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineA.add_NumberOfPieceStartedProssesByMachine();

    else:
        MachineA.ChangeMachineStatus(MachineStatus.NotBusy)
    RemoveEventFromFEL(0);









def event_CompletionOfServiceOfMachineB():
    if(isNowInSetupTime()==False):
        MachineB.add_NumberOfPieceComplitedProcessByMachine();
        MachineB.Add_JustUsefulServiceTimeForEachMachine(MachineB.Calculate_ServiceTimeForMachineInNonSetupTime())
        MachineB.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineB.Calculate_ServiceTimeForMachineInNonSetupTime())

    if(isMachineNotBusy(MachineC)):
        MachineC.ChangeMachineStatus(MachineStatus.Serving);
        piece1=MachineB.LastPieceThatMachineStartedToProsses;
        piece1.ApplyEndTimeOfLastPosion();
        piece1.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        piece1.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineC)
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
        piece2.ApplyEndTimeOfLastPosion();
        piece2.ChangePieceStatus(PieceStatus.InProcessingByMachineB)
        piece2.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineB)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineB);
        AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineB.add_NumberOfPieceStartedProssesByMachine();

    elif(QueueOfEnterToMachineBType2.isQueueEmpty()==False):
        piece2=QueueOfEnterToMachineBType2.popPieceFromQueue();
        MachineB.StartProssesOnPieceByMachine(piece2)
        piece2.ApplyEndTimeOfLastPosion();
        piece2.ChangePieceStatus(PieceStatus.InProcessingByMachineB)
        piece2.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineB)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceForPiece1ByMachineB);
        AddEventToFEL(Event.CompletionOfServiceOfMachineB,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineB.add_NumberOfPieceStartedProssesByMachine();

    else:
        MachineB.ChangeMachineStatus(MachineStatus.NotBusy)
    RemoveEventFromFEL(0);







def event_CompletionOfServiceOfMachineC():
    ProssesForExitOfLastPieceThatCompliteServiceByLastMachineOfSystem();
    if(isNowInSetupTime()==False):
        MachineC.add_NumberOfPieceComplitedProcessByMachine();
        MachineC.Add_JustUsefulServiceTimeForEachMachine(MachineC.Calculate_ServiceTimeForMachineInNonSetupTime())
        MachineC.Add_UsefulAndUnusefulServiceTimeForEachMachine(MachineC.Calculate_ServiceTimeForMachineInNonSetupTime())
        add_NumberOfPieceThatExitedFromSystemInNonSetupTime(MachineC.LastPieceThatMachineStartedToProsses.type);



    if(QueueOfEnterToMachineC_FromMachineA.isQueueEmpty()==False):
        piece=QueueOfEnterToMachineC_FromMachineA.popPieceFromQueue();
        MachineC.StartProssesOnPieceByMachine(piece)
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineC)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceByMachineC);
        AddEventToFEL(Event.CompletionOfServiceOfMachineC,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineC.add_NumberOfPieceStartedProssesByMachine();

    elif(QueueOfEnterToMachineC_FromMachineB.isQueueEmpty()==False):
        piece=QueueOfEnterToMachineC_FromMachineB.popPieceFromQueue();
        MachineC.StartProssesOnPieceByMachine(piece)
        piece.ApplyEndTimeOfLastPosion();
        piece.ChangePieceStatus(PieceStatus.InProcessingByMachineC)
        piece.ApplyStartTimeOfNewPosion(PieceStatus.InProcessingByMachineC)
        serviceDeuration=DeterminingDurationOfService(TypeOfService.ServiceByMachineC);
        AddEventToFEL(Event.CompletionOfServiceOfMachineC,CalculteTimeOfCompletionService(serviceDeuration));
        if(isNowInSetupTime()==False):
            MachineC.add_NumberOfPieceStartedProssesByMachine();
    
    else:
        MachineC.ChangeMachineStatus(MachineStatus.NotBusy)
    RemoveEventFromFEL(0);
