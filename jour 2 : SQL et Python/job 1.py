import mysql.connector

# Remplacez les valeurs suivantes par vos propres informations de connexion
host = "localhost"
user = "root"
password = "root"
database = "LaPlateforme"

# Établir la connexion à la base de données
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password,
    database=database
)

# Créer un objet curseur pour exécuter des requêtes SQL
cursor = conn.cursor()

# Exécuter la requête pour récupérer l'ensemble des étudiants
query = "SELECT * FROM etudiant"
cursor.execute(query)

# Récupérer les résultats
result = cursor.fetchall()

# Afficher les résultats
for row in result:
    print(row)

# Fermer le curseur et la connexion
cursor.close()
conn.close()
