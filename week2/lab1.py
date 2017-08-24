def proc1(p):
	p[0] = p[1]

def proc2(p):
	p = p + [1]

def proc3(p):
	q = p
	p.append(3)
	q.pop()

def proc4(p):
	q = []
	while p:
		q.append(p.pop())
	while q:
		p.append(q.pop())


p = [1,0,1]
p[0] = p[0] + p[1] # p[0] = 1 p[1] = 0
p[1] = p[0] + p[2] # p[0] = 1 p[2] = 1
p[2] = p[0] + p[1] # p[0] = 1 p[1] = 2

# print (p) # 1,2,3


# Define a procedure, total_enrollment,
# that takes as an input a list of elements,
# where each element is a list containing
# three elements: a university name,
# the total number of students enrolled,
# and the annual tuition fees.

# The procedure should return two numbers,
# not a string, 
# giving the total number of students
# enrolled at all of the universities
# in the list, and the total tuition fees
# (which is the sum of the number
# of students enrolled times the
# tuition fees for each university).

udacious_univs = [['Udacity',90000,0]]

usa_univs = [ ['California Institute of Technology',2175,37704],
              ['Harvard',19627,39849],
              ['Massachusetts Institute of Technology',10566,40732],
              ['Princeton',7802,37000],
              ['Rice',5879,35551],
              ['Stanford',19535,40569],
              ['Yale',11701,40500]  ]

def total_enrollment(univs):
	num_students = 0
	total_tuition = 0

	for univ in univs:
		univ_students = univ[1]
		univ_tuition = univ[2]

		num_students = univ_students
		total_tuition = total_tuition + (univ_tuition * univ_students)

	return num_students, total_tuition
	
def greatest(list_of_numbers):
    
