# HW5
# REMINDER: The work in this assignment must be your own original work and must be completed alone.
# Don't forget to list any authorized forms of collaboration using a Collaboration Statement
# https://psu.instructure.com/courses/2171635/pages/week-13-review-sessions

class Node:
    def __init__(self, content):
        self.value = content
        self.next = None

    def __str__(self):
        return ('CONTENT:{}\n'.format(self.value))

    __repr__=__str__


class ContentItem:
    '''
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content3 = ContentItem(1005, 18, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content4 = ContentItem(1005, 18, "another header", "111110")
        >>> hash(content1)
        0
        >>> hash(content2)
        1
        >>> hash(content3)
        2
        >>> hash(content4)
        1
    '''
    def __init__(self, cid, size, header, content):
        self.cid = cid
        self.size = size
        self.header = header
        self.content = content

    def __str__(self):
        return f'CONTENT ID: {self.cid} SIZE: {self.size} HEADER: {self.header} CONTENT: {self.content}'

    __repr__=__str__

    def __eq__(self, other):
        if isinstance(other, ContentItem):
            return self.cid == other.cid and self.size == other.size and self.header == other.header and self.content == other.content
        return False

    def __hash__(self):
      # sum the ASCII values of the header and mod the sum by 3
      value = 0
      for item in self.header:
        value += ord(item)
      return value % 3



class CacheList:
    '''
        >>> content1 = ContentItem(1000, 10, "Content-Type: 0", "0xA")
        >>> content2 = ContentItem(1004, 50, "Content-Type: 1", "110010")
        >>> content3 = ContentItem(1005, 180, "Content-Type: 2", "<html><p>'CMPSC132'</p></html>")
        >>> content4 = ContentItem(1006, 18, "another header", "111110")
        >>> content5 = ContentItem(1008, 2, "items", "11x1110")
        >>> lst=CacheList(200)
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst.put(content2, 'lru')
        'INSERTED: CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010'
        >>> lst.put(content4, 'mru')
        'INSERTED: CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110'
        >>> lst
        REMAINING SPACE:122
        ITEMS:3
        LIST:
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        >>> lst.put(content5, 'mru')
        'INSERTED: CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110'
        >>> lst
        REMAINING SPACE:120
        ITEMS:4
        LIST:
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1004 SIZE: 50 HEADER: Content-Type: 1 CONTENT: 110010]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        >>> lst.put(content3, 'lru')
        "INSERTED: CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>"
        >>> lst
        REMAINING SPACE:0
        ITEMS:3
        LIST:
        [CONTENT ID: 1005 SIZE: 180 HEADER: Content-Type: 2 CONTENT: <html><p>'CMPSC132'</p></html>]
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        <BLANKLINE>
        >>> lst.put(content1, 'mru')
        'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        <BLANKLINE>
        >>> 1006 in lst
        True
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1008 SIZE: 2 HEADER: items CONTENT: 11x1110]
        <BLANKLINE>
        >>> contentExtra = ContentItem(1034, 2, "items", "other content")
        >>> lst.update(3000, contentExtra)
        'Cache miss!'
        >>> lst.update(1008, contentExtra)
        'UPDATED: CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content'
        >>> 1008 in lst
        False
        >>> lst
        REMAINING SPACE:170
        ITEMS:3
        LIST:
        [CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content]
        [CONTENT ID: 1006 SIZE: 18 HEADER: another header CONTENT: 111110]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>
        
        >>> contentExtraDiff = ContentItem(1504, 150, "more items", "other content")
        >>> lst.update(1006, contentExtraDiff)
        'UPDATED: CONTENT ID: 1504 SIZE: 150 HEADER: more items CONTENT: other content'
        >>> lst
        REMAINING SPACE:38
        ITEMS:3
        LIST:
        [CONTENT ID: 1504 SIZE: 150 HEADER: more items CONTENT: other content]
        [CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content]
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        <BLANKLINE>

        >>> contentExtraMore = ContentItem(2504, 50, "other items", "other content")
        >>> lst.update(1000, contentExtraMore)
        'Cache miss!'
        >>> lst
        REMAINING SPACE:38
        ITEMS:3
        LIST:
        [CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA]
        [CONTENT ID: 1504 SIZE: 150 HEADER: more items CONTENT: other content]
        [CONTENT ID: 1034 SIZE: 2 HEADER: items CONTENT: other content]
        <BLANKLINE>

    
        >>> lst.clear()
        'Cleared cache!'
        >>> lst
        REMAINING SPACE:200
        ITEMS:0
        LIST:
        <BLANKLINE>
    '''
    
    def __init__(self, size):
        self.head = None
        self.maxSize = size
        self.remainingSpace = size
        self.numItems = 0

    def __str__(self):
        listString = ""
        current = self.head
        while current is not None:
            listString += "[" + str(current.value) + "]\n"
            current = current.next
        return 'REMAINING SPACE:{}\nITEMS:{}\nLIST:\n{}'.format(self.remainingSpace, self.numItems, listString)  

    __repr__=__str__

    def __len__(self):
        return self.numItems


    #A portion o your grade in this class comes from your ability to reuse code by calling other methods
    #lst.put(content1, 'mru')
    #'INSERTED: CONTENT ID: 1000 SIZE: 10 HEADER: Content-Type: 0 CONTENT: 0xA'
    def put(self, content, evictionPolicy):
        # YOUR CODE STARTS HERE
        # Check if size of content exceeds maxSize.
        # Check if cid is already in CacheList
        # Remove items according to evictionPolicy until there is enough space to insert content
        # insert ContentItem at beginning of list
      if self.maxSize >= content.size:
        if content.cid in self:
          return f'Content {content.cid} already in cache, insertion not allowed'
        else:
          while self.remainingSpace < content.size:
            if evictionPolicy == "mru":
              self.mruEvict()
            elif evictionPolicy == "lru":
              self.lruEvict()
              
          new = Node(content)
          new.next = self.head
          self.head = new
          self.numItems += 1
          self.remainingSpace -= content.size
          print(self)
          return f"INSERTED: {content}"
      else:
        return "Insertion not allowed"

      
    def __contains__(self, cid):
      if self.numItems > 1:
        current = self.head
        previous = None
        count = 0
        while count < self.numItems:
          if current.value.cid == cid:
            if previous == None:
              return True
            else:
              if current.next == None:
                previous.next = None
              else:
                previous.next = current.next
              current.next = self.head
              self.head = current
              return True
          previous = current
          current = current.next
          count += 1
      return False
   
        # YOUR CODE STARTS HERE
        # REMINDER: Need a current and previous pointer
        # Traverse the CacheList and compare cid's. If cid's are equal, then move node to head and return True.
        # If not, return False
      


    def update(self, cid, content):
        # YOUR CODE STARTS HERE
        # cid associated, new content item 
      if cid in self:
        self.remainingSpace += self.head.value.size
        if content.size <= self.remainingSpace:
          self.head.value = content
          self.remainingSpace -= content.size
          print(self)
          return f'UPDATED: {content}'
        else:
          self.remainingSpace -= self.head.value.size
          return "Cache miss!"
      else:
        return "Cache miss!"
        # get the old contentItem to the head of the CacheList
        # Check if size would be violated
        # if size not violated, replace old ContentItem (aka self.head) with new Contentitem
        # if size is violated, return "Cache miss!"
        


    def mruEvict(self):
        # Remove the head of the CacheList (need special cases for length 0 and 1)
        # Update remainingSpace and numItems
     
      if self.head == None:
        self.head = None
      elif self.head.next == None:
        self.head = None
        self.numItems -= 1
        self.remainingSpace = self.maxSize
      else:
        self.numItems -= 1
        self.remainingSpace += self.head.value.size
        self.head = self.head.next 

    def lruEvict(self):
        # Remove the last item of teh CacheList (using iteration to get there) (need special cases for legnth 0 and 1)
        # Update remaningSpace and numItem
      if self.head == None:
        self.head = None
      elif self.head.next == None:
        self.head = None
        self.numItems -= 1
        self.remainingSpace = self.maxSize
      else:
        current = self.head
        while current.next.next != None:
          current = current.next
        self.numItems -= 1
        self.remainingSpace += current.next.value.size
        current.next = None
        
    
    def clear(self):
      self.head = None
      self.remainingSpace = self.maxSize
      self.numItems = 0
      return 'Cleared cache!'
        # YOUR CODE STARTS HERE
        
        #self.head = None -> not recomment
        #Delink every Node in the CacheList
        #Set self.head to None
        #Update remainingSpace and numItems
        #OR, invoke mruEvict or lruEvict utnil CahceList is empty


class Cache:

    def __init__(self):
        self.hierarchy = [CacheList(200), CacheList(200), CacheList(200)]
        self.size = 3
    
    def __str__(self):
        return ('L1 CACHE:\n{}\nL2 CACHE:\n{}\nL3 CACHE:\n{}\n'.format(self.hierarchy[0], self.hierarchy[1], self.hierarchy[2]))
    
    __repr__=__str__


    def clear(self):
        for item in self.hierarchy:
            item.clear()
        return 'Cache cleared!'

    
    def insert(self, content, evictionPolicy):
      lstindex = hash(content)
      lst = self.hierarchy[lstindex]
      if lst.put(content,evictionPolicy) == f"INSERTED: {content}":
        return f'INSERTED: {content}'

      elif lst.put(content,evictionPolicy) == f'Content {content.cid} already in cache, insertion not allowed':
        return f'Content {content.cid} already in cache, insertion not allowed'
        
      else:
        return "Insertion not allowed"
      
      
        # YOUR CODE STARTS HERE
        # Invoke the hash function on the content to determine which CacheList to insert into
        # Call put on the appropriate CacheList, passing in the content and the evictionPolicy

    def __getitem__(self, content):
      for item in self.hierarchy:
        if item.__contains__(content.cid):
          return content
      return 'Cache miss!'
          
        # YOUR CODE STARTS HERE
        # Invoke the hash function on the content to determine which CacheList to check.
        # Call the in operator on this CacheList and if it returns tru, teturn the item at the head


    def updateContent(self, content):
        # YOUR CODE STARTS HERE
        #invoke the hash function on the content to determine which CacheList to update form
        #call update on the appropriate CacheList, passing in the content and the evictionPolicy
      for item in self.hierarchy:
        if item.__contains__(content.cid):
          return item.update(content.cid, content)

   