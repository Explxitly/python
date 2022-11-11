import time

from person import Person

with open("largeData.dat") as f:
    lines = f.readlines()

print(lines)

last_name = ''
first_name = ''
address = ''
city = ''
state = ''
postcode = ''
people = []

for line in lines:
    if ',' in line:
        last_name, first_name = line.strip().split(', ')
        continue
    elif line[0].isdigit():
        address = line.strip()
        continue
    else:
        my_list = (line.strip().split('\t'))
        if len(my_list) > 1:
            # print(my_list)
            city, state, postcode = my_list
            continue
    person = Person(last_name, first_name, address, city, state, postcode)
    people.append(person)


# for person in people:
#     print(person)

def bubbleSort(people):
    n = len(people)
    # Traverse through all peopleay elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            # traverse the peopleay from0ton-i-1
            # Swap if the element found is greater
            # than the next element
            if people[j].last_name > people[j + 1].last_name:
                people[j], people[j + 1] = people[j + 1], people[j]


bubbleSort(people)
for person in people:
    print(person)


def mergeSort(people):
    if len(people) > 1:

        # Finding the mid of the peopleay
        mid = len(people) // 2

        # Dividing the peopleay elements
        L = people[:mid]

        # into 2 halves
        R = people[mid:]

        # Sorting the first half
        mergeSort(L)

        # Sorting the second half
        mergeSort(R)

        i = j = k = 0

        # Copy data to temp peopleays L[] and R[]
        while i < len(L) and j < len(R):
            if L[i].first_name < R[j].first_name:
                people[k] = L[i]
                i += 1
            else:
                people[k] = R[j]
                j += 1
            k += 1

        # Checking if any element was left
        while i < len(L):
            people[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            people[k] = R[j]
            j += 1
            k += 1


print("\n")
mergeSort(people)
for person in people:
    print(person)


# Function to find the partition position
def partition(people, low, high):
    # Choose the rightmost element as pivot
    pivot = people[high]

    # Pointer for greater element
    i = low - 1

    # Traverse through all elements
    # compare each element with pivot
    for j in range(low, high):
        if people[j].last_name <= pivot.last_name:
            # If element smaller than pivot is found
            # swap it with the greater element pointed by i
            i = i + 1

            # Swapping element at i with element at j
            (people[i], people[j]) = (people[j], people[i])

    # Swap the pivot element with the greater element specified by i
    (people[i + 1], people[high]) = (people[high], people[i + 1])

    # Return the position from where partition is done
    return i + 1


low = 0
high = len(people) - 1


# Function to perform quicksort
def quick_sort(people, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(people, low, high)

        # Recursive call on the left of pivot
        quick_sort(people, low, pi - 1)

        # Recursive call on the right of pivot
        quick_sort(people, pi + 1, high)


print("\n")
quick_sort(people, low, high)
for person in people:
    print(person)


def pythonSort(people):
    # some data had lowercase names which affects sorting
    people.sort(key=lambda person: person.first_name.upper(), reverse=False)


print("\n")
pythonSort(people)
for person in people:
    print(person)

start = time.perf_counter()
bubbleSort(people)
end = time.perf_counter()
bubble_sort_time = end - start

start = time.perf_counter()
mergeSort(people)
end = time.perf_counter()
merge_sort_time = end - start

start = time.perf_counter()
quick_sort(people, low, high)
end = time.perf_counter()
quick_sort_time = end - start

start = time.perf_counter()
pythonSort(people)
end = time.perf_counter()
python_sort_time = end - start

print("\n")

times = {
    "Bubble Sort": bubble_sort_time,
    "Merge Sort": merge_sort_time,
    "Quick Sort": quick_sort_time,
    "Python Sort": python_sort_time
}

times = dict(sorted(times.items(), key=lambda item: item[1]))

for k, v in times.items():
    print(k, ':', v)

with open('people.csv', 'w') as f:
    for person in people:
        # print(person)
        f.write(str(person) + '\n')
