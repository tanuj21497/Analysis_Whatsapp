from matplotlib import pyplot as plt
import numpy as np
from math import e, pi

msg = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]
sum =0
sq_sum =0
mean =0
mean_list  = []
var_list=[]
sum_list = []

adder = 0;

for t in range(30):
    adder+= msg[t]
    sum_list.append(adder)
j=0
var =0
var_list.append(0);

for i in msg:
    j+=1
    sum+=i
    sq_sum +=(i**2)
    mean = sum/j

    mean_list.append( sum/j)

j=0
for i in range(1, len(msg)):
    for k in range(i+1):
        var += (msg[k]-mean_list[i])**2
    var_list.append(var/(i))
    var=0

def exponential(x, var):

    lam = 1/(var**0.5)

    return lam *(e**(-1 * lam *x))

def gaussian(x, mean, var):
    d = 1/((2 *pi *var)**0.5)
    power = -1 *((x-mean)**2)/(2*var)

    return d*(e**power)


exponential_list =[]
gaussian_list =[]
# ********************************************************
inp = 30
print(mean_list[inp-1])
print(var_list[inp-1])

dif = 6
# ********************************************************

head = 0
tail = dif
gap_identifier =[]
gap =0
h =0
u=0

upper = (sum_list[-1] %5) +sum_list[-1] +5

while(u< upper and h<30):
    if sum_list[h]>=head and sum_list[h]< tail:
        gap+=1
        h+=1
        u+=1
        continue

    gap_identifier.append(gap)
    gap=0
    head+=dif
    tail+=dif

gap_identifier.append(gap)

new_gap_identifier = []

for item in gap_identifier:
    new_gap_identifier.append((item)/30)


last_x_axis = []

for ite in range(1, len(gap_identifier)+1):
    last_x_axis.append(ite * dif)

for k in range(inp):
    exponential_list.append(exponential(msg[k], var_list[inp-1]))
    gaussian_list.append(gaussian(msg[k],mean_list[inp-1], var_list[inp-1]))


plt.plot(msg, exponential_list, color = "black")
plt.title("Exponential PDF")
plt.show()

plt.plot(msg, gaussian_list, color = "black")
plt.title("Normal PDF")
plt.show()

plt.plot(last_x_axis,new_gap_identifier, color = "black")
plt.title("Frequency")
plt.show()
