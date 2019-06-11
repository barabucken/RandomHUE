import random
import time

init = 0

while True:
    scolor = random.randrange(3)
    
    if scolor == 0:
      r = random.randrange(0,128)
    else:
      r = random.randrange(127,256)

    if scolor == 1:
      g = random.randrange(0,128)
    else:
      g = random.randrange(127,256)

    if scolor == 2:
      b = random.randrange(0,128)
    else:
      b = random.randrange(127,256)


    if init == 1:
      print("Starting run")
      print(r,g,b)
      print(oldr,oldg,oldb)
      print()
      if r > oldr:
        changer = r - oldr
      else:
        changer = oldr - r

      if g > oldg:
        changeg = g - oldg
      else:
        changeg = oldg - g

      if b > oldb:
        changeb = b - oldb
      else:
        changeb = oldb - b
          
      for x in range(10):

        if oldr > r:
          oldr = oldr - (changer / 10)
        else:
          oldr = oldr + (changer / 10)

        if oldg > g:
          oldg = oldg - (changeg / 10)
        else:
          oldg = oldg + (changeg / 10)
      
        if oldb > b:
          oldb = oldb - (changeb / 10)
        else:
          oldb = oldb + (changeb / 10)

        print(round(oldr), round(oldg), round(oldb))
         
      oldr = int(round(oldr))
      oldg = int(round(oldg))
      oldb = int(round(oldb))
  
    if init == 0:
      init = 1
      oldr = r
      oldg = g
      oldb = b
    
    time.sleep(5)
    


