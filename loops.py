vendors = ["Cisco", "HP", "Nortel", "Avaya", "Juniper"]
	 
for element in vendors: #interating over a sequence and executing the code indented under the "for" clause for each element in the sequence
    print(element)
else: #the indented code below "else" will be executed when "for" has finished looping over the entire list
       print("The end of the list has been reached")
