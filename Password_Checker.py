"""
Programa para revisar una contraseña y verficar si es la correcta o no, si prueba más de 3 veces ya no puede acceder
"""

intentos=0
password="Hercules69"
print("Bienvenido al sistema de autentificación")

while intentos>=0:

    rep_pass=input("Por favor coloque su contraseña para ingresar: ")

    if password==rep_pass:
        print("Entraste con éxito a tu cuenta")
        break

    if password!=rep_pass:
        intentos=intentos+1
        print("Contraseña incorrecta")
        print("\nPruebe nuevamente\n")
        
    if intentos==3 and password!=rep_pass:
        print("Has probado demasiadas veces, prueba dentro de 1 hora")
        break



"""                       
--..,_                     _,.--.
       `'.'.                .'`__ o  `;__.    
          '.'.            .'.'`  '---'`  `
            '.`'--....--'`.'
              `'--....--'`
"""
