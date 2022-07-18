def linearSearch(numList,item):
  for element in numList:
    if element == item:
      return True
  return False

def binarySearch(numList, item):
  if len(numList) == 0:
    return False
  else:
    middle = len(numList)//2
    if numList[middle]==item:
      return True
    else:
      if item < numList[middle]:
        return binarySearch(numList[:middle],item)
      else:
        return binarySearch(numList[middle+1:],item)
  