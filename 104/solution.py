isPandigital = False
currentFiboNumber = 1
fn_minus1 = 1
fn_minus2 = 1
k = 2
blueprint = [1,2,3,4,5,6,7,8,9]

while not isPandigital:
    currentFiboNumber = fn_minus1 + fn_minus2
    fn_minus2 = fn_minus1
    fn_minus1 = currentFiboNumber
    k += 1
    print(k)
    if (len(str(currentFiboNumber)) >= 18):
        stringNum = str(currentFiboNumber)
        startList = [int(digit) for digit in stringNum[:9]]
        startList.sort()
        endList = [int(digit) for digit in stringNum[-9:]]
        endList.sort()
        isPandigital = (startList == endList) and (startList == blueprint)
print("Its the",k,"th element.")
print("The resulting number is:",currentFiboNumber)
