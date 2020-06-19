import random

while True:
  print ("MAX PASSWORD LENGTH IS 10 To 15")
  
  x =int(input("TYPE YOUR PASSWORD LENGTH IN NUMBER :"))
  
  if x<=9:
  	print("PLEASE INPUT A LENGTH BETWEEN 10 TO 15")
  	
  if x>15:
  	print("PLEASE INPUT A LENGTH BETWEEN 10 TO 15")
 
 
  
  	


  _words = ["1","2","3","4","5","6","7","8","9","0","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","@","#","$","%","&","_","+","×","₹","!","=","A","B","c","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

  random.shuffle(_words)

  if x == 10:
	  g = _words[10:20]
	  random.shuffle(g)
	  raw_pass = "YOUR PASSWORD:            -----------               {}{}{}{}{}{}{}{}{}{}". format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9])
	
	  print (raw_pass)
	
  if x == 11:
	  g =   _words[10:21]
	  random.shuffle(g)
	  raw_pass = "YOUR PASSWORD:             ---------              {}{}{}{}{}{}{}{}{}{}{}". format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10])
	  print(raw_pass)
	

  if x == 12:
	  g =   _words[10:22]
	  random.shuffle(g)
	  raw_pass = "YOUR PASSWORD:            ----------               {}{}{}{}{}{}{}{}{}{}{}{}". format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11])
	  print(raw_pass)
	

  if x == 13:
	  g = _words[10:23]
	  random.shuffle(g)
	  raw_pass = "YOUR PASSWORD:            ----------               {}{}{}{}{}{}{}{}{}{}{}{}{}". format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11],g[12])
	  print(raw_pass)
	
  if x == 14:
	  g = _words[10:24]
	  random.shuffle(g)
	  raw_pass = "YOUR PASSWORD:           ----------                {}{}{}{}{}{}{}{}{}{}{}{}{}{}". format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11],g[12],g[13])
	  print(raw_pass)
	
  if x == 15:
	  g = _words[10:25]
	  random.shuffle(g)
	  raw_pass = "YOUR PASSWORD:         -------------                  {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}". format(g[0],g[1],g[2],g[3],g[4],g[5],g[6],g[7],g[8],g[9],g[10],g[11],g[12],g[13],g[14])
	  print(raw_pass)
	