def runEvent1(argument):
  if not(__name__ == '__main__'):
    from main import Event1
    try:
      Event1(argument)
    except TypeError:
      Event1()
def runEventadd(argument):
  if not(__name__ == '__main__'):
    from main import Eventaddd
    try:
      Eventaddd(argument)
    except TypeError:
      Eventaddd()
def runEventread(argument):
  if not(__name__ == '__main__'):
    from main import Eventread
    try:
      Eventread(argument)
    except TypeError:
      Eventread()
def runEventinit(argument):
  if not(__name__ == '__main__'):
    from main import Eventinit
    try:
      Eventinit(argument)
    except TypeError:
      Eventinit()
def runEventdelete(argument):
  if not(__name__ == '__main__'):
    from main import Eventdelete
    try:
      Eventdelete(argument)
    except TypeError:
      Eventdelete()
