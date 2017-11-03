from helpers import alphabet_position, rotate_character


def encrypt(text,rot):
    encrypted = ''
    for char in text:
        encrypted += rotate_character(char,rot)

    return encrypted




def main():
    text = input ("What is the message you wish to encrypt?")
    rot = input ("what is your encrypt factor?")
    print (encrypt(text,rot))


if __name__ == "__main__":
    main()
