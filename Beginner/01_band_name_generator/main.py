#1. Create a greeting for your program.

#2. Ask the user for the city that they grew up in.

#3. Ask the user for the name of a pet.

#4. Combine the name of their city and pet and show them their band name.

#5 Make sure the input cursor shows on a new line.


print("Greetings fellow music fan!\n"
      "This program will ask you two questions:\n"
      "1) The city you grew up in;\n"
      "2) The name of a pet.\n"
      "After you answer these questions, we will generate the name of a band for you!\n"
      "So, let's get started!")

city_name = input("Tell us the name of the city you grew up in:\n")
print('Excellent!')
pet_name = input("Now tell us the name of a pet:\n")
print("Brilliant. Now let us create a band name for you\nWorking.....")
print('Your band name is: ' + city_name.capitalize() + ' ' + pet_name)
