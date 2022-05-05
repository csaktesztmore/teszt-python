"""tanulo = ["irodalom", 2, "történelem", 3, "matek", 4, "nyelvtan", 5, "fizika", 5]

jegyek = []


for i in range(0 len(tanulo),2):
    jegy = int(tanulo[i + 1])
    jegyek.append(jegy)
    print(tanulo[i], end = ": ")
    for j in range(jegy):
        print("*", end = "")
    print()"""



#akasztófa
"""puzzle = "tojás"
my_solution = "*****"
life = 10
correct_letters = []
incorrect_letters = []

while life > 0 and puzzle != my_solution:
    print(my_solution)
    tipp = input("Tippelj egy betűt: ")
    if len(tipp) == len(puzzle):
        temp = my_solution
        my_solution = tipp
        print("Éppen megpróbálod kitalálni a megoldást")
        if my_solution == puzzle:
            print("Helyes!")
        else:
            print("Helytelen!")
            life -= 1
            print(str(life) + "Életed maradt!")
            my_solution = temp

    else:
        found = False
        for i in range(len(puzzle)):
            if puzzle[i] == tipp:
                my_solution_list = list(my_solution)
                my_solution_list[i] = tipp
                my_solution = "".join(my_solution_list)
                found = True
        if not found:
            incorrect_letters.append(tipp)
            life -= 1
            print("helytelen! " + str(life) + " életed maradt!")
        else:
            correct_letters.append(tipp)
            print("A jó betűk listája: " + str(correct_letters))
            print("A rossz betűk listája: " + str(incorrect_letters))

if life > 0:
        print("Gratulálok")
else:
    print("ez most nem jött össze:(")"""


#prímtényezős felbontás
num = int(input("kérek egy számot: "))
i = 2
prim_osztok = []

while num > 1:
    while num % i == 0:
        num /= i
        prim_osztok.append(i)
    i += 1

print(prim_osztok)
        




