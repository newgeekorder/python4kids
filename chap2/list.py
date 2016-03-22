# this is an example of a list also called an array

# potion list
wizard_list = ['spider legs', 'toe of frog', 'eye of newt', 'bat wing', 'slug butter', 'snake dandruff']
print("my starter list " + str(wizard_list))

# things we need from humans
human_list = ['hair', 'toe nails']
print ("things we need from a human target " + str(human_list))

print ("#######################################")
print ("To create a love potion we need both lists: ")
print ( wizard_list + human_list)
total_list = wizard_list + human_list
print ("total number of items needed " + str( len( total_list )) + "\n")

# get a sepecific item
# Note the array counts from 0
print ("Item number 3 is " + total_list[2] )

# google how to print the list in reverse 
