"""
@Author: Stavros
@Project: Passwd Parser
@Description:
	This script opens the /etc/passwd file and parse it in order to print the information that is saved
	in that file in a user-friendly manner.

	/etc/passwd file format:
	username:passwd:uid:gid:description:home:shell

@Version: v1
@TODO: Add Comments to Functions
"""
import sys

class PasswdParser():
  
  def __init__(self):
    self.__username = ''
    self.__passwd = ''
    self.__uid = ''
    self.__gid = ''
    self.__decription = ''
    self.__home = ''
    self.__shell = ''

  def __findAll(self, character, string):
    indexes = []
    for index in range(len(string)):
      if(string[index] == character):
        indexes.append(index)
    return indexes
  
  def __extractInfo(self, locationsOfDelimeter,LineFromFile):
    usernameSlice = locationsOfDelimeter[0]
    passwdSlice = locationsOfDelimeter[1]
    uidSlice = locationsOfDelimeter[2]
    gidSlice = locationsOfDelimeter[3]
    descriptionSlice = locationsOfDelimeter[4]
    homeSlice = locationsOfDelimeter[5]

    self.__username = LineFromFile[:usernameSlice]
    self.__passwd = LineFromFile[(usernameSlice + 1) : passwdSlice]
    self.__uid = LineFromFile[(passwdSlice + 1) : uidSlice]
    self.__gid = LineFromFile[(uidSlice + 1) : gidSlice]
    self.__decription = LineFromFile[(gidSlice + 1) : descriptionSlice]
    self.__home = LineFromFile[(descriptionSlice + 1) : homeSlice]
    self.__shell = LineFromFile[(homeSlice + 1) :]

    print("Username: {}".format(self.__username))
    print("\tPassword: {}".format(self.__passwd))
    print("\tUID: {}".format(self.__uid))
    print("\tGID: {}".format(self.__gid))
    print("\tDescription: {}".format(self.__decription))
    print("\tHome: {}".format(self.__home))
    print("\tShell: {}".format(self.__shell))
  
  def __extractUsernames(self, LineFromFile):
    delimeter = LineFromFile.index(':')
    username = LineFromFile[:delimeter]
    print("Usermame: {}".format(username))

  
  def parsePasswdFile(self, filename='/etc/passwd'):
    try:
      userAns = int(input('Do you want to extract all the information or just the usernames ?\n\tGive 0 for Usernames\n\tGive 1 for All the Information\n: '))
      file = open(filename, 'r')
      for line in file:
        indexes = self.__findAll(':', line)
        if(userAns == 0):
          self.__extractUsernames(line)
        elif(userAns == 1):
          self.__extractInfo(indexes, line)
        else:
          print("Sorry, I don't understand your input. TRY AGAIN")
          sys.exit(0)
    except KeyboardInterrupt:
      print("\nThe Script Is Interrupted By The User")
    except IOError:
      print("\nSorry I couldn't open the file.\nPlease verify that the file exists or the name is correct")
    finally:
      file.close()


if(__name__ == "__main__"):
  try:
    filename = input('Enter the name of the file (default: /etc/passwd): ')
    if(filename == ''):
      filename = '/etc/passwd'
    
    parser = PasswdParser()
    parser.parsePasswdFile('test00')
  except KeyboardInterrupt:
    print("\nThe script is interrupted by the user")
  except Exception as var:
    print("Oops ! This problem has occured:\n{}".format(var))
else:
  print("This script is not supposed to be inserted as a module !")
    
