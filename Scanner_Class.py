print("Welcome to My_Game")
a = input("What is your Good Name: ")
if a:  # Check if input is not empty
    print("Thanks for entering My_Game")

b = input("What is your College Name: ")
if b:  # Check if input is not empty
    print("Thanks for entering your college details")

c = input("Enter your years of experience: ")
if c:  # Check if input is not empty
    print("Thanks for your experience information")

print("Please check all your application details once for confirming:")
print(a,
      b,
      c)

d = input("Can we proceed? (Yes/No): ")
if d.lower() == "yes":
    print("Thank you for your trust. We will proceed with your application.")
else:
    print("Thanks for visiting. Have a nice day!")
    exit()  # Ends the program here if the user says "No"

e = input("We will update you once your application is shortlisted. How was your experience? ")
print("Thanks for choosing us!")



