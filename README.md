# Projet de comptage d'objets #

### Ce projet vise à compter les objets (en particulier les voitures) dans une vidéo en utilisant le modèle YOLOv8. Le modèle YOLO (You Only Look Once) est un réseau de neurones convolutifs utilisé pour la détection en temps réel d'objets. Ici, nous utilisons un modèle pré-entraîné pour détecter et suivre les voitures, puis comptabiliser les objets passant une ligne définie dans la vidéo. ###

### Structure du Projet ###
### Chargement du Modèle et Configuration : ###

- Le modèle YOLOv8 pré-entraîné (yolov8n.pt) est chargé pour la détection d'objets.
- Une vidéo d'entrée (object_counting.mp4) est ouverte pour le traitement.
- La ligne de comptage et les classes d'objets à compter sont définies.

### Traitement de la Vidéo et Comptage des Objets : ###
- La vidéo est lue cadre par cadre.
- Les objets détectés sont suivis et comptés lorsqu'ils traversent la ligne de comptage.
- Les résultats sont affichés et sauvegardés dans une nouvelle vidéo de sortie.

### Fichiers et Répertoires ###
- yolov8n.pt : Fichier du modèle YOLOv8 pré-entraîné.
- object_counting.mp4 : Vidéo d'entrée contenant les objets à compter.
- object_counting_output.avi : Vidéo de sortie avec les résultats du comptage des objets.
