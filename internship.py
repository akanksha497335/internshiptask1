import random
import string

# Predefined lists of adjectives and nouns
adjectives = [
    "Cool", "Happy", "Silent", "Funky", "Brave", "Silly", "Epic", "Mighty", "Crazy", "Wild"
]
nouns = [
    "Tiger", "Dragon", "Ninja", "Wizard", "Pirate", "Samurai", "Eagle", "Falcon", "Wolf", "Panther"
]

# Special characters to choose from
special_chars = ['!', '@', '#', '$', '%', '&']

def generate_username(include_number, include_special):
    """Generate a single random username based on preferences."""
    # Choose random adjective and noun
    adjective = random.choice(adjectives)
    noun = random.choice(nouns)
    
    username = adjective + noun
    
    # Optionally add a random number (1 to 999)
    if include_number:
        number = str(random.randint(1, 999))
        username += number
    
    # Optionally add a random special character at the end
    if include_special:
        special = random.choice(special_chars)
        username += special
        
    return username

def save_usernames(usernames, filename="usernames.txt"):
    """Save generated usernames to a file."""
    with open(filename, "w") as file:
        for name in usernames:
            file.write(name + "\n")
    print(f"\nUsernames have been saved to {filename}")

def main():
    print("Welcome to the Random Username Generator!\n")
    
    # Ask user how many usernames they want to generate
    while True:
        try:
            count = int(input("How many usernames would you like to generate? "))
            if count <= 0:
                print("Please enter a positive integer.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter an integer.")
    
    # Ask for customization options
    include_number = input("Include numbers in the username? (Y/N): ").strip().lower() == "y"
    include_special = input("Include special characters in the username? (Y/N): ").strip().lower() == "y"
    
    # Generate usernames
    usernames = []
    for _ in range(count):
        username = generate_username(include_number, include_special)
        usernames.append(username)
    
    # Display generated usernames
    print("\nGenerated Usernames:")
    for name in usernames:
        print(name)
    
    # Save usernames to file
    save_usernames(usernames)

if __name__ == "__main__":
    main()
