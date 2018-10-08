def armstrong (n):
 sum=0
 t=n
 while (t>0):
  d=t%10
  sum+=digit**3
  t=t//10
 return sum

