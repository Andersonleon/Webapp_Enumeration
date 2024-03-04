import requests;
import os;


def robots():
    return;

def fingerprint(EnumerateLink):

    os.system("nikto -h {EnumerateLink} > nikto")

    return;




def main():

    EnumerateLink = input("please enter the link that is going to be enumerated upon: ")
    fingerprint(EnumerateLink)

if __name__ == "__main__":
    main()

