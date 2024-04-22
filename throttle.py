import time
from functools import wraps

class CoolDownDecorator(object):
  def __init__(self,func,interval):
    self.func = func
    self.interval = interval
    self.last_run = 0
  def __call__(self,*args,**kwargs):
    now = time.time()
    if now - self.last_run < self.interval:
      print('---skipped--')
    else:
      self.last_run = now
      return self.func(*args,**kwargs)

def CoolDown(interval):
  def applyDecorator(func):
    decorator = CoolDownDecorator(func=func,interval=interval)
    return wraps(func)(decorator)
  return applyDecorator
