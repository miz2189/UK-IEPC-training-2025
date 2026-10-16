
num = int(input())

plan = []

REST = "\U0001F60E"   # 😎
LEG  = "\U0001F9B5"   # 🦵
ARM  = "\U0001F4AA"   # 💪


for _ in range(num):
    a = input()
    if "res" in a:
        plan.append(REST)
    elif "leg" in a:
        plan.append(LEG)
    else:
        plan.append(ARM)


space = 0
track = 0
for i in range(31):
    space += 1
    print(plan[track],end="")
    track += 1
    if track == len(plan) :
         track = 0
    if space % 7 == 0:
        print()