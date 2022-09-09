	
my_name = "joseph"
my_pass = "j@78se1"
ent_name = input("Please enter your name: ")
n = ent_name.lower()
if my_name == n:
    print(f"Hello, '{ent_name}!' The password is : '{my_pass}'")
elif my_name != n:
    print(f"Hello, '{ent_name}!' See you later.")