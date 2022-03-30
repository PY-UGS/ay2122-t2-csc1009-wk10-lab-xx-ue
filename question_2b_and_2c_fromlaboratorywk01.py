#part1
print("Part 1-------------")
def find_module_name(module_code):
    switcher = {
        "CSC1006": "Math2",
        "CSC1007": "Operating Systems",
        "CSC1008": "Data Structure and Algorithm",
        "CSC1009": "Object Oriented Programming",
        "CSC1010": "Computer Network"
    }
    print("Module name: " +switcher.get(module_code, "Invalid"))
print("Enter module code")  
user_input=input()
find_module_name(user_input)


#part2
print("\nPart 2-------------")
for i in range(102,65,-1):
    if (i % 2) != 0:
        print(i)