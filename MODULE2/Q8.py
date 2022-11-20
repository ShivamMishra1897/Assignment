#Write a Python program to test whether a passed letter is a vowel or not
chr = input("Enter a character: ")

if(chr=='A' or chr=='a' or chr=='E' or chr =='e' or chr=='I'
or chr=='i' or chr=='O' or chr=='o' or chr=='U' or chr=='u'):
    print(chr, "is a Vowel")
else:
    print(chr, "is a Consonant")