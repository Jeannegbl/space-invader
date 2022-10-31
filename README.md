# Space Invaders

Exercice issu du site : [https://www.geeksforgeeks.org/building-space-invaders-using-pygame-python/](https://www.geeksforgeeks.org/building-space-invaders-using-pygame-python/)

Ce jeu est un classique des jeux vidéos, le joueur peut contrôller un vaisseau spacial. Il a la possibilité de se déplacer sur la gauche ou la droite. 
Et de tirer des missiles qui partent en ligne droite. 

Par défaut, les contrôles sont : 
 - La flèche gauche (permettant de déplacer le vaisseau à gauche)
 - La flèche droite (permettant de déplacer le vaisseau à droite)
 - La touche espace (permettant de tirer)
 
## Installation du projet
> pip install pygame

## Lancement de l'application 
> python main.py

## Les objectifs de cet exercice

Forkez ce dépôt, puis travaillez sur votre projet. L'url de votre dépôt devra être communiquée au formateur.
Pour chaque consigne donnée, concertez-vous afin de savoir ce qui est à réaliser puis implémentez la solution. 
Réalisez un commit pour chaque fonctionnalité mise en place. 

### Problème de vitesse
Vous devriez rapidement réaliser que le jeu est actuellement injouable. En effet, il est bien trop rapide. 
Ce jeu a été implémenté en utilisant une bibliothèque externe nommée `pygame`.

Allez voir la [documentation officielle de pygame](https://www.pygame.org/docs/ref/time.html#pygame.time.Clock) afin de voir la documentation de l'objet Clock. 
Il permettra de pouvoir ajuster la boucle infinie afin qu'elle s'adapte à un FPS demandé.



Il va donc faloir rajouter : 
```python
    clock = pygame.time.Clock()
    # puis au sein de la boucle
    while True:
        # ...
        clock.tick(60) # Approcher le 60 FPS
```

### Les objectifs suivants  
- **Changer le mapping du clavier**

Changer la touche espace  avec le click souris. 
Et le déplacement avec les lettres **ZQSD**

- **Modifiez les ennemis**

Changez le sprite associé aux ennemis et passez le nombre d'ennemis à 13.

- **Restructurez le code**

Plusieurs tableaux sont actuellement mis en place pour gérer les ennemis. 
Refactorez le code afin que l'ensemble des informations liées aux ennemis au sein d'une même classe.

- **Il est possible de terminer un niveau**
Faites en sorte de pouvoir tuer les ennemis. Lorsqu'un ennemi est tué, une petite animation doit avoir lieu et l'ennemi disparaître.

- **Pouvoir tirer plusieurs balles simultanément**

Un autre objet serait à mettre en place et s'est les balles. Créez ce nouvel objet et laisser l'utilisateur avoir la possibilité de tirer plusieurs balles à la fois. 

- **Réalisez un écran de fin** 

Si tous les ennemis sont tués, l'application doit afficher un score final.
 Le score sera basé sur le temps total mis pour tuer les ennemis. 

- **Ajoutez un premier écran d'interface**

Ce dernier permettra de définir : 
- Le nombre d'ennemis
- Les touches du clavier
- De lancer une partie
- D'afficher les derniers scores