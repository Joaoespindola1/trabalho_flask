CREATE DATABASE aula_13_10;

USE aula_13_10;

CREATE TABLE setor (
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50) NOT NULL
);

CREATE TABLE funcionarios(
id INT AUTO_INCREMENT PRIMARY KEY,
primeiro_nome VARCHAR(50) NOT NULL,
sobrenome VARCHAR(50) NOT NULL,
data_admissao DATE NOT NULL,
status_funcionario BOOL NOT NULL,
id_setor INT,
FOREIGN KEY (id_setor) REFERENCES setor(id)
);

SELECT * FROM setor;
SELECT * FROM cargos;

UPDATE cargos
SET id_setor = 2
WHERE id = 4;

ALTER TABLE funcionarios ADD COLUMN cargo VARCHAR(50) NOT NULL;
ALTER TABLE funcionarios DROP COLUMN cargo;

CREATE TABLE cargos(
id INT AUTO_INCREMENT PRIMARY KEY,
nome VARCHAR(50),
id_setor INT,
FOREIGN KEY (id_setor) REFERENCES setor(id)
);

ALTER TABLE cargos MODIFY COLUMN nome VARCHAR(50) NOT NULL;

ALTER TABLE funcionarios ADD COLUMN id_cargo INT;
ALTER TABLE funcionarios ADD FOREIGN KEY (id_cargo) REFERENCES cargos(id);

