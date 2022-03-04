# 📖 Présentation
`sprites` est une librairie Python, elle permet d'affichier des éléments sur l'écran de la [Galaxia](https://thingz.co/pages/galaxia-beta).
Vous pouvez l'installer en ajoutant le [dossier *sprites*](sprites) dans */GALAXIA/lib/*.

Pour programmer la carte, vous pouvez utiliser [l'interface en ligne](https://play.thingz.co/galaxia) et cliquer sur "Texte" ou le fichier *code.py* qui est dans votre Galaxia.

[**Télécharger la librairie**](https://github.com/Emilien-B/sprites/releases/tag/librarie)

[**Télécharger l'utilitaire d'image**](https://github.com/Emilien-B/sprites/releases/tag/utilitaire_image) ([voir ℹ️](https://github.com/Emilien-B/sprites#%E2%84%B9%EF%B8%8F))
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
sprite.color = 0xFFFF00 # modifie la couleur d'une icône ou d'une image
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

