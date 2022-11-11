people_dict = {}
for person in people:
    people_dict[hash(person)] = person

for k, v in people_dict.items():
    #print key:value
    print(k, ':', v)