

import hashlib

def hashmd5_1():
    s = "monkey"

    hash = hashlib.md5(s.encode())
    hashmd5 = hash.hexdigest()
    print(hashmd5)



def hashmd5_2():
    s = "monkey"

    hash = hashlib.md5()
    hash.update(s.encode())
    hashmd5 = hash.hexdigest()
    print(hashmd5)




if __name__ == '__main__':
    # echo -n monkey | md5sum
    hashmd5_1()
    hashmd5_2()