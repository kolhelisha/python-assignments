def validate_pan(pan):
    if(len(pan)== 10 and
       pan[0:5].isalpha() and
       pan[:5].isupper() and
       pan[5:9].isdigit() and
       pan[9].isalpha() and
       pan[9].isupper()):
        return True
    else:
        return False    
def pan_category(pan):
    category_dict = {
        'A' : "Association of Persons (AOP)",
        'B' : "Body of Individuals (BOI)",
        'G' : "Government Agency",
        'J' : "Artificial Juridical Person",
        'L' : "Local Authority",
        'F' : "Firm",
        'T' : "Trust",
        'C' : "Company",
        'P' : "Individual",
        'H' : "HUF (Hindu Undivided Family)"
    }
    category_code = pan[3]
    return category_dict.get(category_code, "Unknown Category")
pan = input("Enter your PAN number: ")
if validate_pan(pan):
    print("Valid PAN number")
    category = pan_category(pan)
    print("Category:", category)
else:
    print("Invalid PAN number")
