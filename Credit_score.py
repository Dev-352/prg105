# Ask your user for their credit score. Tell them if they have Bad, Fair, Good, or Excellent credit.

# inputs integer value from user
credit_score = int(input("What is your credit score? "))

if credit_score >= 720:
    print("You have excellent credit.")
elif credit_score >= 690:
    print("You have good credit.")
elif credit_score >= 630:
    print("You have fair credit.")
else:
    print("Bad credit.")
