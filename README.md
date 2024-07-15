# tuto_django

## Quand utiliser include()
>Il faut toujours utiliser include() lorsque l’on veut inclure d’autres motifs d’URL. admin.site.urls est la seule exception à cette règle.

`$ python manage.py runserver`

>Par défaut, INSTALLED_APPS contient les applications suivantes, qui sont toutes contenues dans Django :

django.contrib.admin – Le site d’administration. Vous l’utiliserez très bientôt.
django.contrib.auth – Un système d’authentification.
django.contrib.contenttypes – Une structure pour les types de contenu (content types).
django.contrib.sessions – Un cadre pour les sessions.
django.contrib.messages – Un cadre pour l’envoi de messages.
django.contrib.staticfiles – Une structure pour la prise en charge des fichiers statiques.

>$ python manage.py migrate