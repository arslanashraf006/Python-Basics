#1
country_dic = {
    "China":	143,
"India":	136,
"USA":	32,
"Pakistan":	21,
}

inputs = input("Enter one input value from (print, add, remove, query): ")

if inputs == 'print':
    for k,v in country_dic.items():
        print(k,"==>",v)
elif inputs == 'add':
    enter_country = input("Add country name: ")
    if country_dic.__contains__(enter_country):
        print("country already exist")
    else:
        population = input("enter country population: ")
        num_pop = int(population)
        country_dic[enter_country] = num_pop
        print(country_dic)
elif inputs == 'remove':
    value = input("Enter country you want to remove: ")
    if(country_dic.__contains__(value)):
        del country_dic[value]
        for k,v in country_dic.items():
            print(k,"==>",v)
    else:
        print("country does not exist")
elif inputs == 'query':
    value = input("Enter country name you want to get data: ")
    print(country_dic[value])