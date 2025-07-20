# A code to grade students
mark = int(input("Enter your marks: "))

if mark >= 80:
    print("Excellent \n You have scored an A grade :)")
elif mark >= 70:
    print("Very good \n You have scored a B grade :)")
elif mark >= 60:
    print("Well done \n You have scored a C grade :)")    
elif mark >= 50:
    print("Good \n You have scored a D grade :)")
elif mark >= 40:    
    print("You can do better next time \n You have scored an E grade :)")

else:
    print("You have failed the exam :( \n You need to score at least 40 marks to pass")