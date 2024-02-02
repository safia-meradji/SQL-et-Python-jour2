-- Création de la base de données
CREATE DATABASE IF NOT EXISTS Entreprise;

-- Utilisation de la base de données
USE Entreprise;

-- Création de la table "employe"
CREATE TABLE employe (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255),
    prenom VARCHAR(255),
    salaire DECIMAL(10, 2),
    id_service INT,
    FOREIGN KEY (id_service) REFERENCES service(id)
);
-- Ajouter des enregistrements dans la table "service"
INSERT INTO service (nom) VALUES
('Service A'),
('Service B'),
('Service C');

-- Insertion d'employés dans la table "employe"
INSERT INTO employe (nom, prenom, salaire, id_service) VALUES
('Dupont', 'Jean', 3500.00, 1),
('Martin', 'Sophie', 2800.50, 2),
('Lefevre', 'Pierre', 4200.75, 1),
('Dubois', 'Marie', 3200.25, 3);

-- Récupération des employés dont le salaire est supérieur à 3 000 €
SELECT * FROM employe WHERE salaire > 3000.00;

-- Création de la table "service"
CREATE TABLE service (
    id INT PRIMARY KEY AUTO_INCREMENT,
    nom VARCHAR(255)
);

-- Insertion de services dans la table "service"
INSERT INTO service (nom) VALUES
('RH'),
('Informatique'),
('Comptabilité');

