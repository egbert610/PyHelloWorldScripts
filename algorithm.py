#intsA = [-1,3,8,2,9,5]
#intsB = [4,1,2,10,5,20]
intsA = [7,4,1,10]
intsB = [4,5,8,7]
def FindCloserInSum2(array1,array2,targetNumber):
    listB = (intsB)
    closestN = 99
    strOutput = ""
    for number in intsA:
        for i in range(closestN+1):
            if (targetNumber-number-i in intsB) or (targetNumber-number+i in intsB):
                closestN = i
                break
    print(f'closest Number = {closestN}')
    for number in intsA:
        if (targetNumber-number-closestN in intsB):
            strOutput = strOutput + f'({number},{targetNumber-number-closestN})'
        if (targetNumber-number+closestN in intsB) and closestN>0:
            strOutput = strOutput + f'({number},{targetNumber - number + closestN})'
    return strOutput

print(FindCloserInSum2(intsA,intsB,16))