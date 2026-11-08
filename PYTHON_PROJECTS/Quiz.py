# Day 27: KBC Game using lists, loops, and logic building

questions = [
    ["Which language was used to create Python?", "C", "Java", "C++", "Assembly", 1],
    ["What is the correct file extension for Python files?", ".python", ".pl", ".py", ".p", 3],
    ["Which keyword is used to define a function in Python?", "func", "def", "function", "lambda", 2],
    ["What is the output of 2 ** 3 in Python?", "6", "8", "9", "5", 2]
]

levels = [1000, 2000, 3000, 5000]
money = 0

print("=== Welcome to Kaun Banega Crorepati ===\n")

for i in range(len(questions)):
    q = questions[i]
    print(f"Question for ₹{levels[i]}:")
    print(f"{q[0]}")
    print(f"1. {q[1]}          2. {q[2]}")
    print(f"3. {q[3]}          4. {q[4]}")
    
    reply = int(input("Enter your option (1-4) or 0 to Quit: "))
    
    if reply == 0:
        print(f"\nYou chose to quit the game.")
        break
        
    if reply == q[5]:
        money = levels[i]
        print(f"Correct Answer! You won ₹{money}\n")
    else:
        print("\nWrong Answer!")
        break

print(f"\nGame Over! Total money won: ₹{money}")