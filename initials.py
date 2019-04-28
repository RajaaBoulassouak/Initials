def get_initials(fullname):
    return ''.join([initial[0] for initial in fullname.split()]).upper()

def main():
    fullname = input("What is your fullname? ")
    initials = get_initials(fullname)
    print(f'The initials of {fullname} are, {initials}')

if __name__ == '__main__':
    main()