print("My Name is Faheem")
name :str="faheem Saif"
print(name)

fname:str = "Faheem"
lname:str = "Saif"
age:int = 23
education:str  = "BS Computer science"
card:any = f"""PIAIC Student card
Student Name: {fname+" "+ lname}
 Age: {age} 
 Education: {education}
" Print the card"  """
print(card)
# string boundries
# "'", '"' use
name:str = "I'm Faheem"
print(name)
# backslash \ IS USED  for the conversion of any special character to normal character
name2:str = 'I\'m Faheem'
print(name2)


import re 
name: str = "           Faheem           saif    " 
display(name)

name1: str = re.sub('{2,100}',' ',name )
display(name1)