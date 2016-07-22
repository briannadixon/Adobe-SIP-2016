start = '''
You wake up one morning and find that you aren’t in your bed; you aren’t even in your room.
You’re in the middle of a giant maze.
A sign is hanging from the ivy: “You have one hour. Don’t touch the walls.”
There is a hallway to your right and to your left.
'''


print("start")


user_input = input("Type 'left' to go left or 'right' to go right.") 
while (user_input !=left and right):
	print("invaild")
	user_input= input()
if user_input == "left":
    print("You decide to go left and you touch the wall") # finished the story by writing what happens
    #done = True
    user_input= input("pick water or run ")
    if user_input == "run":
    	print("You decide to go left and you get away from zombies")
    if user_input == "get water":
   	 print("You decide to go right and you find a pond and a bucket")
   	 user_input=input()
    if user_input== "water":
    	print("You decide to get water and you drowned the zombies")
    if user_input =="go straight":
   		print("find the exit")




elif user_input == "right":
    print("You choose to go right and you are closer to the exit") # finished the story writing what happens
    user_input=input("pick walk or find fire")
    if user_input == "walk":
    	print("You decided to go straight and the zombies catch you")
    	
    	if user_input ==("find fire"):
    		print("You decide to find the fire and you make it spread")
    	if user_input =="go straight":
    		print("run til 10 steps to find the exit") 
    

