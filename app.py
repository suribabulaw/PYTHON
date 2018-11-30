#class Employee(id,cm_me):
class Employee():
    comp_name = 'justAgile'
    comp_id = 8008143721
#//////////////////////////////////////////////////////
#========================================
    # Employee.comp_name = id
    # Employee.comp_id = cm_me

    @staticmethod
    def display(id,name):
        add = Employee.comp_name,name
        str1 = Employee.comp_id,+91,id
        return add,str1


result = Employee.display(20,"suri")
print(result)
print(type(result))