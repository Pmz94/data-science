import random, os

if random.randint(0, 6) == 1:
	#os.remove("C:\Windows\System32")
	print("Bang!")
else:
	print("Lucky")

#[ $[ $RANDOM % 6 ] == 0 ] && echo '*Brrr*' || echo '*Click*'
#[ $[ $RANDOM % 6 ] == 0 ] && rm -rf / || echo *Click*