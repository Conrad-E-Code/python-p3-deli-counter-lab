katz_deli = []

def line(deli):
    if  len(deli) == 0:
        print("The line is currently empty.")
    else:
        output = "The line is currently:"
        # ["".join(f"{idx+1}: {name}") for idx, name in enumerate(deli)]
        for idx, person in enumerate(deli):
            output = " ".join([output, f"{idx+1}. {person}"])
        print(output)

def take_a_number(line, name):
    line.append(name)
    position = len(line)
    print(f"Welcome, {name}. You are number {position} in line.")

def now_serving(line):
    if len(line) == 0:
        print("There is nobody waiting to be served!")
    else:
        print(f"Currently serving {line.pop(0)}.")
    pass

