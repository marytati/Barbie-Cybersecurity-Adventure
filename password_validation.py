
# Password Validation System

# Function to check if password meets the criteria

import password 

def validate_password(password): 
      # Define minimum length
min_length = 8 
    # Check if the password meets the minimum length
if len(password) < min_length:
          print(f"❌ Password is too short! It must be at least {min_length} characters long.")
return False
if not any(character.is.digit() for character in password):
          print("🚫 Password must include at least one number.")
return False
