import hashlib

correct_pw_hash = open('level5.hash.bin', 'rb').read()
dictionary = open('dictionary.txt', 'r')

def hash_pw(pw_str):
    pw_bytes = bytearray()
    pw_bytes.extend(pw_str.encode())
    m = hashlib.md5()
    m.update(pw_bytes)
    return m.digest()

def level_3_pw_check():
    for user_pw in dictionary_array:
        user_pw_hash = hash_pw(user_pw)
        
        if( user_pw_hash == correct_pw_hash ):
            print(user_pw)
            
            return
    print("That password is incorrect")

dictionary_array = []
for line in dictionary:
    dictionary_array.append(line.strip())




    
level_3_pw_check()
