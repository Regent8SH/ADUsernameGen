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

Example usage:

testnames.txt contents:
'''
John Hammond\n
The Cyber Mentor\n
Professor  Messer\n
ippsec\n
'''

>./ADUsernameGen.py -i testnames.txt -o testoutput.txt

>cat testoutput.txt
 
JohnHammond\n
John.Hammond\n
JHammond\n
JohnH\n
JohHam\n
JHam\n
JohnHammond1\n
John.Hammond1\n
JHammond1\n
JohnH1\n
JohHam1\n
JHam1\n
TheMentor\n
The.Mentor\n
TMentor\n
TheM\n
TheMentor1\n
The.Mentor1\n
TMentor1\n
TheM1\n
ProfessorMesser\n
Professor.Messer\n
PMesser\n
ProfessorM\n
ProMes\n
PMes\n
ProfessorMesser1\n
Professor.Messer1\n
PMesser1\n
ProfessorM1\n
ProMes1\n
PMes1\n
