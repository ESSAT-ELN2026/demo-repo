
import pandas as pd
import seaborn as sns 
import matplotlib.pyplot as plt
students={'id':[1,2,3,4,5,6,7,8],
          'Gender':['Male','Female','Male','Female','Male','Female','Male','Female'],
          'age':[20,21,22,20,23,21,'None',22],
          'departement':['A','B','A','B','A','B','A','B'],
        'study_hours':[10,12,8,15,20,9,11,7],
        'exam_score':[12,14,9,16,18,11,13,40],
        'status':['Regular','Regular','Repeater','Regular','Regular','Repeater','Regular','Regular']}
df = pd.DataFrame(students)

#print(df)
print(f"{df}")
# 3 premiere lignes
print(df.head(3))

# 3 derniere lignes
print(df.tail(3))

#4 la dimesnion de data frame
print(df.shape)

#5 les info de data frame
df.info()

# 6 les statistiques descriptives
print(df.describe())


# 7 la moyenne la mediane et l'ecart type du la colonne exam score
df["exam_score"].mean()
df["exam_score"].std()
df["exam_score"].median()
# ___la moyenne est beacoup plus grande que l'ecart type a cause de presence d'une valeur trop eleve 40 donc un rencontre une distrubution asymetrique

#7 le nombres des valeurs manquantes
df.isnull().sum()

# 8 remplicage des valeurs manquantes de age par la moyenne
df["age"].fillna(df['age'].mean(),inplace=True)
print(df)

#9 visualisation des outliers avec boxplot
plt.boxplot(df['exam_score'])
plt.show()

# 10 correlation entre study hours et exam score
print(f"la correlation est {df['study_hours'].corr(df['exam_score'])}")
#_____il y a une tres faible correlation entre study hours et exam scor a cause de presence de la note 40 qui est un outlier tres fort sinon les notes sont proportionnel au study hours

# 11 calcul de la moyenne de exame score pour chaque departement  
moyenne_departement = df.groupby('departement')['exam_score'].mean()
print(moyenne_departement)
#et quel departement a de meilleurs resultats
meilleur_departement = moyenne_departement.idxmax()
print("Le département avec les meilleurs résultats est :", meilleur_departement)
#a cause du note 40


# 12 creer une nouvel colonne 'passed' true si exam score >= 10 false sinon 
df['reussi'] = df['exam_score'] >= 10


# 13 quel est le pourcentage d'étudiant ayant réussi
pourcentage_reussite = df['passed'].mean() * 100
print("Pourcentage d'étudiants ayant réussi :", pourcentage_reussite)

