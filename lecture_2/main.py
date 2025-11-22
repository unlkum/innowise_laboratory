def generate_profile(age):
    """
    Return Life Stage.
    Args:
        age (int): First num
    
    Returns:
        string: Life stage
    """
    if 0 <= age <= 12:
        return "Child"
    elif 13 <= age <= 19:
        return "Teenager"
    elif age >= 20:
        return "Adult"

def main():
    """Create and Print user profile"""
    user_name = input("Enter your full name: ")
    birth_year_str = input("Enter your birth year: ")

    birth_year = int(birth_year_str)
    current_age = 2025 - birth_year

    hobbies = []
    while True:
        word = input("Enter a favorite hobby or type 'stop' to finish: ")
        if word.lower() == "stop":
            break
        hobbies.append(word)

    life_stage = generate_profile(current_age)

    user_profile = {
        "Name": user_name,
        "Age": current_age,
        "Stage": life_stage,
        "Hobbies": hobbies,
    }
    print("---")
    print("Profile Summary:")
    print(f"Name: {user_profile['Name']}")
    print(f"Age: {user_profile['Age']}")
    print(f"Life Stage: {user_profile['Stage']}")

    if not user_profile["Hobbies"]:
        print("You didn't mention any hobbies.")
    else:
        print(f"Favorite Hobbies ({len(hobbies)}):")
        for hobby in user_profile["Hobbies"]:
            print(f"- {hobby}")
        print("---")


if __name__ == "__main__":
    main()
