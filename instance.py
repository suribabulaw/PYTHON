class Inst:
    static_variable_name  = 'justAgile'
    static_variable_contact =8008143721

    @staticmethod
    def static_method():
        ref_name = Inst.static_variable_contact
        ref_contact = Inst.static_variable_name
        return ref_name , ref_contact

    def static_method2(a,b):
        value = a+ True
        mast_2 = b+ False
        return value,mast_2
# True value  = 1
#false value  = 0


result = Inst.static_method()
print(result)
print(Inst.static_method())
#/////////////////
#with parameter

print(Inst.static_method2(20,10))
############
######################
globale_= Inst.static_method2(50,30)
print(globale_)



