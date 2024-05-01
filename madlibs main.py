print("""Complete the following paragraph.
Use these words: strive, involves, never, depends""")

Question=("""In the world of coding, developers ____ continuously to improve their skills. 
Whether it ____ learning new languages or mastering algorithms, the journey ____ stops. 
Success ____ not just on talent but also on persistence and dedication.""")

print(Question)
print("""
""")
w1=input("Enter first word: ")
w2=input("Enter second word: ")
w3=input("Enter third word: ")
w4=input("Enter fourth word: ")

final_paragraph = (f"In the world of coding, developers {w1} continuously to improve their skills.\n"
                   f"Whether it {w2} learning new languages or mastering algorithms, the journey {w3} stops.\n"
                   f"Success {w4} not just on talent but also on persistence and dedication.")



if w1=="strive" and w2=="involves" and w3=="never" and w4=="depends":
    print("You got them correct.")
    print("")
    print(final_paragraph)
else:
    print("You are wrong! Do it again.")
