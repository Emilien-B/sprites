Lors d'un stage chez [Thingz](https://thingz.co/) j'ai pu contribué à la création d'une librairie pour leur carte [Galaxia](https://thingz.co/pages/galaxia-beta). La carte sort bientôt.

# 📖 Présentation
`sprites` est une librairie Python, elle permet d'affichier des éléments sur l'écran de la 
Vous pouvez l'installer en ajoutant le [dossier *sprites*](sprites) dans */GALAXIA/lib/*.

Pour programmer la carte, vous pouvez utiliser [l'interface en ligne](https://play.thingz.co/galaxia) et cliquer sur "Texte" ou le fichier *code.py* qui est dans votre Galaxia.

[**Télécharger la librairie**](https://github.com/Emilien-B/sprites/releases)

[**Télécharger l'utilitaire d'image**](https://github.com/Emilien-B/sprites/tree/main/utilitaire_image)
# ⚙️ Utilisation

💾 Importer la libraire :
```python3
import sprites
```
Les différents types de sprite de la librarie sont [`rectangle`](https://github.com/Emilien-B/sprites#-rectangle), [`icon`](https://github.com/Emilien-B/sprites#%EF%B8%8F-icon) et [`image`](https://github.com/Emilien-B/sprites#-image).

## 🟨 Rectangle
On commence par créer un rectangle et le stocker dans une variable (ici `sprite`). 
```python3
sprite = sprites.rectangle(x=0, y=0, color=0xFF0000, width=20, height=20, scale=1, hidden=False)
```
Vous pouvez définir de nombreux arguments:

**x et y** : position du rectangle (en nombres entiers)

**color** : couleur du rectangle (en [hexadécimal](https://htmlcolorcodes.com/))

**width et height** : longueur et hauteur du rectangle (en nombres entiers) (non modifiable)

**scale** : échelle du rectangle, elle multiplie les dimensions du rectangle (en nombre entier supérieur ou égal à 1)

**hidden** : si le rectangle est caché, lorsque cette variable est à `False` le rectangle est visible (en booléen, `True` ou `False`)

<img src="https://cdn-learn.adafruit.com/assets/assets/000/074/495/large1024/circuitpython_coord_sys.png?1555378384" width="300"></img>


## ♥️ Icon
On commence par créer une image et la stocker dans une variable (ici `sprite2`).

```python3
sprite2 = sprites.icon(x=0, y=0, scale=1, name="cross", color=0xFFFFFF, hidden=False)
```
**x et y** : position de l'icône (en nombres entiers)

**scale** : échelle de l'icône, elle multiplie les dimensions de l'image (en nombre entier supérieur ou égal à 1)

**name** : nom de l'icône, il peut être : "cross", "circle", "heart" ou "emoji" (non modifiable)
[Comment ajouter ses propres icônes ?](https://github.com/Emilien-B/sprites#%E2%84%B9%EF%B8%8F)


**color** : couleur de l'icône (en [hexadécimal](https://htmlcolorcodes.com/))

**hidden** : si l'icône est caché, lorsque cette variable est à `False` l'icône est visible (en booléen, `True` ou `False`)

## 🌅 Image 
On commence par créer une image et la stocker dans une variable (ici `sprite3`).
```python3
sprite3 = sprites.image(x=0, y=0, scale=1, path="/thingz.bmp", hidden=False)
```
**x et y** : position de l'image (en nombres entiers)

**scale** : échelle de l'image, elle multiplie les dimensions de l'image (en nombre entier supérieur ou égal à 1)

**path** : chemin du fichier en .bmp à l'intérieur de la Galaxia (non modifiable)

**hidden** : si l'image est caché, lorsque cette variable est à `False` l'image est visible (en booléen, `True` ou `False`)

## ℹ️ 
>Afin de sauvegarder une image dans la Galaxia dans le bon format, les bonnes dimensions, les bonnes couleurs... 
>Vous pouvez utiliser [l'utilitaire d'image Galaxia](https://github.com/Emilien-B/sprites/tree/main/utilitaire_image).
>
> Si vous souhaiter ajouter une icône il faut qu'elle soit blanche sur fond noir et en 20x20, puis, il faut la déplacer dans */GALAXIA/lib/sprites/icons/* .

## Autres commandes


Tous les attributs peuvent être récupérés. 

Exemples:
```python3
sprite.x 
>>> 30 # valeur x de sprite
sprite.name 
>>> "emoji" # nom de l'icône utilisée
```
Presque tous les attributs sont modifiables (hormis ceux marqués "non modifiable").

Exemples:
```python3
sprite.x += 10 # déplace le sprite vers la droite
sprite.color = 0xFFFF00 # modifie la couleur d'une icône
```
Renvoie `True` si les deux sprites fournis sont en collision.
```python3
sprites.collision(sprite,sprite2)
```
Renvoie `True` si le sprite fourni est en collision avec la bordure du haut (north).
`border` peut être "n"(north), "s"(south), "w"(west) ou "e"(east).
```python3
sprites.border_collision(border="n",sprite)
```
Indique la version.
```python3
sprites.version()
```

# 🗄 Exemples
### 1• Exemple d'affichage des éléments

<details>
  <summary>⌨️ Voir le code
  </summary>

```python3
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
```

</details>

<details>
  <summary>🎥 Voir la vidéo
  </summary>

https://user-images.githubusercontent.com/59746560/158021351-8c2e5e3c-5c90-458e-ab8a-b561a26bebf9.mov

</details>


[ 📂 **Accéder aux fichiers**](https://github.com/Emilien-B/sprites/tree/main/exemples/exemple1)


### 2• Exemple de déplacement d'un sprite

<details>
  <summary>⌨️ Voir le code
  </summary>

```python3
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

```

</details>

<details>
  <summary>🎥 Voir la vidéo
  </summary>

https://user-images.githubusercontent.com/59746560/158021570-7a8d26ca-97bb-4dec-91f1-ba46e96ed60d.mov

</details>


[ 📂 **Accéder aux fichiers**](https://github.com/Emilien-B/sprites/tree/main/exemples/exemple2)

# 📎 Autres...


### 🖥 Mon compte Twitter

<img src="https://pbs.twimg.com/profile_banners/815889012162437120/1613380165/1500x500" alt="" width="300"/>

**[twitter.com/emilien_barde](https://twitter.com/emilien_barde)**

### 💰 Me soutenir
**[paypal.com/emilienb31](https://www.paypal.com/paypalme/emilienb31)**

### 📚 Documentation

**[Documentation de la librarie sur laquelle je me suis basé](https://docs.circuitpython.org/en/latest/shared-bindings/displayio/)**

**[FAQ sur la Galaxia](https://doc.clickup.com/d/h/2g0zm-1688/80aeb3d8ff62efa/2g0zm-788)**
