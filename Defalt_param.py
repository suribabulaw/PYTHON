def sample(id,name,contact):
    com_name = name
    com_contact = contact
    com_id = name
    return com_name,com_id,com_id

result = sample(10,'suri',8008143721)
print(result)


################################################
#######################################################
def sample11(id,name,contact):
     com_name = name
     com_id  = id
     com_contact = contact
     return com_id,com_name,com_contact
print(sample11(101,"suri",8008143721))


########################################################
######DEFAULT prameter

def sample2(id=1,name=None,contact=''):
    cm_id = id
    cm_name =name , "suri"
    cm_contact = contact
    return cm_id,cm_contact,cm_name

print(sample2())
print(sample2(20))
print(type(sample2(20,"suri",8008143721)))

#####################
################################
# def sample3(*id,name='',):
#     S_id = id + 1
#     s_name= name , 'GANGAVATH'
#     return S_id ,s_name
#
# # print(sample3(20,"suri",20,50,50,))
# print(sample3(20,"suri",20,50,50))



