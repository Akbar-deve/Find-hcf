#defining a function find_hcf with x and y parameter

def find_hcf(x,y):
    #check which one is smaller then take it in smaller variable 
    if x>y: smaller =y
    else: smaller =x
    #Itterat over smaller varaiable 
    for i in range(1,smaller+1):
        if x%i==0 and y%i==0:
            hcf=i
    #you can return the hcf value to the funcgtion where it is called or you can print inside the function 
    print(f'hcf of n1= {x} and n2 = {y} is = {hcf}')
#declearing inputs 
n1=int(input("enter n1 value--> "))
n2=int(input("enter n2 value--> "))
#function calling 
find_hcf(n1,n2)
