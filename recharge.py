dayNum = 80
numOfCalls = 3001
dataUsed = 2.2
msgSend = 101
print("\n\n")
print("Kindly Recharge" if (dayNum > 84) else f"{84-dayNum} Days left for plan to expires you do\nCall could not be connected, you reached your call limits\nData is working but slow\nMsg cannot be send, you reached your msg limit" if (dataUsed > 2.0 and numOfCalls > 3000 and msgSend > 100) else "Data is working but slow" if (dataUsed > 2.0) else "Call could not be connected, you reached your call limits" if (
    numOfCalls > 3000) else "Msg cannot be send, you reached your msg limit" if (msgSend > 100) else f"{84-dayNum} Days left for plan to expires\n Yet to use :\nMsg = {100-msgSend} call = {3000-numOfCalls} Data = {2.0-dataUsed}")
print("\n\n")
