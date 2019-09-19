#bij test voer je de sequentie in

test = "cgatcgatgctagctgacgatgtggtaggcttgactgcg"
# vervolgens print hij de hoeveelheid van elke letter

print(test.count("a"))
print(test.count("t"))
print(test.count("c"))
print(test.count("g"))

#en dan print hij het totaal van de gc en het percentage

print (test.count("g")+ (test.count("c")))

print (test.count("c")+ (test.count("g") / (test.count("a")+ (test.count("t")+ (test.count("c")+ (test.count("g")))))))