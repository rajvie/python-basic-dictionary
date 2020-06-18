import json
from difflib import get_close_matches 
data = json.load(open("D:\college\semester 2 ty\Python\original.json"))

def translate(w):
	w = w.lower()
	if w in data:
		return data[w]
	elif len(get_close_matches(w,data.keys()))>0:
		yn = input("Did You Mean %s Instead.\n Enter Y if Yes or N if No : \n" %get_close_matches(w,data.keys())[0])
		if yn == "Y":
			return (get_close_matches(w,data.keys())[0])
		elif yn == "N":
			return "The Word Doesn't Exist"
		else:
			return "We Didn't Understand Your Query " 
	else:
		return "The Word Doesn't Exist" 
	
word = input("Enter Word:")
output = (translate(word))
if type(output) == list:
	for item in output:
		print(item)
else:
	print(output)
