

def validate_zip_code(zipcode):

    if len(zipcode) == 5 and zipcode.isdigit():
        print("your zip code is valid")
    else:
        print("your zip code is not valid")


num =input("Enter your Zip code : ")
validate_zip_code(num)