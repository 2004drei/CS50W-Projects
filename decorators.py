def announce(f):
  def wrapper():
    print("Function is about to run...")
    f()
    print("Function is done.")
  return wrapper

@announce
def hello():
  print("Hello World")

hello()