import mysql.connector

class ZooManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def ajouter_animal(self, nom, race, id_cage, date_naissance, pays_origine):
        query = "INSERT INTO animal (nom, race, id_cage, date_naissance, pays_origine) VALUES (%s, %s, %s, %s, %s)"
        values = (nom, race, id_cage, date_naissance, pays_origine)
        self.cursor.execute(query, values)
        self.conn.commit()

    def supprimer_animal(self, animal_id):
        query = "DELETE FROM animal WHERE id = %s"
        values = (animal_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def modifier_animal(self, animal_id, new_nom, new_race, new_id_cage, new_date_naissance, new_pays_origine):
        query = "UPDATE animal SET nom = %s, race = %s, id_cage = %s, date_naissance = %s, pays_origine = %s WHERE id = %s"
        values = (new_nom, new_race, new_id_cage, new_date_naissance, new_pays_origine, animal_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def afficher_animaux(self):
        query = "SELECT * FROM animal"
        self.cursor.execute(query)
        animaux = self.cursor.fetchall()
        for animal in animaux:
            print(animal)

    def afficher_animaux_cages(self):
        query = "SELECT a.nom, a.race, c.id AS id_cage FROM animal a LEFT JOIN cage c ON a.id_cage = c.id"
        self.cursor.execute(query)
        animaux_cages = self.cursor.fetchall()
        for animal_cage in animaux_cages:
            print(animal_cage)

    def calculer_superficie_totale(self):
        query = "SELECT SUM(superficie) AS superficie_totale FROM cage"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        superficie_totale = result[0]
        print(f"La superficie totale de toutes les cages est de {superficie_totale} m2")

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe ZooManager
zoo_manager = ZooManager("votre_hôte", "votre_utilisateur", "votre_mot_de_passe", "zoo")

# Ajouter un nouvel animal
zoo_manager.ajouter_animal("Lion", "Félin", 1, "2020-01-01", "Afrique")

# Afficher tous les animaux
zoo_manager.afficher_animaux()

# Afficher les animaux dans les cages
zoo_manager.afficher_animaux_cages()

# Calculer la superficie totale des cages
zoo_manager.calculer_superficie_totale()
