
def main():
    print(" welcome to the Email slicer ")
    print("")

    email_input = input("Input your email address : ")

    (username,domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username : ",username)
    print("Domain : " ,domain)
    print("Extention",extension)

main()