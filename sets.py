set1 = {"1.1.1.1", "2.2.2.2", "3.3.3.3", "4.4.4.4"} #creating a set 
list1 = [11, 12, 13, 14, 15, 15, 15, 11]
string1 = "aaabcdeeefgg"
set1 = set(list1) #creating a set from a list; removing duplicate elements; returns {11, 12, 13, 14, 15}
set2 = set(string1) #creating a set from a string; removing duplicate characters; returns {'b', 'a', 'g', 'f', 'c', 'd', 'e'}; remeber that sets are UNORDERED collections of elements
len(set1) #returns the number of elements in the set
11 in set1 #returns True; checking if a value is an element of a set
	 
10 not in set1 #returns True; checking if a value is an element of a set
set1.add(16) #adding an element to a set
	 
set1.remove(16) #removing an element from a set
