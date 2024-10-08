import pyotp # For generating and validating OTPs
import time # For handling time delays (if needed)
# Simulate a user database
users_db = {}
# Function to register a user and generate a 2FA secret
def register_user(username):
      # Generate a unique OTP secret
secret = pyotp.random_base32()
users_db[username] = { 'secrets' : secret, 
                      'is_2fa_enabled': True # Assume 2FA is enabled
                     }
    print(f"User '{username}' registered with 2FA. Secret: {secret}")
# Function to generate OTP for a user

def generate_otp(username):
  if username in users_db and users_db[username]['is_2fa_enabled']:
            secret = users_db[username]['secret']
  totp = pyotp.TOTP(secret)  # Create a TOTP object using the secret
        return totp.now()  # Generate the current OTP
    else:
        return None
