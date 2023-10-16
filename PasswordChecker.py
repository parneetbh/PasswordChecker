import requests
import hashlib
import sys

def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        # To check if the request was successful (status code = 200)
        raise RuntimeError(f'Error fetching: {res.status_code}, check API and try again')
    else:
        return res
    
def password_leaks_count(hashes, hash_to_check):
    #Generator that iterates through each line of the response and splits it into a tuple containing the hash(h) and count.
    hashes = (line.split(':') for line in hashes.text.splitlines()) 
    for h, count in hashes:
        if h == hash_to_check:
            return count
    return 0

def pwned_api_check(password):
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first_five_char, tail = sha1password[:5], sha1password[5:]
    response = request_api_data(first_five_char)
    return password_leaks_count(response, tail)

def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f'{password} was found {count} times. Time to change your password!')
        else:
            print(f'{password} was not found. Safe to continue using this password!')
        
if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

