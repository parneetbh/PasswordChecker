# Password Checker

This Python script checks if a given password has been previously exposed in data breaches using the Pwned Passwords API. It uses a k-anonymity model to protect your sensitive information while performing the check.

## Getting Started

Follow these instructions to get a copy of the project up and running on your local machine.

## Prerequisites

Python 3.x
Requests library (install via pip install requests)

## Installation

Clone the repository to your local machine:
git clone https://github.com/your-username/password-checker.git

Change the directory to the project folder:
cd password-checker

Run the script with your password as an argument:
python password_checker.py your_password

## How it Works

The script utilizes the Pwned Passwords API, which provides a secure way to check if a password has been exposed in previous data breaches without sending the actual password. It works as follows:
The input password is hashed using SHA-1.
The first 5 characters of the hashed password are sent to the Pwned Passwords API.
The API responds with a list of suffixes and counts.
The script compares the hashed password's suffix with the received suffixes to determine if the password has been compromised.

## Usage

To check a password, run the script with the password(s) you want to check as arguments. For example:

python password_checker.py mypassword1 mypassword2

The script will provide feedback on whether each password has been exposed in data breaches.


