"""Problem statement:- Write a python program to store marks scored in subject "data structure and algorithm" by N students in class .Write a function to compute the following 
1)The average score of class
2)Highest score and lowest score of class
3)Count of student who were absent for the test 
4)Display marks with highest frequency"""
  
  
m=[]
n=int(input("How many students you want to enter\n"))
	
def mrkent():
    
	print("enter the marks of students(enter -1 if absent)")
	for i in range (n):
		m.append(int(input()))   
		

def display():

   print("\nMarks Scored in FDS")
   for i in range(len(m)):
      if(m[i] == -1) :
         print("\tStudent %d : AB"%(i+1))
      else :
         print("\tStudent %d : %d"%(i+1,m[i]))
         
def absent():
    count=0
    for i in range (n):
        if (m[i]==-1):
            count=count+1
    print("total absent students are:-",count)
    on=n-count
    print("total present students:-",on)


def average():
   
   sum = 0
   for i in range(len(m)) :
      if(m[i] != -1) :
         sum = sum + m[i]
   avg = sum / len(m)
   print("\nAverage score of class is %.2f\n\n"%avg)

    
def highlow():
	m1=[]
	m2=[]
	count=0
	for i in range (len(m)):
		if (m[i]==-1):
			count=count+1
	for k in range (len(m)):
		for j in range (len(m)):
			if (m[k]>m[j]):
				temp=m[k]
				m[k]=m[j]
				m[j]=temp
	m1.append(m)
	e=n-count
	for z in range (0,e):
		m2.append(m[z])
	
	print("highest marks obtained",m2[0])
	print("lowest marks obtained",m2[e-1])
	

def freq():
	list=m
	count=0
	num=m[0]
	for i in range(len(m)):
		cf=list.count(i)
		if (cf>count and m[i]!=-1 ):
			
			count=cf
			num=i
	print("Element with highest frequency",num)


mrkent()

#exception()
ma=0
while (ma==0):
	ch=int(input("PRESS\n1.AVERAGE SCORE\n2.HIGHEST AND LOWEST SCORE\n3.COUNT OF STUDENT WHO WERE ABSENT\n4.SCORE THAT OCCURED MOST\n5.DISPLAY\n6.EXIT\n"))
	if (ch==1):
		average()
	elif (ch==2):
		highlow()
	elif (ch==3):
		absent()
	elif (ch==4):
		freq()
	elif (ch==5):
		display()
	else:
		print("THANK YOU")
		break
