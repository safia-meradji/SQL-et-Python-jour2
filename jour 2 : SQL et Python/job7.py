import mysql.connector

class EmployeManager:
    def __init__(self, host, user, password, database):
        self.conn = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        self.cursor = self.conn.cursor()

    def create_employe(self, nom, prenom, salaire, id_service):
        query = "INSERT INTO employe (nom, prenom, salaire, id_service) VALUES (%s, %s, %s, %s)"
        values = (nom, prenom, salaire, id_service)
        self.cursor.execute(query, values)
        self.conn.commit()

    def read_employes(self):
        query = "SELECT * FROM employe"
        self.cursor.execute(query)
        employes = self.cursor.fetchall()
        for employe in employes:
            print(employe)

    def update_employe(self, employe_id, new_salaire):
        query = "UPDATE employe SET salaire = %s WHERE id = %s"
        values = (new_salaire, employe_id)
        self.cursor.execute(query, values)
        self.conn.commit()

    def delete_employe(self, employe_id):
        query = "DELETE FROM employe WHERE id = %s"
        values = (employe_id,)
        self.cursor.execute(query, values)
        self.conn.commit()

    def __del__(self):
        self.cursor.close()
        self.conn.close()

# Exemple d'utilisation de la classe EmployeManager
employe_manager = EmployeManager("votre_hôte", "votre_utilisateur", "votre_mot_de_passe", "Entreprise")

# Ajouter un nouvel employé
employe_manager.create_employe("Durand", "Paul", 3800.00, 2)

# Lire tous les employés
employe_manager.read_employes()

# Mettre à jour le salaire d'un employé
employe_manager.update_employe(1, 4000.00)

# Supprimer un employé
employe_manager.delete_employe(2)

# Lire à nouveau tous les employés après les modifications
employe_manager.read_employes()
