import sys


fd = open('mgt.log', 'a+')
sys.stdout = fd


# str(datetime.datetime.now()) + sys.stdout = fd


print("add user")
print("delete user")






fd.close()