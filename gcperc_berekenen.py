test = "cgatcgatgctagctgacgatgtggtaggcttgactgcg"
print(test.count("a"))
print(test.count("t"))
print(test.count("c"))
print(test.count("g"))

print (test.count("g")+ (test.count("c")))

print (test.count("c")+ (test.count("g") / (test.count("a")+ (test.count("t")+ (test.count("c")+ (test.count("g")))))))