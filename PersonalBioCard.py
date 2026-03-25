#create list
info={}
#take inputs from the user
info["name"]=input("enter name:")
info["age"]=input("enter age :")
info["course"]=input("enter course name:")
info["college"]=input("enter college name:")
info["email"]=input("enter email:")

title="PERSONAL BIO CARD"
#when we are writing code,we even need to think of edge cases

#if in case for empty input:
for key in info:
    if info[key] == "":
        info[key] = 'NULL'
#prepare lines ,like how they to be presented
max_key_length=max(len(key) for key in info)
lines=[]
for key,value in info.items():
    line=key.ljust(max_key_length) +" : "+ value
    lines.append(line)

#now lets calculate maximum width
max_length=0
for line in lines:
    if len(line)>max_length:
        max_length=len(line)
 #compare line length with title       
if len(title)>max_length:
    max_length=len(title)

#add space for box orders
max_length=max_length+4
#now lets print the bio card
print("╔" + "="*max_length + "╗")
print("║ "+ title.center(max_length-2) + " ║")
print("╠" + "="*max_length + "╣")
for line in lines:
    print("║ " + line.ljust(max_length-2)+ " ║")
print("╚" + "="*max_length + "╝")
