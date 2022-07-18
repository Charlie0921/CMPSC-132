def insertionSort(numList):
  for i in range(1, len(numList)):
    pos = i
    while pos > 0 and numList[pos] < numList[pos-1]:
      numList[pos-1], numList[pos] = numList[pos], numList[pos-1]
      pos -= 1
  return numList

def selectionSort(numList):
  n = len(numList)
  for i in range(n):
    for j in range(i,n):
      if numList[i] > numList[j]:
        numList[i], numList[j] = numList[j], numList[i]
  return numList

#inplace algorithm -> mutability of the list, changing all the elements in place
