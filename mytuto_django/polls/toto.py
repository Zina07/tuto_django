
prenom = "zina"
text = f"lala je m'appelle {prenom} et j'adore django"


# Template
template="""
...
{for id in lala}
href="{% zina id=id %}"
{ endfor }
...
"""

# Urls.py
"""
...
path(/polls/:id, name=zina)
...
"""