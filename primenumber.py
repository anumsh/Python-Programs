def primeNumber(lower,upper):
  for num in range(lower,upper + 1):
   isprime=True
   if num >1:
       for checkprime in range(2,num/2):
           if (num % checkprime) == 0:
             isprime = False
             break
       if(isprime):
           print (num)
  return
           
primeNumber(30,80)
