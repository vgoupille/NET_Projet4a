Projet_NET 

Csardi, G., & Nepusz, T. (2006). The igraph software package for complex network research. InterJournal, Complex Systems, 1695.

Bonjour,
J’espère que vous avez pu jouer un peu avec des graphes « simples » de votre côté avant d’avoir accès aux gros graphes que nous vous avons promis en NET.
Vous pourrez les télécharger ici :
 
Attention : je vous conseille fortement de tester un peu vos méthodes avec des petits graphes ou avec les graphes HSA-… (qui sont plus petits et illustrés par des grandes images au cas où vous voulez savoir à quoi ils ressemblent), avant de jouer avec le gros graphe global.
On en reparle quand vous avez réussi à prendre ça en main.
Indication : vous avez un graphe au format .graphml (http://graphml.graphdrawing.org/ ou https://fr.wikipedia.org/wiki/GraphML), ça se lit avec :
- la librairie yED 
- avec networkX  : https://networkx.org/documentation/stable/reference/readwrite/generated/networkx.readwrite.graphml.read_graphml.html,

- avec igraph https://igraph.org/python/doc/api/igraph.Graph.html#Read_GraphMLz
Je vous conseille d’utiliser networkx, mais ce n’est pas une obligation.


library a installer :
 pip install igraph
 pip install networkx

pip install pyyed #A simple Python library to export graphs to the yEd graph editor

pip install yfiles_jupyter_graphs #yFiles Graphs for Jupyter is a free diagram visualization extension for JupyterLab and Jupyter Notebook. You can easily load structures from your favorite Python graph package and benefit from the superior visualization and automatic layouts of our established yFiles SDK.