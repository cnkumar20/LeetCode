class Solution:

    def __init__(self,input):
        self.number_array = list(input)

    def __selectionSort(self):
        for i in range(len(self.number_array)):
            min = self.number_array[i]
            for j in range(i,len(self.number_array)):
                min = min if(min < self.number_array[j]) else self.number_array[j]
                if(min != self.number_array[i]):
                    self.number_array[j] = self.number_array[i]
                    self.number_array[i] = min
    def sort_and_print(self):
        self.__selectionSort()
        print(self.number_array)

a = Solution([3,5,2,5,1,7,3,43,1])
a.sort_and_print()