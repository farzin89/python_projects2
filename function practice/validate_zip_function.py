

def validate_zip_code(zipcode):

    if len(zipcode) == 5 and zipcode.isdigit():
        print("%s is valid zip code" %(zipcode))
    else:
        print("%s is not valid zip code" %(zipcode))


num =input("Enter your Zip code : ")
validate_zip_code(num)