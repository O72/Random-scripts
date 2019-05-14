from zipfile import ZipFile
import argparse

parser = argparse.ArgumentParser(description="\nUsage: python zipbrute.py -z <zipfile.azip> -p <passwordfile.txt>")
parser.add_argument("-z", dest="ziparchive", help="Zip archive file")
parser.add_argument("-p", dest="passfile", help="password file")
parsed_args = parser.parse_args()

try:
    ziparchive=ZipFile(parsed_args.ziparchive)
    passfile=parsed_args.passfile
    foundpass=""

except:
    print(parser.description)
    exit(0)

with open(passfile, "r") as f:
    for line in f:
        password = line.strip("\n")
        password = password.encode("utf-8")

        try:
            foundpass = ziparchive.extractall(pwd=password)
            if foundpass == None:
                print("\n Found password: ", password.decode())
        except RuntimeError:
            pass
    if foundpass == "":
        print("/n Password not found. Try a bigger password list.")
