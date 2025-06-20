import validator_collection
def main():
    print(validate(input("What's your email address? ")))



def validate(s):
    x = 0
    if '@' in s and validator_collection.is_not_empty(s) and len(s.split()) == 1:
        for i in s:
            if i == '@':
                x+=1
            if x > 1:
                return "Invalid"
        return "Valid"
    else:
        return "Invalid"



if __name__ == "__main__":
    main()
