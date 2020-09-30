from password import User
from password import Credentilas

def new_user(username, passwords):
  """
  creates a new user
  """
  new_user = User(username, passwords)
  return new_user

def save_user(user):
  """
  save created user
  """
  user.save_user()

def create_account(sitename, accountname, password):
  """
  creating account details
  """
  new_account = Credentilas(sitename, accountname, password)
  return new_account

def save_account(password):
  """
  saving account details
  """
  password.save_account()

def delete_accounts(password):
  """
  deleting account details
  """
  password.delete_account()

def display_account_details():
  """
  displays saved account details
  """
  return Credentilas.display_account()

def main():
  """
  main functions called here
  """
  print("--PASSWORD LOCKER APP :)--")
  print("Tip Create an account first")
  print("What's your name?")
  user_name = input()
  print(f"Hey {user_name}. Would you like to create an account?")
#   print("\n")

  while True:
    print("Use these codes to make requests:")
    print("+- add user account")
    print("create- create an account")
    print(" del - delete and account")
    print("view- view account details")
    short_code = input().lower()

    if short_code == "+":
      print("USER ACCOUNT")
      print ("Enter USERNAME")
      username = input()
      print ("Enter NEW USER password")
      passwords = input()
      save_user(new_user(username, passwords))
      print("User account {username} successfully created")
      print("The next step is to save specific account details")
      print("ACCOUNT DETAILS")
      print ("Enter ACCOUNT name:")
      accountname = input()
      print("Enter PASSWORD")
      password = input()
      save_account(create_account(sitename, accountname, password))

    elif short_code == "create":
      print ("Enter site name")
      sitename = input()
      print ("Enter account name:")
      accountname = input()
      print("Enter password")
      password = input()
      save_account(create_account(sitename, accountname, password))

    elif short_code == "view":
      if display_account_details():
        for account in display_account_details():
          print(f"{sitename}, {accountname}, {password}")
      else: print("No accounts available")
    elif short_code == "del":
      delete_accounts(save_account)

if __name__ == "__main__":
  main()