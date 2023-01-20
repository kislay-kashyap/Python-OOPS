class VoterAgeException(Exception):
    pass

def validate_voter_age(age):
    if(age<18):
        raise VoterAgeException("Voters must be of 18 or more")
    
age = int(input("Enter your age: "))
try:
    validate_voter_age(age)
    print("You are eligible to vote")
except VoterAgeException as e:
    print(e)
