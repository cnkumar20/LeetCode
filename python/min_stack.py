class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here
        """
        self.minimum = 99999999999999
        self.container = list()
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.container.extend([x])
        if(x < self.minimum):
            self.minimum = x
        
        

    def pop(self):
        """
        :rtype: void
        """
        pop = self.container.pop()
        if(len(self.container)==0):
            self.minimum= 99999999999
            return
        self.minimum = min(self.container)
        

    def top(self):
        """
        :rtype: int
        """
        return self.container[len(self.container)-1]
        
        

    def getMin(self):
        """
        :rtype: int
        """ 
        return self.minimum
      
