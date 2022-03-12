# Importer les librairies
from thingz import accelerometer
import time
import sprites

# Créer un rectangle
sprite = sprites.rectangle(x=30,y=40,color=0xffff00, width=20, height=20 )

# Répéter indéfiniment
while True:

    # Si l'accéléromètre penche vers le bas et que le carré de touche pas le bas de l'écran
    if accelerometer.get_y() > 150 and not sprites.border_collision('s',sprite):
        # Déplacer le sprite vers le bas
        sprite.y += 1
    
    # Si l'accéléromètre penche vers le haut et que le carré de touche pas le haut de l'écran
    if accelerometer.get_y() < 150*-1 and not sprites.border_collision('n',sprite):
        # Déplacer le sprite vers le haut
        sprite.y -= 1 
    
    # Si l'accéléromètre penche vers la droite et que le carré de touche pas la droite de l'écran
    if accelerometer.get_x() > 150 and not sprites.border_collision('e',sprite):
        # Déplacer le sprite vers la droite
        sprite.x += 1
    
    # Si l'accéléromètre penche vers la gauche et que le carré de touche pas la gauche de l'écran
    if accelerometer.get_x() < 150*-1 and not sprites.border_collision('w',sprite):
        # Déplacer le sprite vers la gauche
        sprite.x -= 1

    # Attendre 0,005s
    time.sleep(0.005)
