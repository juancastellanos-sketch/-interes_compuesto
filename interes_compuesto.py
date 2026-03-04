print("--------bienvenido-------")

print()
print()
print("------------------------------------")
prnt("------dijite su capital-----")
print("------------------------------------")
c= float(input("dijite su capital"))

x= c *  2
n=0

while c < x:
    c= c * 1.05
    n= n+1

print(" su capital se ha duplicado en" , n,"meses")
print("su capital final es de" , c)