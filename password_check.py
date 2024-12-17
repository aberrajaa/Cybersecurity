import re
import random
import string
import hashlib
import requests
from zxcvbn import zxcvbn

def validate_password(password):
    
    if len(password) < 8:
        return "Weak: Less than 8 characters"
    if not re.search("[A-Z]", password):
        return "Weak: Missing uppercase letter"
    if not re.search("[a-z]", password):
        return "Weak: Missing lowercase letter"
    if not re.search("[0-9]", password):
        return "Weak: Missing number"
    if not re.search("[@#$%^&+=!]", password):
        return "Weak: Missing special character"
    return "Medium" if len(password) < 12 else "Strong"

def analyze_password_strength(password):
       
    result = zxcvbn(password)
    score = result["score"]  
    time_to_crack = result["crack_times_display"]["offline_fast_hashing_1e10_per_second"]
    feedback = result["feedback"] 
    
    return {
        "score": score,
        "time_to_crack": time_to_crack,
        "feedback": feedback 
    }


def check_password_pwned(password):
    
    sha1_password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    prefix, suffix = sha1_password[:5], sha1_password[5:]
    response = requests.get(f"https://api.pwnedpasswords.com/range/{prefix}")

    if response.status_code != 200:
        return "Error: Unable to connect to HIBP API."

    hashes = (line.split(':') for line in response.text.splitlines())
    for h, count in hashes:
        if h == suffix:
            return f"Compromised: Found {count} times."
    return "Safe: Not found in HIBP database."

def generate_password(length=16):
 
    characters = string.ascii_letters + string.digits + "@#$%^&+=!"
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def password_check():
    print("=== Password Security Analyzer ===")
    password = input("Enter your password: ")

    basic_validation = validate_password(password)
    print(f"Password Strength (basic): {basic_validation}")
    print("\n")
    
    advanced_analysis = analyze_password_strength(password)
    print(f"Password Strength (advanced): Score {advanced_analysis['score']} / 4")
    print(f"Estimated time to brute-force: {advanced_analysis['time_to_crack']}")
    print(f"Feedback : {advanced_analysis['feedback']['warning']}")
    print(f"Suggestion : {advanced_analysis['feedback']['suggestions']}")
    
    print("\n")
    print("Have your password been compromised ?")
    pwned_check = check_password_pwned(password)
    print(f"Compromised Check: {pwned_check}")
    print("\n")
    
    if basic_validation == "Weak" or pwned_check.startswith("Compromised"):
        print("\nYour password is not secure. Generating a secure password...")
        secure_password = generate_password()
        print(f"Generated Password: {secure_password}")
        print("Please save this password securely.")

if __name__ == "__main__":
    password_check()
