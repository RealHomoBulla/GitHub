'''Task 1
Create a class method named `validate`, which should be called from the `__init__` method to validate parameter email,
passed to the constructor. The logic inside the `validate` method could be to check
if the passed email parameter is a valid email string.'''

# Lists of prohibited symbols.
global punctuations
punctuations = ' !()[]{};:\/\'",<>?#$%^&*~'
# Also 2 special symbols in a row can't be used.
global limited_symbols
limited_symbols = ['..','.-', '._', '-.', '_.', '--', '__', '-_', '_-']

class Validate:

  def __init__(self, email):
    self.email = email
    # If email has not passed validation, it will be overriden to "Invalid Email".
    if not self.final_validation():
      self.email = f'Invalid Email: "{email}"'

  # Checks every possible type of validation. All of them should be True, then it returns True and email will not be
  # overriden to Invalid.
  def final_validation(self):
      if self.email_check() and self.prefix_check() and self.etta_check() and self.domain_check():
        # This will print correct email, if it was accepted.
        print(f'Your Email accepted: "{self.prefix}@{self.etta}.{self.domain}"')
        return True
      return False

  def email_check(self):

    # Type should be string.
    if type(self.email) is not str:
      print('You passed a wrong type of data.')
      return False

    # First symbol should not be a dot or special symbol, it should be a number or a letter.
    if not self.email[0].isalnum():
      print('Email should start with letter or number.')
      return False

    # If any prohibited symbols is used, email is invalid
    count = 0
    for char in self.email:
      if char in punctuations:
        print(f'Not valid email. "{char}" is not allowed.')
        return False
      # It should check, that there is exactly one "@" symbol. Not less, not more.
      elif char == '@':
        count += 1
    if count != 1:
      print('Not valid email.')
      return False

    # If in any point, 2 special symbol are in a row, it should be Invalid.
    for pair in limited_symbols:
      if pair in self.email:
        print('You can\'t use two special symbols in a raw.')
        return False

    # Now email is splitted on 3 parts - prefix is everything before "@",
    self.prefix = self.email.split('@')[0]
    # Rest is everything after "@", which then will be splitted again.
    self.etta = self.email.split('@')[1]

    # Now we check, that in domain name there is at least one dot (".").
    count = 0
    for char in self.etta:
      if char == '.':
        count += 1
    if count < 1:
      print('Domain name is wrong.')
      return False

    # Then we split again by the first dot. It can be like @ukho.gov.uk-> "ukho" should be separated.
    self.etta = self.etta.split('.')[0]
    # Then it separates "gov.uk" because it is a domain name.
    self.domain_list = self.email.split('.')[1:]
    for item in self.domain_list:
      # We join back the domain.
      self.domain = '.'.join(self.domain_list)
      # Domain name less than 2 symbols are not acceptable.
      if len(item) < 2:
        print('Very short sub-domain name.')
        return False
    # If it's all good, we get the accepted general email, but then we'll check prefix and domain for special cases.
    return True

  # Now we will check  prefix.
  def prefix_check(self):

    # Max length for the prefix is 64 characters.
    if len(self.prefix) >= 64:
      print('Your prefix (part before "@" symbol) can\'t be longer than 64 characters.')
      return False

    # Min length for the prefix is 3 characters
    if len(self.prefix) <= 3:
      print('Your prefix (part before "@" symbol) can\'t be shorter than 3 characters.')
      return False

    # Prefix should not end with a special symbol, only with a letter or a number.
    if self.prefix[-1] in '-_.':
      print('Last symbol should be a letter or number.')
      return False
    # If all conditions met, we passed this check, returns True.
    return True


  def etta_check(self):

    # First symbol should not be a special symbol, only a letter or a number.
    if self.etta[0] in '-_':
      print('First symbols should be letter or numbers.')
      return False

    # Min length for this part is 2 characters
    if len(self.etta) < 2:
      print('Your domain (part after "@" symbol) can\'t be shorter than 2 characters.')
      return False

    # Max length for this part is 64 characters.
    if len(self.etta) > 64:
      print('Your domain (part after "@" symbol) can\'t be longer than 64 characters.')
      return False
    # If all conditions met, we passed this check, returns True.
    return True


  def domain_check(self):

    # Min length for the domain is 2 characters
    if len(self.domain) < 2:
      print('Your domain (part after "." symbol) can\'t be shorter than 2 characters.')
      return False

    # Domain can conntain only letters and dots, no any numbers or special symbols.
    for char in self.domain:
      if char in '-_1234567890':
        print('Domain can contain only letters and dots.')
        return False

    # Domain should end with letter, not a dot.
    if self.domain[-1] == '.':
      print('Email can\'t end with a dot.')
      return False
    # If all conditions met, we passed this check, returns True.
    return True


correct_mail = Validate('fds-lj@gih.com.gov.ua')
print(correct_mail.email)

print()

wrong_mail = Validate('fds-lj-@gih.com.gov.ua')
print(wrong_mail.email)
