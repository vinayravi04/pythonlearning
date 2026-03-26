#String unpacking

atmpin = "1234"
a,b,c,d=atmpin
print(a,b,c,d)


#String split

name= "Vinay Ravi"
parts = name.split()
firstname = (parts[0])
lastname=parts[1]
print(firstname)
print(lastname)
name="Vinay#####Ravi"
parts = name.split("#")
print(parts)

#String inbuild functions 


nme="vinay ravi"
a=id(nme)
print(a)
print(nme.capitalize())

print(nme.title())
print(id(nme.upper()))
print(f"hijriejfiejr")