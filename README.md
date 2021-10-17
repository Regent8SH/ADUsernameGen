# ADUsernameGen
Generates a list of possible Active Directory usernames with a list of collected names

Script to be used to generate a list of possible Active Directory usernames when supplied with a txt list of names.
I guess it could be used to generate potential usernames for anything, but I had AD in mind when writing it.

python3 must be installed
On linux you can install as follows:
sudo apt-get install python3.6

Example usage is as follows:
./ADUsernameGen.py -i original.txt -o generated.txt

Yes, it is up to you to create a text list of people's names. I can't do everything. Seperate them with newlines and you're good to go.

If additional naming standards are needed, they can easily be added into the "mangleNames" function

Please note: provided names without spaces will be disregarded
... I'M LOOKING AT YOU BEYONCE...
