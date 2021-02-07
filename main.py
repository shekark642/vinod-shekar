#gets imports
class bcolors:
  HEADER = '\033[95m'
  OKBLUE = '\033[94m'
  OKGREEN = '\033[92m'
  WARNING = '\033[93m'
  FAIL = '\033[91m'
  ENDC = '\033[0m'
  BOLD = '\033[1m'
  UNDERLINE = '\033[4m'
import math

#gets the input for the dataset
print(bcolors.OKBLUE+bcolors.BOLD+"Enter a list elements separated by space: "+bcolors.ENDC)
usernumberlistinput1 = input("")
print(bcolors.OKBLUE+bcolors.BOLD+"Enter a second list elements separated by space: "+bcolors.ENDC)
usernumberlistinput2 = input("")
usernumberlist1 = usernumberlistinput1.split()
usernumberlist2 = usernumberlistinput2.split()

#prints mean and sum for dataset 1
sum1 = 0
for num in usernumberlist1:
    sum1 += int(num)
print("")
print("sum of first list = ", sum1)
listmean1=float(sum1)/len(usernumberlist1)
print("mean of first list = ", listmean1)

#prints mean and sum for dataset 2
sum2 = 0
for num in usernumberlist2:
    sum2 += int(num)
print("sum of second list = ", sum2)
listmean2=float(sum2)/len(usernumberlist2)
print("mean of second list = ", listmean2)

#uses formula to find the sigma of the 2 datasets (numerator)
sumnumberstart=[]
xnumberinlist2=0
for x in (usernumberlist1):
  samplemeanlist= ((float(x)-float(listmean1)) * (float(usernumberlist2[int(xnumberinlist2)])-float(listmean2)))
  sumnumberstart.append(samplemeanlist)
  samplemeanlist=0
  xnumberinlist2=(xnumberinlist2+1)

numerator=(float(sum(sumnumberstart)))
print("")
print("numerator = ", numerator)


#gets first and second half of the denominator to simplify code
firstlist=[]
for x in (usernumberlist1):
  numberfirstlist= ((float(x)-float(listmean1))**2)
  firstlist.append(numberfirstlist)
  numberfirstlist=0

secondlist=[]
for x in (usernumberlist2):
  numbersecondlist= ((float(x)-float(listmean2))**2)
  secondlist.append(numbersecondlist)
  numbersecondlist=0

#uses formula to get the square root of the sigma in denominator
denominatorbeforesqrt=(float(sum(firstlist)))*(float(sum(secondlist)))
denominator=math.sqrt(denominatorbeforesqrt)
print("denominator = ", denominator)
answer = ((float(numerator))/(float(denominator)))
print("")
print(bcolors.OKGREEN+bcolors.BOLD+"correlation coefficient = ", answer)
