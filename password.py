import random
import string

length=int(input("enter password length:"))
password=string.ascii_letters+string.digits+string.punctuation
p=random.sample(password,length)
print(f"------->>>>>>>>>> genreated password: {''.join(p)}")

    

