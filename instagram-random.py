import requests
import random

def check_username(username):
    url = f"https://www.instagram.com/{username}/?__a=1"
    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

def generate_username():
    prefixes = ['cool', 'awesome', 'super', 'mega', 'fantastic']
    suffixes = ['user', 'insta', 'gram', 'lover', 'fan']
    numbers = random.randint(0, 9999)
    return random.choice(prefixes) + random.choice(suffixes) + str(numbers)

if __name__ == "__main__":
    username = generate_username()
    if check_username(username):
        print(f"The username '{username}' is valid!")
    else:
        print(f"The username '{username}' is not valid.")