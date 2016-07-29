class Solution:

    def __init__(self,input):
        self.number_array = list(input)

    def __selectionSort(self):
            for j in range(1,len(self.number_array)):
                curvalue = self.number_array[j]
                while(j> 0 and curvalue < self.number_array[j-1]):
                    self.number_array[j] = self.number_array[j-1]
                    j -= 1
                self.number_array[j] = curvalue



    def sort_and_print(self):
        self.__selectionSort()
        print(self.number_array)

a = Solution([3,5,2,5,1,7,3,43,1])
a.sort_and_print()