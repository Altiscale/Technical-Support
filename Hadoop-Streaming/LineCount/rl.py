#!./py279/bin/python
import sys
def main():
  sum = 0
  for line in sys.stdin:
    sum+=1
  print "%s" % sum
if __name__=='__main__':
  main()
