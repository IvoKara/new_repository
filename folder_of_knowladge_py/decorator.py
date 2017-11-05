def decor(func):        #decorator
  def wrap():
    print("============")
    func()
    print("============")
  return wrap
@decor
def print_text():
  print("Hello world!")

##print_text()
##@decor == print_text = decor(print_text)
print_text()
