
''' Write a python program to store first year percentage of students in an array.                   
Write function for sorting array of floating point numbers in ascending order using:
 a) Selection Sort
 b) Bubble Sort and display top five scores'''


marks=[]
n = int(input("Enter number of students whose marks are to be displayed : "))
print("Enter marks for",n,"students : ")
for i in range(0, n):
	e= int(input())
	marks.append(e) 

print("The marks of",n,"students are : ")
print(marks)

def selection():
	for i in range(len(marks)):
		min_idx = i
		for j in range(i + 1, len(marks)):
			if marks[min_idx] > marks[j]:
				min_idx = j
		(marks[i], marks[min_idx] )= (marks[min_idx], marks[i])
	print("Marks of students after performing Selection Sort on the list : ")
	for i in range(len(marks)):
		print(marks[i])

def bubble():
	n = len(marks)
	for i in range(n - 1):
		for j in range(0, n - i - 1):
			if marks[j] > marks[j + 1]:
				marks[j], marks[j + 1] = marks[j + 1], marks[j]
	print("Marks of students after performing Bubble Sort on the list :")
	for i in range(len(marks)):
		print(marks[i])	

def tfive():
	print("Top five Marks are : ")
	print(marks[n-1],marks[n-2],marks[n-3],marks[n-4],marks[n-5],)
	
		
main=1;
while main==1:
	
	print("1. Selection Sort of the marks")
	print("2. Bubble Sort of the marks")
	print("3. top 5 marks")
	print("4.exit")
	ch=int(input("\n\nEnter your choice: "))
	if ch==1:
		selection()
	
	elif ch==2:
		bubble()
	elif ch==3:
		tfive()
	elif ch==4:
		print("\nThanks for ")
		main=0
	else:
		print("\nEnter a valid choice!!")
"""output
TEST CASES
1)20 30 10 5 62 81 9 
Enter number of students whose marks are to be displayed : 7
Enter marks for 7 students : 
20
30
10
5
62
81
9
The marks of 7 students are : 
[20, 30, 10, 5, 62, 81, 9]
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 1
Marks of students after performing Selection Sort on the list : 
5
9
10
20
30
62
81
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 2
Marks of students after performing Bubble Sort on the list :
5
9
10
20
30
62
81
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 3
Top five Marks are : 
81 62 30 20 10
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 4

Thanks for



2)5 7 8 15 20 56 67 10 

Enter number of students whose marks are to be displayed : 8
Enter marks for 8 students : 
5
7
8
15
20
56
67
10
The marks of 8 students are : 
[5, 7, 8, 15, 20, 56, 67, 10]
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 1
Marks of students after performing Selection Sort on the list : 
5
7
8
10
15
20
56
67
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 2
Marks of students after performing Bubble Sort on the list :
5
7
8
10
15
20
56
67
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 3
Top five Marks are : 
67 56 20 15 10
1. Selection Sort of the marks
2. Bubble Sort of the marks
3. top 5 marks
4.exit


Enter your choice: 4

Thanks for 
 




"""

