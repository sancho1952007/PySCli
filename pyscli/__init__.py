import sys
num=0
def cli(*argv, sensitive):
  global num
  for args in argv:
    if sensitive!=False:
      if args in ' '.join(sys.argv[1:]):
        num += 1
    
      else:
        None
    else:
      if args.lower() in ' '.join(sys.argv[1:]).lower():
        num += 1
    
      else:
        None
  if num==len(argv):
      return True
  else:
      return False
