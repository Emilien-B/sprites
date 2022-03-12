# Importer les librairies
import sprites 
import time

# Créer un rectangle
forme = sprites.rectangle(x=15, y=40, color=0x00FFFF, width=20, height=50, scale=1, hidden=False)

# Créer une icône de coeur
coeur = sprites.icon(x=110, y=55, scale=1, name="heart", color=0xFF0000, hidden=False)

# Créer les images de l'animation
anim1 = sprites.image(x=50,y=30,path="/walk1.bmp", hidden=True)
anim2 = sprites.image(x=50,y=30,path="/walk2.bmp", hidden=True)
anim3 = sprites.image(x=50,y=30,path="/walk3.bmp", hidden=True)
anim4 = sprites.image(x=50,y=30,path="/walk4.bmp", hidden=True)

# Mettre les images de l'animation dans une liste
anims = [anim1,anim2,anim3,anim4]

# Alterner indéfiniment entre cacher et montrer les images
while True:
    for anim in anims:
        anim.hidden = False
        time.sleep(0.3)
        anim.hidden = True