class Fashion:
    company_name ='justAgile'
    Company_contact = 8008143721
    @staticmethod
    def display():
        name = Fashion.company_name
        contact = Fashion.Company_contact

        return name,  contact


result = Fashion.display()
print(result,'suri',"nithesh")
print(type(result))
