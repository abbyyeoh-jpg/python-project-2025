beatles= []
print("Step 1:", beatles)

beatles.append("John_Lennon")
beatles.append("Paul_McCartney")
beatles.append("George_Harrison")
print("Step 2:", beatles)

for i in range (2):
    name= input("enter name:")
    beatles.append(name)
print("Step 3:", beatles)

del beatles[-1]
del beatles [-1]
print("Step 4:", beatles)

beatles.insert(0,"Ringo_Starr")
print("Step 5:", beatles)

print("The Fab", len(beatles))
