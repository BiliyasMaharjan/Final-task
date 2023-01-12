import sys
import random

def generate_email(name):
  # Split the name into first name and surname
  # Salsbur2y, Debra Mary Adele
  parts = name.split(',')
  surname = parts[0]
  first_names = parts[1].strip()

  # Generate the initials
  # D.M.A
  initials = '.'.join([n[0] for n in first_names.split()])

  # Generate the random digits
  digits = ''.join([str(random.randint(0, 9)) for i in range(4)])

  # Remove any non-alphabetic characters from the surname
  surname = ''.join([c for c in surname if c.isalpha()])
  
  return f"{initials}.{surname}{digits}@poppleton.ac.uk"

# Check if the file name is given or not.
if len(sys.argv) < 2:
  print("Error: Missing command-line argument.")
  sys.exit(1)

# Open the input file.
try:
  with open(sys.argv[1], 'r') as f:
    lines = f.readlines()
except:
  print(f"Error: Cannot open {sys.argv[1]}. Sorry about that.")
  sys.exit(1)

# Open the output file
try:
  with open('emails.txt', 'w') as f:
    # Generate the emails
    for line in lines:
      # c6542898 Salsbury, Debra Mary Adele
      parts = line.strip().split()
      student_id = parts[0]
      name = ' '.join(parts[1:])
      email = generate_email(name)
      f.write(f"{student_id} {email.lower()}\n")
except:
  print("Error: Cannot open abc.txt for writing. Sorry about that.")
  sys.exit(1)
