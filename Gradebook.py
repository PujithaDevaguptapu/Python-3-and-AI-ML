last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
subjects = ["Physics", "Calculus", "Poetry", "History"]
grades = [98, 97, 85, 88]
gradebook = [["Physics", 98], ["Calculus", 97], ["Poetry", 85], ["History", 88]]
print(gradebook)

#Adding sublists
gradebook.append(["Computer Science", 100])
gradebook.append(["Visual arts", 93])
print(gradebook)

#Incrementing/Modifing  the value in sublist
gradebook[5][1] += 5
print(gradebook)


gradebook[2].remove(85)
print(gradebook)
gradebook[2].append("Pass")
print(gradebook)

#Combing last sem's gradebook with today's gradebook
full_gradebook = last_semester_gradebook + gradebook 
print(full_gradebook)
