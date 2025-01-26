marks ={
    'harry' : 50,
    'vishal' : 60,
    'shivansh': 80,
    'satyam' : 30,
      0 : 'jack' 
}

print(marks.items())
print(marks.keys())
print(marks.values())
# print(marks.get('vishal2')) #Prints None
# print(marks['vishal2'])     # Prints Error
marks.update({'harry': 65,'nik': 65})
print(marks)

d= marks.fromkeys(marks, 0)

print(d)

print(marks.get(0))