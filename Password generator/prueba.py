from password import create_password


def get_password(user_password):
    tries = 0

    passwords = []

    while True:
        tries += 1
        password = create_password(len(user_password))

        if tries > 400000:
            print("Password not obtained after 400000 tries")
            break
        if password != user_password and password not in passwords:
            print(f"{tries}- {password}. Incorrect password")
            passwords.append(password)
        elif password == user_password:
            print(f"Password is: {password}. \n{tries} tries")
            break


if __name__ == "__main__":
    user_password = input("Type the password\n")
