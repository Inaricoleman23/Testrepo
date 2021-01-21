print("Hello World")

#list functions
cats = ["Siamese", "Burmese", "Savannah Cat"]
cats.append("BobCat")
cats.pop()
print(cats)

#lists
celebrities = "John Wall"
print(celebrities.lower())
print(celebrities.upper())
print(celebrities.title())
print(f"Hi my favorite person is {celebrities}" )

#input functions
birth_year = input("Enter birth year :")
print("You were born " +  birth_year )

colors= input(" What is your favorite color is : ")
print(" My favorite is " + colors )

#f-string
first_name = input("what is your first name :")
last_name = input("what is your last name :")
full_name = (f"{first_name} {last_name}")
print(full_name)
