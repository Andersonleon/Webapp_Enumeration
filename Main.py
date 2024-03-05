import requests;
import os;


#  todo
# install wordlists and tools,
#



def robots(EnumerateLink):
    os.system(f"wget {EnumerateLink}/robots.txt > robots.txt")
    return;

def fingerprint(EnumerateLink): ##nikto scan

    os.system(f"nikto -h {EnumerateLink} > niktoscan")

    return;

def directory(EnumerateLink):
    os.system(f"dirb {EnumerateLink} common.txt > dirbscan")


def main():

    EnumerateLink = input("please enter the link that is going to be enumerated upon: ")
    fingerprint(EnumerateLink)
    robots(EnumerateLink)

if __name__ == "__main__":
    main()

