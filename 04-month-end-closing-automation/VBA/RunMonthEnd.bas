Attribute VB_Name = "Module1"
Sub RunMonthEnd()

    Dim Status As String
    Dim Details As String
    Dim StartTime As Double

    ' Start refresh
    ThisWorkbook.RefreshAll

    ' Wait for refresh to complete
    StartTime = Timer

    Do
        DoEvents
        Application.Wait Now + TimeValue("00:00:01")

        ' Safety timeout: 60 seconds
        If Timer - StartTime > 60 Then
            MsgBox "The refresh process took too long." & vbCrLf & vbCrLf & _
                   "Please check the Power Query connections.", _
                   vbExclamation, "Month-End Closing"
            Exit Sub
        End If

    Loop While Application.CalculationState <> xlDone

    ' Read final status
    Status = Sheets("Closing Control").Range("B9").Value
    Details = Sheets("Closing Control").Range("C9").Value

    ' Display result
    If Status = "WARNING" Then

        MsgBox "Month-End Closing completed." & vbCrLf & vbCrLf & _
               "Overall Status: " & Status & vbCrLf & _
               Details & vbCrLf & vbCrLf & _
               "Please review the Exception Details sheet.", _
               vbExclamation, "Month-End Closing"

    Else

        MsgBox "Month-End Closing completed." & vbCrLf & vbCrLf & _
               "Overall Status: " & Status & vbCrLf & _
               Details, _
               vbInformation, "Month-End Closing"

    End If

End Sub
