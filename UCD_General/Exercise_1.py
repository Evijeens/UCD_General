# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# Create list areas
areas= [hall , kit , liv , bed , bath]
# Print areas
print(areas)
# Adapt list areas
areas = ["hallway" , hall , "kitchen" , kit, "living room", liv, "bedroom" , bed, "bathroom", bath]

# Print areas
print(areas)
# area variables (in square meters)
hall = 11.25
kit = 18.0
liv = 20.0
bed = 10.75
bath = 9.50

# house information as list of lists
house = [["hallway", hall],
         ["kitchen", kit],
         ["living room", liv] ,
         ["bedroom" , bed] ,
         ["bathroom" , bath]]

# Print out house
print(house)

# Print out the type of house
print(type(house))
# Create the areas list
areas = ["hallway", 11.25, "kitchen", 18.0, "living room", 20.0, "bedroom", 10.75, "bathroom", 9.50]

# Print out second element from areas
print(areas[2])

# Print out last element from areas
print(areas[-1])

# Print out the area of the living room
print(areas[5])
# Sum of kitchen and bedroom area: eat_sleep_area
eat_sleep_area = (areas[3] + areas[7])

# Print the variable eat_sleep_area
print(eat_sleep_area)
# Use slicing to create downstairs
downstairs = areas[0:6]

# Use slicing to create upstairs
upstairs = areas[6:10]

# Print out downstairs and upstairs
print(downstairs , upstairs)
# Alternative slicing to create downstairs
downstairs = areas[:6]

# Alternative slicing to create upstairs
upstairs = areas[6:]
print(downstairs , upstairs)
# Correct the bathroom area
areas[-1] = "10.50"

# Change "living room" to "chill zone"
areas[4] = "chill zone"
print(areas)
# Add poolhouse data to areas, new list is areas_1
areas_1 = areas + ["poolhouse" , 24.5]

# Add garage data to areas_1, new list is areas_2
areas_2 = areas_1 + ["garage" , 15.45]
print(areas_2)
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Create areas_copy
areas_copy = list(areas)

# Change areas_copy
areas_copy[0] = 5.0

# Print areas
print(areas)
# Create variables var1 and var2
var1 = [1, 2, 3, 4]
var2 = True

# Print out type of var1
print(type(var1))

# Print out length of var1
print(len(var1))

# Convert var2 to an integer: out2
out2 = int(var2)
# Create lists first and second
first = [11.25, 18.0, 20.0]
second = [10.75, 9.50]

# Paste together first and second: full
full = first + second

# Sort full in descending order: full_sorted
full_sorted = sorted(full, reverse = True)

# Print out full_sorted
print(full_sorted)
# string to experiment with: place
place = "poolhouse"

# Use upper() on place: place_up
place_up = place.upper()

# Print out place and place_up
print(place)
print(place_up)

# Print out the number of o's in place
print(place.count('o'))
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Print out the index of the element 20.0
print(areas . index(20.0))

# Print out how often 9.50 appears in areas
print(areas . count(9.5))
# Create list areas
areas = [11.25, 18.0, 20.0, 10.75, 9.50]

# Use append twice to add poolhouse and garage size
areas.append(24.5)
areas.append(15.45)

# Print out areas
print(areas)

# Reverse the orders of the elements in areas
areas.reverse()

# Print out areas
print(areas)
