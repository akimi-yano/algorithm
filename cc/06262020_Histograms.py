# https://statistics.laerd.com/statistical-guides/understanding-histograms.php
# Make a Histograms

# lower bound 20
# upper bound 100
# num of bins - 8
# 36	25	38	46	55	68	72	55	36	38
# 67	45	22	48	91	46	52	61	58	55
# [ 0, 0, 0, 0, 0, 0, 0,  0]
# [30,40,50,60,70,80,90,100]
# (upper-lower)/num_bins
# (100-20)/8 = 10 in each

# class Histogram:
#     def __init__(self,num_bins,lower,upper):
#         self.bins = [0]*num_bins
#         num_each = (upper-lower)//num_bins
#         self.limits = []
#         for i in range(lower+num_each,upper+1,num_each):
#             self.limits.append(i)
#         print("Histgram initialized: ", self.bins)
#         print("Limits initialized: ", self.limits)
        
#     def count(self,val):
#         def search_category(val):
#             low = 0
#             high = len(self.limits)-1
#             while low<=high:
#                 mid = (low+high)//2
#                 if self.limits[mid]==val:
#                     return mid
#                 elif self.limits[mid]>val:
#                     high=mid-1
#                 else:
#                     low=mid+1
#             return low
#         index=search_category(val)
#         self.bins[index]+=1
#     def print_hist(self):
#         print("Histgram updated: ", self.bins)
#         # print("Limits used: ",self.limits)
# my_hist = Histogram(8,20,100)
# new_data = [36,25,38,46,55,68,72,55,36,38,67,45,22,48,91,46,52,61,58,55]
# for data in new_data:
#     my_hist.count(data)
# my_hist.print_hist()


# test_data = [30,40,50,60,70,80,90,100]
# def test_search_category(val):
#     low = 0
#     high = len(test_data)-1
#     while low<=high:
#         mid = (low+high)//2
#         if test_data[mid]==val:
#             return mid
#         elif test_data[mid]>val:
#             high=mid-1
#         else:
#             low=mid+1
#     return low
# print(test_search_category(45))
# print(test_search_category(20))
# print(test_search_category(30))
# print(test_search_category(31))
# print(test_search_category(40))
# print(test_search_category(50))
# print(test_search_category(68))
# print(test_search_category(88))
# print(test_search_category(46))
# print(test_search_category(38))
# print(test_search_category(87))



# OPTIMIZATION!!! if you know the lower bound and num each, can find the index at O(1)
# cannot put 100 upper bound is exclusive 
class Histogram:
    def __init__(self,num_bins,lower,upper):
        self.bins = [0]*num_bins
        self.num_each = (upper-lower)//num_bins
        self.lower = lower
            
    def count(self,val):
        index = (val - self.lower)//self.num_each 
        self.bins[index]+=1
    def print_hist(self):
        print("Histgram Updated: ", self.bins)

my_hist = Histogram(8,20,100)
new_data = [36,25,38,46,55,68,72,55,36,38,67,45,22,48,91,46,52,61,58,55]
for data in new_data:
    my_hist.count(data)
my_hist.print_hist()
