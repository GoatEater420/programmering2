
# step 1
beatles = []

print("Step 1:", beatles)
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")

# step 2
morebeatles = ["Stu Sutcliffe", "Pete Best"]

for members in morebeatles:
   beatles.append(members)


print("Step 2:", beatles)
del beatles[3:5]

beatles.insert(0,"ringo starr")
# testing list legth
print("The Fab", len(beatles))

