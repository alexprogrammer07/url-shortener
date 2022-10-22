import pyshorteners  # Importing package by which links can be shortened

print("Simple URL shortener :) ")

while True:
    print("\nEnter 'Q' to Quit the program")

    link = input("Enter the Link to shorten:\n")  # Inputs and stores url in lowercase

    if link == "q" or link == "quit":
        exit(0)

    shortener = pyshorteners.Shortener()  # Function to shorten the url

    shortened_link = shortener.tinyurl.short(link)  # using tinyurl.com for shortening the link

    print(shortened_link)  # Printing the shortened link
    print(type(link))       #get the class thelink variable
