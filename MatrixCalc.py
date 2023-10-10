#Input Numbers
first = int(input("First Number: "))
second = int(input("second Number: "))
third = int(input("third Number: "))
fourth = int(input("fourth Number: "))
fifth = int(input("fifth Number: "))
sixth = int(input("sixth Number: "))
seventh = int(input("seventh Number: "))
eighth = int(input("eighth Number: "))
nineth = int(input("nineth Number: "))
print(" ")
#matrix List
matrix = [first, second, third,
          fourth, fifth, sixth,
          seventh, eighth, nineth]

#determinant
determinant = first * ((fifth * nineth) - (sixth * eighth)) - second * ((fourth * nineth) - (sixth * seventh)) + third * ((fourth * eighth) - (fifth * seventh))

#Minorz
firstminor = first * ((fifth * nineth) - (sixth * eighth))
secondminor = second * ((fourth * nineth) - (sixth * seventh))
thirdminor = third * ((fourth * eighth) - (fifth * seventh))
fourthminor = fourth * ((second * nineth) - (third * eighth))
fifthminor = fifth * ((first * nineth) - (third * seventh))
sixthminor = sixth * ((first * eighth) - (second * seventh))
seventhminor = seventh * ((second * sixth) - (third * fifth))
eighthminor = eighth * ((first * sixth) - (third * fourth))
ninethminor = nineth * ((first * fifth) - (second * fourth))

#AlgSumz

algSumFirst = (fifth * nineth) - (sixth * eighth)
algSumSecond = ((fourth * nineth) - (sixth * seventh)) * -1 
algSumThird = (fourth * eighth) - (fifth * seventh)
algSumFourth = ((second * nineth) - (third * eighth)) * -1 
algSumFifth = (first * nineth) - (third * seventh)
algSumSixth = ((first * eighth) - (second * seventh)) * -1 
algSumSeventh = (second * sixth) - (third * fifth)
algSumEighth = ((first * sixth) - (third * fourth)) * -1 
algSumNineth = (first * fifth) - (second * fourth)

#Determinat for Inversion
detForInverse = 1 / determinant

#Inverse Each
inversedFirst = algSumFirst * detForInverse
inversedSecond = algSumSecond * detForInverse
inversedThird = algSumThird * detForInverse
inversedFourth = algSumFourth * detForInverse
inversedFifth = algSumFifth * detForInverse
inversedSixth = algSumSixth * detForInverse
inversedSeventh = algSumSeventh * detForInverse
inversedEighth = algSumEighth * detForInverse
inversedNineth = algSumNineth * detForInverse


#Print Matrix

def printMatrix():
    print(" ")
    print("Your Matrix : ")
    print("|[", first, "], ", "[", second, "], ", "[", third, "]|")
    print("|[", fourth, "], ", "[", fifth, "], ", "[", sixth, "]|") 
    print("|[", seventh, "], ", "[", eighth, "], ", "[", nineth, "]|")
    print(" ")

def transposedMatrix():
    print("Your Transposed Matrix : ")
    print("|[", first, "], ", "[", fourth, "], ", "[", seventh, "]|")
    print("|[", second, "], ", "[", fifth, "], ", "[", eighth, "]|") 
    print("|[", third, "], ", "[", sixth, "], ", "[", nineth, "]|")
    print(" ")

#AlgSumMatrix

def printAlgSumMatrix():
    print("Your Matrix in AlgSumz :")
    print("|[", algSumFirst, "], ", "[", algSumSecond, "], ", "[", algSumThird, "]|")
    print("|[", algSumFourth, "], ", "[", algSumFifth, "], ", "[", algSumSixth, "]|") 
    print("|[", algSumSeventh, "], ", "[", algSumEighth, "], ", "[", algSumNineth, "]|")    
    print(" ")

#MinorMatrix

def printMinorMatrix():
    print("Your Matrix in Minors :")
    print("|[", firstminor, "], ", "[", secondminor, "], ", "[", thirdminor, "]|")
    print("|[", fourthminor, "], ", "[", fifthminor, "], ", "[", sixthminor, "]|") 
    print("|[", seventhminor, "], ", "[", eighthminor, "], ", "[", ninethminor, "]|")
    print(" ")

#Fully inverse

def printInversed():
    print("Fully Inversed Matrix : ")
    print("|[", inversedFirst, "], ", "[", inversedFourth, "], ", "[", inversedSeventh, "]|")
    print("|[", inversedSecond, "], ", "[", inversedFifth, "], ", "[", inversedEighth, "]|") 
    print("|[", inversedThird, "], ", "[", inversedSixth, "], ", "[", inversedNineth, "]|")

#Choice
print("1. Print your matrix.")
print("2. Print Transposed Matrix")
print("3. Print your matrix in algsumz.")
print("4. Print your matrix in minors.")
print("5. Print inversed matrix.")
print("6. Print Determinant.")
print("7. Print all of them.")
print(" ")

choiceX = int(input("Your choice (1, 2, 3, 4, 5, 6, 7) : "))
if choiceX == 1:
    printMatrix()
elif choiceX == 2:
    transposedMatrix()
elif choiceX == 3:
    printAlgSumMatrix()
elif choiceX == 4:
    printMinorMatrix()
elif choiceX == 5:
    printInversed()
elif choiceX == 6:
    print("Determinant is : ", determinant)
elif choiceX == 7:
    printMatrix()
    transposedMatrix()
    printAlgSumMatrix()
    printMinorMatrix()
    printInversed()
    print("Determinant is : ", determinant)
    print("")
else:
    print("Wrong choice.")
