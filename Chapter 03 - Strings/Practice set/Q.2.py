letter = ''' Dear, <|name|>
             You are selected
             <|Date|> '''

a = (input("Enter the name:"))
b=  (input("Enter date:"))

# letter= letter.replace("<|name|>",  a )
# letter= letter.replace("<|Date|>",  b )
# print(letter) This will aslo work 

print(letter.replace("<|name|>", a).replace ( "<|Date|>", b))