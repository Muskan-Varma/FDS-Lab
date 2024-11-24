
"""write a python program to store second year percentage of students in array . Write function for sorting array of floating point numbers in ascending order using 
1)Insertion sort
2)Shell sort and display top five scores """

a1=[]
n=int(input("ENTER NUMBER OF STUDENTS\t"))
print("ENTER PERCANTAGE OF STUDENTS")
for i in range(n):
	a1.append(float(input()))
print("LIST BEFORE SORTING\n",a1)

def isort(arr):#FOR INSERTIONSORT
	for i in range(1, len(arr)):
		key=arr[i]
		j = i-1
		while j >=0 and key < arr[j] :
			arr[j+1] = arr[j]
			j -= 1
		arr[j+1] = key


def ssort(arr):#FOR SHELL SORT
	gap=n//2
	while gap>0:
		j=gap
		while j<n:
			i=j-gap 
			while i>=0:
				if arr[i+gap]>arr[i]:
					break
				else:
					arr[i+gap],arr[i]=arr[i],arr[i+gap]
				i=i-gap 
			j+=1
		gap=gap//2

		
def pprint(a):#FOR PRINTING TO 5 SCORES
	
	print("\nTOP 5 SCORES ARE")
	g=len(a)
	
	print("\n",a[g-1],"\n",a[g-2],"\n",a[g-3],"\n",a[g-4],"\n",a[g-5])

	
		


main=1;
while main==1:#MENU
	print("1.INSERTION SORT\n2.SHELL SORT\n3.TOP FIVE MARKS\n4.EXIT\n")
	ch=int(input("ENTER YOUR CHOICE\t"))
	
	if ch==1:
		b=[]
		print("LIST AFTER USING INSERTION SORT\n")
		isort(a1)
		b.append(a1)
		print(b)	
	elif ch==2:
		c=[]
		print("LIST AFTER USING SHELL SORT\n")
		ssort(a1)
		c.append(a1)
		print(c)
	elif ch==3:
		pprint(a1)
	elif ch==4:
		print("THANK YOU")
		break;
	else:
		print("YOU ENTERED WRONG CHOICE")





"""output
TEST CASES
1)20 30 10 5 62 81 9 
ENTER NUMBER OF STUDENTS	7 
ENTER PERCANTAGE OF STUDENTS
20.0
30.0
10.0
5.0
62.0
81.0
9.0
LIST BEFORE SORTING
 [20.0, 30.0, 10.0, 5.0, 62.0, 81.0, 9.0]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	1
LIST AFTER USING INSERTION SORT

[[5.0, 9.0, 10.0, 20.0, 30.0, 62.0, 81.0]]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	2
LIST AFTER USING SHELL SORT

[[5.0, 9.0, 10.0, 20.0, 30.0, 62.0, 81.0]]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	3

TOP 5 SCORES ARE
81.0 
 62.0 
 30.0 
 20.0 
 10.0
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	4
THANK YOU



2)5 7 8 1 20 56 67 10 
ENTER NUMBER OF STUDENTS	8
ENTER PERCANTAGE OF STUDENTS
5.0
7.0
8.0
15.0
20.0
56.0
67.0
10.0
LIST BEFORE SORTING
 [5.0, 7.0, 8.0, 15.0, 20.0, 56.0, 67.0, 10.0]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	1
LIST AFTER USING INSERTION SORT

[[5.0, 7.0, 8.0, 10.0, 15.0, 20.0, 56.0, 67.0]]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	2
LIST AFTER USING SHELL SORT

[[5.0, 7.0, 8.0, 10.0, 15.0, 20.0, 56.0, 67.0]]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	3

TOP 5 SCORES ARE

 67.0 
 56.0 
 20.0 
 15.0 
 10.0
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	4
THANK YOU


3)78 34 78 20 34 67 20 20 78 21 22 
ENTER NUMBER OF STUDENTS	11
ENTER PERCANTAGE OF STUDENTS
78.0
34.0
78.0
20.0
34.0
67.0
20.0
20.0
78.0
21.0
22.0
LIST BEFORE SORTING
 [78.0, 34.0, 78.0, 20.0, 34.0, 67.0, 20.0, 20.0, 78.0, 21.0, 22.0]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	1
LIST AFTER USING INSERTION SORT

[[20.0, 20.0, 20.0, 21.0, 22.0, 34.0, 34.0, 67.0, 78.0, 78.0, 78.0]]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	2
LIST AFTER USING SHELL SORT

[[20.0, 20.0, 20.0, 21.0, 22.0, 34.0, 34.0, 67.0, 78.0, 78.0, 78.0]]
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	3

TOP 5 SCORES ARE

 78.0 
 78.0 
 78.0 
 67.0 
 34.0
1.INSERTION SORT
2.SHELL SORT
3.TOP FIVE MARKS
4.EXIT

ENTER YOUR CHOICE	4
THANK YOU


"""




	
