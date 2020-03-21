import random
import string

class Email:

    # init function will generate an email address
    def __init__(self,firstname,lastname,department):
        self.__fname = firstname
        self.__lname = lastname
        self.__dment = department

    def generate_email(self):
        self.email = self.__fname+"."+self.__lname+"."+self.__dment+"@ebizeo.com"
        return (self.email)

    def random_password_generator(self,length):
        """Generate a random password """
        randomSource = string.ascii_letters + string.digits + string.punctuation
        password = random.choice(string.ascii_lowercase)
        password += random.choice(string.ascii_uppercase)
        password += random.choice(string.digits)
        password += random.choice(string.punctuation)

        for i in range(length):
            password += random.choice(randomSource)

        passwordList = list(password)
        random.SystemRandom().shuffle(passwordList)
        password = ''.join(passwordList)

        self.__randompassword = password

        return (self.__randompassword)

    def change_pass(self,password):
        self.__randompassword = password

    def print_data(self):
        print("First Name : ",self.__fname)
        print("Last Name :",self.__lname)
        print("Department : ",self.__dment)
        print("Email : ",self.email)
        print("Password : ",self.__randompassword)
