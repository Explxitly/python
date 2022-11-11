import time

from person import Person

# fileref = open("smallData.csv", "r")  # r is for read
# fileref = open("mediumData.csv","r") # r is for read
fileref = open("largeData.csv","r") # r is for read

lines = fileref.readlines()

first_name = ''
last_name = ''
street = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    last_name, first_name, street, city, state, postcode = line.strip().split(', ')
    person = Person(last_name.strip(), first_name.strip(), street, city, state, postcode)
    people.append(person)


def linearSearch(people, searchString):
    for i in range(len(people)):
        if people[i].last_name == searchString:
            return print(people[i])
    return -1


#linearSearch(people, 'Pezzini')


# data must be sorted by attribute being searched for
# if not found returns last item in list-this is a bug
def binarySearch(people, searchString):
    first = 0
    last = len(people) - 1
    index = -1
    while (first <= last) and (index == -1):
        mid = (first + last) // 2
        if people[mid].last_name == searchString:
            index = mid
        elif searchString < people[mid].last_name:
            last = mid - 1
        else:
            first = mid + 1

    return people[index]


#print(binarySearch(people, 'Jamie'))


def pythonSearch(people, searchString):
    for person in people:
        if searchString == person.last_name:
            return person
    return -1


# print(pythonSearch(people, 'Frank'))

# for person in people:
#    print(person)

def FibonacciSearch(people, searchString):
    fibM_minus_2 = 0
    fibM_minus_1 = 1
    fibM = fibM_minus_1 + fibM_minus_2
    while fibM < len(people):
        fibM_minus_2 = fibM_minus_1
        fibM_minus_1 = fibM
        fibM = fibM_minus_1 + fibM_minus_2
    index = -1;
    while (fibM > 1):
        i = min(index + fibM_minus_2, (len(people) - 1))
        if (people[i].last_name < searchString):
            fibM = fibM_minus_1
            fibM_minus_1 = fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
            index = i
        elif (people[i].last_name > searchString):
            fibM = fibM_minus_2
            fibM_minus_1 = fibM_minus_1 - fibM_minus_2
            fibM_minus_2 = fibM - fibM_minus_1
        else:
            return people[i]
    if(fibM_minus_1 and index < (len(people)-1) and people[index+1].last_name == searchString):
        return index+1;
    return -1


start = time.perf_counter()
print(FibonacciSearch(people, 'Rizzo'))
end = time.perf_counter()
FibonacciSearch_time = end - start

start = time.perf_counter()
print(pythonSearch(people, 'Rizzo'))
end = time.perf_counter()
pythonSearch_time = end - start

sortedPeople = sorted(people, key=lambda x: x.last_name);
start = time.perf_counter()
print(binarySearch(sortedPeople, 'Rizzo'))
end = time.perf_counter()
binarySearch_time = end - start

start = time.perf_counter()
print(linearSearch(people, 'Rizzo'))
end = time.perf_counter()
linearSearch_time = end - start

print("\n")




times = {
    "Fibonacci Search": FibonacciSearch_time,
    "Python Search": pythonSearch_time,
    "Binary Search": binarySearch_time,
    "Linear Search": linearSearch_time
}

times = dict(sorted(times.items(), key=lambda item: item[1]))

for k, v in times.items():
    print(k, ':', v)