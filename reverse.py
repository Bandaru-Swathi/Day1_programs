n=input("enter n=");
temp=n;
rev=0;
while (n>0):
	digit=n%10;
	rev=digit+(rev*10);
	n=n/10;
if (rev==temp):
	print temp,"is Palindrome"
else:
	print temp,"is not Palindrome"
print "the Reversed no.is",rev
