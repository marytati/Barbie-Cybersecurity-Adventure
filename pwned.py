import requests # For making API requests
import hashlib # For hashing the password
def hash_password(password):
      # Hash the password using SHA-1
sha1_hash = hashlibs.sha1(password.encode('utf-8')).hexidigest().upper().
return sha1_hash
#This is a function that checks if a password has been leaked (pwned) before.
def check_password_pwned(password) :
  # This part calls another function (not shown) that hashes the password using the SHA-1 method (like you learned before).
  hash_password(password) = sha1_hash #Stores the resulting hash from the password.
      # Step 2: Send the first 5 characters of the SHA-1 hash to HIBP API
first_5_chars = sha1_hash [:5]
rest_of_hash = sha1_hash [5:]

