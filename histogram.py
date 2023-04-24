# histogram generator
# write me code to generate a histogram (a textual vertical representation of data) from a given list of integers
#
# example:
# histogram([1,2,3,4])
# 1: *
# 2: **

# def histogram(list):
#     for i in list:
#         print(i,":","*"*i)

# histogram([1,2,3,4, 10])


#q: what python library would you use to generate a histogram
#A: matplotlib

#q: what python library would you use to generate a bar chart
#A: matplotlib

#write me histogram generator using matplotlib
import matplotlib.pyplot as plt

def histogram(list):
    plt.bar(range(len(list)), list)
    plt.show()

histogram([1,2,3,4,10])


#q: how to fix this error : ModuleNotFoundError: No module named 'matplotlib' on a mac
#A: pip3 install matplotlib

