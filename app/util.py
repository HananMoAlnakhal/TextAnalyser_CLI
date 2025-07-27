class CircularDoubledList:
    class Node:
        def __init__(self,val,next=None,prev=None):
            self.v=val
            self.next=next
            self.prev=prev

    def __init__(self):
        self._tail=None
        self._head=None
        self._size=0

    def enqueue(self,e):
        newest=self.Node(e)
        if self._size==0:
            newest.next=newest
            newest.prev=newest
            self._head=newest
            self._tail=newest
        else:
            newest.next=self._head
            newest.prev=self._tail
            self._tail.next=newest
        self._tail = newest
        self._head.prev=self._tail
        self._size+=1

    def enQ_LIST(self,LIST):
        for item in LIST:
            self.enqueue(item)
        return self

    def GetColor(self,reverse=False):
        val=self._tail.v if not reverse else None
        self.__rotate(reverse)
        if reverse:val=self._tail.v
        return val
    
    def __rotate(self,r=False):
        if r:
            self._tail = self._tail.next    
        else:
            self._tail = self._tail.prev