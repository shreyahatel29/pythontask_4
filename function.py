# Function Example

# Example 1

def users(user_id,name,dept,salary):
    print(f'user_id = {user_id}')
    print(f'name = {name}')
    print(f'dept = {dept}')
    print(f'salary = {salary}')

    return{
        'user_id':'user_id',
        'name':'name',
        'dept':'dept',
        'salary':'salary'
    }
print()
user1 = (101,'Ankit','Sales',13000)
print(f'user1 = {user1}')
user2 = (102,'Sahil','Finance',20000)
print(f'user2 = {user2}')
user3 = (103,'Ram','HR',21000)
print(f'user3 = {user3}')
print('------')

# Example 2

def student_info(roll_no,name,address,mob_no):
    print(f'roll_no = {roll_no}')
    print(f'name = {name}')
    print(f'address = {address}')
    print(f'mob_no= {mob_no}')
 
    return{
        'roll_no':'roll_no',
        'name':'name',
        'address':'address',
        'mob_no':'mob_no'
    }
print()
stud1 = (1001,'Anmol','Nagpur',987654489)
print(f'stud1 = {stud1}')
stud2 = (1002,'Smith','Sadar',876590443)
print(f'stud2 = {stud2}')
stud3 = (1003,'Tanmay','Dhantoli',9946578321)
print(f'stud3 = {stud3}')
print('-----')