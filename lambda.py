
#lambda function
l = lambda x:x > 5
print(l(10));

# using lambda exprestion to filter the values
def alter(values,check):
    return [val for val in values if check(val)]

my_list = [1,2,3,4,5]
another_list = alter(my_list,lambda x:x!=5)
print(another_list)

# using without lambda functions
def alter(values,check):
    return [val for val in values if check(val)]

def check_for_eight(x):
    return x != 8 
new_list = [1,6,3,5,8]
another_list = alter(new_list,check_for_eight)
print(another_list,'eightlist')


# remove a number from a string
def check_for_number(x):
    return [val for val in x if val not in  [str(r) for r in range(10)]]

random_str = 'helll343yaa'
l = alter(random_str,check_for_number);
c=''.join(l)
print(c,'is it')


chatString = 'removeeeees'
letter = alter(chatString,lambda x:x != 'e');
print(''.join(letter),'eeeeeeess')








    