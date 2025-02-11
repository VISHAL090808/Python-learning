

with open(r'd:\Python\Chapter 09 - file\Practice_set\log.html') as f:
   lines = f.readlines()

lineno = 1
for line in lines :
        if('python' in line):
              print('yes! python present in line no ', lineno)
        else:
              ('there is no python in the line ')
        
        lineno+=1


        
