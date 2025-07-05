"""
How can we add the family pet, "Dino", to the following list?

flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
"""
# 1. Using the append method
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.append("Dino")
print(flintstones)

# 2. Using the extend method
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.extend(["Dino"])
print(flintstones)

# 3. Using the insert method
flintstones = ["Fred", "Barney", "Wilma", "Betty", "Bambam", "Pebbles"]
flintstones.insert(len(flintstones), "Dino")
print(flintstones)

"""
LS Solution
"""

flintstones.append("Dino")