import random

option = ["sasso", "carta", "forbice"]
user_point = 0
pc_point = 0

while True:
    print("scrivi sasso/carta/forbice o Q per quittare")
    user_input = input().lower()
    random_number = random.randint(0, 2)
    pc_input = option[random_number]

    if user_input in option:
        print("il pc ha scelto:", pc_input)
        if user_input == "sasso" and pc_input == "forbice":
            user_point += 1
            print("Hai vinto!","[", user_point,"]")
            print("")
            continue
        elif user_input == "carta" and pc_input == "sasso":
            user_point += 1
            print("Hai vinto!", "[", user_point, "]")
            print("")
            continue
        elif user_input == "forbice" and pc_input == "carta":
            user_point += 1
            print("Hai vinto!", "[", user_point, "]")
            print("")
            continue
        elif user_input == pc_input:
            print("Avete fatto la stessa scelta riprova!")
            print("")
            continue
        else:
            pc_point += 1
            print("Hai perso!", "[", pc_point, "]")
            continue
    elif user_input == "q":
        break
    elif user_input not in option:
        print("Devi scegliere sasso/carta/forbice!")
        print("")
        continue
print("alla prossima!")