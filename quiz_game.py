print("welcome to my computer quiz!")
playing = input("Do you want to play?")
if playing.lower() != "Yes" and playing.lower()!= 'y':
    quit()
print("Okay! Let's Play :)")
# score = 0
# answer = input("what does CPU stand for? ")
# if answer.lower() == "central processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect. The correct answer is Central Processing Unit.")

# answer = input("what does GPU stand for? ")
# if answer.lower() == "graphics processing unit":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect. The correct answer is Graphics Processing Unit.")

# answer = input("what does RAM stand for? ")
# if answer.lower() == "random access memory":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect. The correct answer is Random Access Memory.")


# answer = input("what does PSU stand for? ")
# if answer.lower() == "power supply":
#     print("Correct!")
#     score += 1
# else:
#     print("Incorrect. The correct answer is Power Supply.")

# print(f"Your {score} questions are  Correct")
# print(f"Your score is : {score/4 *100}  %.")


quiz_data= [
    {"question": "what does CPU stand for? ",
     "answer":"central processing unit",
    },
    {"question": "what does GPU stand for?",
     "answer":"graphics processing unit",
    },
    {"question": "what does RAM stand for?",
     "answer":"random access memory",
    },
    {"question": "what does PSU stand for?",
     "answer":"power supply",
    },
]
score = 0
for item in quiz_data:
    answer= input(item["question"] + " ")
    if answer.lower() == item["answer"]:
        print("Correct!")
        score += 1
    else:
        print(f"Incorrect. The correct answer is {item['answer']}")

print(f"Your {score} out of {len(quiz_data)}  questions are  Correct")
print(f"Your score is : {score/len(quiz_data) *100}  %.")