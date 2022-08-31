"""
You are going back home after a hard-working day, and a fundamental question is asked to you : What can I eat tonight ?

You are tired to open your fridge every evening and asking the same question, so you decide to create a program which will give you all possible recipes you can cook with foods you have.
Input
Line 1: an integer N for the number of different food you have in your fridge

N next lines : Strings coresponding to the names of the different foods you have in your fridge

next line an integer P for the number of recipes than you know

P next lines : Strings (comma-separated) where the first input corresponds to the name of the recipe, and next inputs correspond to the foods needed to cook the recipe.
Output
X lines : Strings corresponding to the cookable recipes, if no recipe can me cooked, just write "FASTFOOD JOKER"

Output recipes must be given in the same order they have been reading in the standards inputs.
Constraints
1<N<100
1<P<100
1<X<100
Example
Input
4
Poulet
Vin blanc
Bouillon de poule
Moutarde
2
Poulet moutarde,Poulet,Moutarde,Vin blanc,Bouillon de poule
Risotto au chorizo,Riz,Chorizo,Bouillon de poule,Vin blanc,Poivron
Output
Poulet moutarde

INPUT:
22
Poulet
Citron vert
Basilic
Bouillon de poule
Conserve perimee
Pates
Huile de noisette
Biere
mozzarella
Cognac
Vin blanc
Sucre
Beurre
Chapelure
Ail
Bicarbonate de soude
Oignon blanc
Moutarde
Calvados
Riz
Poivron
Pignons de pin
4
Poulet moutarde,Poulet,Moutarde,Vin blanc,Bouillon de poule
Risotto au chorizo,Riz,Chorizo,Bouillon de poule,Vin blanc,Poivron
Pates au sucre,Pates,Sucre
Pates au beurre,Pates,Beurre

OUTPUT:
Poulet moutarde
Pates au sucre
Pates au beurre

INPUT:
19
Bicarbonate de soude
Biere
Chapelure
Cheddar
Cidre
Clous de girofle
Coca Vanille
Conserve perimee
Croutons
Gencives de porc
Gousse d'ail
Gras double
Machoir d'ane
Moutarde
Pain hamburger
Pied de veau
Pignons de pin
Sel
Sucre
4
Pates au sel,Pates,Sel
Pates au beurre,Pates,Beurre
La specialite du chef,Ketchup,Coca Vanille,Pied de veau,Gencives de porc,Machoir d'ane,Parmesan
Soupe au lait,Lait,Sucre,Pain

OUTPUT:
FASTFOOD JOKER

INPUT:
8
Pates
Oeuf
Parmesan
Coca Vanille
Conserve perimee
Ketchup
Jambon
Emmental
21
Poulet moutarde,Poulet,Moutarde,Vin blanc,Bouillon de poule
Risotto au chorizo,Riz,Chorizo,Bouillon de poule,Vin blanc,Poivron
Trippes a la motte de Caen,Pied de veau,Gras double,Cidre,Carrotte,Oignon blanc,Calvados
Omelette aux champignons,Oeuf,Champignon
Croque monsieur,Pain de mie,Jambon,Emmental
Croque madame,Pain de mie,Jambon,Emmental,Oeuf
Hamburger,Pain hamburger,Steack hache,Cheddar,Oignon rouge,Salade verte
Salade cesar,Salade verte,Poulet frit,Croutons,Parmesan
Galette bretonne,Crepe au sarazin,Oeuf,Jambon,Emmental,Champignon
Carbonara,Pates,Oeuf,Parmesan
Quiche au saumon,Saumon,Boursin,Pate a tarte,Oeuf,Epinard
Cordon bleu,Poulet,Jambon,Emmental
Pates fraiches au foie gras et aux morceaux de truffes,Beurre,Huile d'olive,Tagliatelles fraiches,Tranches de magret de canard,Pelures de truffes,Foie gras de canard mi-cuit,Basilic
Homard grille sabayon au champagne,Homard femelle,Beurre,Jus de citron,Champagne brut,Estragon,Oeuf
Veloute de cepes et chateignes,Chateignes cuites,Beurre,Lait,Creme champetre,Gousse d'ail,Muscade,Huile de noisette,Pignons de pin,Echalotte,Cepes
Fricassee de noix de saint jacques aux champignons de Paris,Noix de Saint Jacques,Creme fraiche epaisse,Champignons de Paris,Beurre,Cognac
Tartare de bar au gingembre,Concombre,Gingembre,Huile d'olive,Bar,Citron vert
Consomme de faisan aux cepes et aux quenelles a la moelle,Faisan,Carotte,Celeri,Bouquet garni,Oignon,Clous de girofle,Boeuf,Poireaux,Tomate,Ail,Cepes
Gratin de legumes du soleil,Pomme de terre,Courgette,Tomate,Creme fraiche,mozzarella
Tartiflette,Reblochon,Pomme de terre,Lardons,Oignon blanc,Ail
Parmentier de canard,Pomme de terre,Confit de canard,Oignon blanc,Huile d'olive,Chapelure

OUTPUT:
Carbonara


"""


n = int(input())
l=[]
for i in range(n):
    av = input()
    l.append(av)
p = int(input())
res=0
for i in range(p):
    nb=1
    recipe = input().split(",")
    for j in recipe[1::]:
        if j not in l:
            nb=0
    if nb==1:
        print(recipe[0])
        res+=1
if res == 0:
    print("FASTFOOD JOKER")