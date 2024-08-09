import random
import time

hp_deadpool = 580
hp_wolverine = 500
hit_deadpool = random.randint(10 ,99)
hit_wolverine = random.randint(10,119)
aux_hit_dp = 0
aux_hit_wv = 0
turno = 1

print("Hp Deadpool:", hp_deadpool)
print("Hp Wolverine:", hp_wolverine)

while hp_deadpool > 0 and hp_wolverine > 0:
    print("")

    print("Turno:", turno)

    if aux_hit_wv != 120:        
        if random.randint(0,100) <= 80:
            print("Deadpool ha hecho %d de daño." %hit_deadpool)
            hp_wolverine -= hit_deadpool
        else: print("Deadpool ha fallado el golpe.")
        print("Hp Wolverine:", hp_wolverine)
    else: 
        print("Deadpool se está recuperando.")
        print("Hp Wolverine:", hp_wolverine)
        aux_hit_wv = 0

    if aux_hit_dp != 100:        
        if random.randint(0,100) <= 80:
            print("Wolverine ha hecho %d de daño." %hit_wolverine)
            hp_deadpool -= hit_wolverine
        else: print("Wolverine ha fallado el gople.")
        print("Hp Deadpool:", hp_deadpool)
    else:
        print("Wolverine se está recuperando.")
        print("Hp Deadpool:", hp_deadpool)
        aux_hit_dp = 0

    aux_hit_dp = hit_deadpool
    aux_hit_wv = hit_wolverine
    hit_deadpool = random.randint(10, 100)
    hit_wolverine = random.randint(10, 120)

    time.sleep(1)
    turno += 1

print("---------------------------------------")
if hp_deadpool <= 0 and hp_wolverine <= 0: print("Doble KO!")
elif hp_wolverine <= 0: print("El ganador es Deadpool!")
else: print("El ganador es Wolverine!")
print("---------------------------------------")
