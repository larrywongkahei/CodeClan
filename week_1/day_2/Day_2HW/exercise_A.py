stops = [ "Croy", "Cumbernauld", "Falkirk High", "Linlithgow", "Livingston", "Haymarket" ]

#1. Add "Edinburgh Waverley" to the end of the list
stops.append("Edinburgh")
##         check point       ##
# print(stops)


#2. Add "Glasgow Queen St" to the start of the list
stops.insert(0, "Glasgow Queen St")
##         check point ###
# print(stops)


#3. Add "Polmont" at the appropriate point (between "Falkirk High" and "Linlithgow")
stops.insert(3, "Polmont")
##         check point ###
# print(stops)
  

#4. Print out the index position of "Linlithgow"
print(stops.index("Linlithgow"))
##


#5. Remove "Livingston" from the list using its name
stops.remove("Livingston")
##            check point ###
# print(stops)


#6. Delete "Cumbernauld" from the list by index
stops.pop(1)
##         check point ###
# print(stops)


#7. Print the number of stops there are in the list
print(len(stops))


#8. Sort the list alphabetically
stops.sort()
##          check point #
# print(stops)


#9. Reverse the positions of the stops in the list
stops.reverse()
##           check point    #
# print(stops)


#10 Print out all the stops using a for loop
for stop in stops:
    print(stop)