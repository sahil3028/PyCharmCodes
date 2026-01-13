def average():

    with open("average.txt",'r') as file:
        data=file.readlines()[1:] #the[1:] is slicing the list like its taking from 2nd element coz we nade the first one as string

    values= [int(i)for i in data]

    return sum(values)/ len(values)

print(average())