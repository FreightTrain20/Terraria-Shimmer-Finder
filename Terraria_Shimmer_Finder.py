print ("Terraria Shimmer Finder")
guidename = input("Enter World's First Guide Name:")
print ("Guide's name is", guidename, "Correct?")
user_input = input("Y/N:")

if user_input.lower() == "n":
    print ("Please restart the program to enter the correct name.")
    exit()
elif user_input.lower() == "y":
    print ("Continuing...")
    
    def get_guide_rng(name):
        guide_map = {
            "joe": 0.0000,
            "connor": 0.0278,
            "tanner": 0.0556,
            "wyatt": 0.0833,
            "cody": 0.1111,
            "levi": 0.1389,
            "luke": 0.1667,
            "jack": 0.1944,
            "scott": 0.2222,
            "logan": 0.2500,
            "cole": 0.2778,
            "asher": 0.3056,
            "bradley": 0.3333,
            "jacob": 0.3611,
            "garrett": 0.3889,
            "dylan": 0.4167,
            "maxwell": 0.4444,
            "steve": 0.4722,
            "brett": 0.5000,
            "andrew": 0.5278,
            "harley": 0.5556,
            "kyle": 0.5833,
            "jake": 0.6111,
            "ryan": 0.6389,
            "jeffrey": 0.6667,
            "seth": 0.6944,
            "marty": 0.7222,
            "brandon": 0.7500,
            "zach": 0.7778,
            "jeff": 0.8056,
            "daniel": 0.8333,
            "trent": 0.8611,
            "kevin": 0.8889,
            "brian": 0.9167,
            "colin": 0.9444,
            "jan": 0.9722
        }
        
        lookup_name = name.lower()
        if lookup_name in guide_map:
            Guide_RNG = guide_map[lookup_name]
            return Guide_RNG
        else:
            print(f"Guide name '{name}' not found in list.")
            return None

    # get the RNG value for the name they already entered
    Guide_RNG = get_guide_rng(guidename)

    if Guide_RNG is not None:
        print(f"The RNG value for {guidename} is {Guide_RNG}")
else:
    print ("Invalid input. Please restart the program and enter Y or N.")
    exit()
print ("1.Large")
print ("2.Medium")
print ("3.Small")

world_size = input("World Size?")
if world_size == "1":
    world_size_user = "Large"
if world_size == "2":
    world_size_user = "Medeum"
if world_size == "3":
    world_size_user = "Small"
print ("World Size is", world_size_user, "Correct?")
user_input = input("Y/N:")
if user_input.lower() == "n":
    print ("Please restart the program to enter the correct world size.")
    exit()
print ("1.Snow")
print ("2.Dungeon")
print ("3.Jungle")
user_input = input("Which of the following have you located?")
if user_input == "1":
    biome = "Snow"
    print ("1.left")
    print ("2.right")
    user_input_Snow = input("Witch side?")
if user_input == "2":
    biome = "Dungeon"
    print ("1.left")
    print ("2.right")
    user_input_Dungeon = input("Witch side?")
if user_input == "3":
    biome = "Jungle"
    print ("1.left")
    print ("2.right")
    user_input_Jungle = input("Witch side?")
print ("Biome is", biome, "Correct?")
user_input = input("Y/N:")
if user_input.lower() == "n":
    print ("Please restart the program to enter the correct biome.")
    exit()



    # --- PART 2: CALCULATE SHIMMER COORDS USING GUIDE_RNG, WORLD SIZE, AND BIOME SIDE ---

print("\n--- Calculating Shimmer Coordinates ---")

# Determine which side variable to use based on selected biome
if biome == "Jungle":
    selected_side = user_input_Jungle
elif biome == "Dungeon":
    selected_side = user_input_Dungeon
elif biome == "Snow":
    selected_side = user_input_Snow
else:
    print("Unknown biome. Exiting.")
    exit()

# Calculate the compass mark using x = Guide_RNG
x = Guide_RNG

# Calculate based on selected biome side and world size
if selected_side == "1":  # Side 1 (left for jungle, right for dungeon/snow based on chart)
    if world_size_user == "Small":
        if biome == "Jungle":
            coord = 3800 - ((3800 - 3276) * x)  # jungle on left
        else:  # dungeon or snow
            coord = 3276 + ((3800 - 3276) * x)  # dungeon/snow on right
    elif world_size_user == "Medeum":
        if biome == "Jungle":
            coord = 6000 - ((6000 - 4992) * x)
        else:  # dungeon or snow
            coord = 4992 + ((6000 - 4992) * x)
    elif world_size_user == "Large":
        if biome == "Jungle":
            coord = 8000 - ((8000 - 6552) * x)
        else:  # dungeon or snow
            coord = 6552 + ((8000 - 6552) * x)

elif selected_side == "2":  # Side 2 (right for jungle, left for dungeon/snow based on chart)
    if world_size_user == "Small":
        if biome == "Jungle":
            coord = 3276 + ((3800 - 3276) * x)  # jungle on right
        else:  # dungeon or snow
            coord = 3800 - ((3800 - 3276) * x)  # dungeon/snow on left
    elif world_size_user == "Medeum":
        if biome == "Jungle":
            coord = 4992 + ((6000 - 4992) * x)
        else:  # dungeon or snow
            coord = 6000 - ((6000 - 4992) * x)
    elif world_size_user == "Large":
        if biome == "Jungle":
            coord = 6552 + ((8000 - 6552) * x)
        else:  # dungeon or snow
            coord = 8000 - ((8000 - 6552) * x)

else:
    print("Invalid side selection.")
    exit()

# Output result
if 'coord' in locals():
    print(f"\n✅ Your Shimmer Compass Mark is at X = {int(coord)}")
    print(f"→ Use this with your Terraria compass to find Shimmer!")
    print ("Remember to go towrds the Jungle, or away from the Dungeon/Snow biome!")
else:
    print("❌ Could not calculate coordinates. Please check inputs.")

print("\n--- Script Complete ---")