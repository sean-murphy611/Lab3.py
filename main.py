# Sean Murphy spm6407@psu.edu
# Yon Lin Kwang yqk5211@psu.edu 
# Aidan Mayo ajm8132@psu.edu 
#Section 1
#Breakout 8

def sum_n(n):
  if n<=1:
    return 1
  else:
    return n + sum_n(n-1)

def print_n(s,n):
  if n<=1:
    print(s)
  else:
    print(s)
    print_n(s,n-1)

def run():
  n = int(input("Enter an int: "))
  out = sum_n(n)
  print("sum is " + str(out)+ ".")
  s = input("Enter a string: ")
  print_n(s,n)

if __name__ == "__main__":
  run()