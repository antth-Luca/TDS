create database antthluca_11d07m24
default character set utf8
default collate utf8_general_ci;

use antthluca_11d07m24;

-- Criação da tabela Cliente
CREATE TABLE Cliente (
    id_cliente INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL
);

-- Criação da tabela Vendedor
CREATE TABLE Vendedor (
    id_vendedor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    data_admissao DATE NOT NULL,
    data_demissao DATE
);

-- Criação da tabela Fatura
CREATE TABLE Fatura (
    id_fatura INT AUTO_INCREMENT PRIMARY KEY,
    id_vendedor_lookup INT NOT NULL,
    id_cliente_lookup INT NOT NULL,
    data_fatura DATE NOT NULL,
    FOREIGN KEY (id_vendedor_lookup) REFERENCES Vendedor(id_vendedor),
    FOREIGN KEY (id_cliente_lookup) REFERENCES Cliente(id_cliente)
);

-- Criação da tabela Produto
CREATE TABLE Produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    preco DECIMAL(10, 2) NOT NULL
);

-- Criação da tabela LinhaFatura
CREATE TABLE LinhaFatura (
    id_linha INT AUTO_INCREMENT PRIMARY KEY,
    id_fatura_lookup INT NOT NULL,
    id_produto_lookup INT NOT NULL,
    quantidade INT NOT NULL,
    FOREIGN KEY (id_fatura_lookup) REFERENCES Fatura(id_fatura),
    FOREIGN KEY (id_produto_lookup) REFERENCES Produto(id_produto)
);

-- Inserção de dados na tabela Cliente
INSERT INTO Cliente (nome) VALUES 
('Empresa A'),
('Empresa B'),
('Empresa C'),
('Empresa D'),
('Empresa E');

-- Inserção de dados na tabela Vendedor
INSERT INTO Vendedor (nome, data_admissao, data_demissao) VALUES 
('João', '2022-01-01', NULL),
('Maria', '2022-02-01', NULL),
('Pedro', '2022-03-01', NULL),
('Ana', '2022-04-01', NULL),
('Carlos', '2022-05-01', NULL);

-- Inserção de dados na tabela Fatura
INSERT INTO Fatura (id_vendedor_lookup, id_cliente_lookup, data_fatura) VALUES 
(1, 1, '2024-07-01'),
(2, 2, '2024-07-02'),
(3, 3, '2024-07-03'),
(4, 4, '2024-07-04'),
(5, 5, '2024-07-05');

-- Inserção de dados na tabela Produto
INSERT INTO Produto (nome, preco) VALUES 
('Produto A', 10.00),
('Produto B', 20.00),
('Produto C', 30.00),
('Produto D', 40.00),
('Produto E', 50.00);

-- Inserção de dados na tabela LinhaFatura
INSERT INTO LinhaFatura (id_fatura_lookup, id_produto_lookup, quantidade) VALUES 
(1, 1, 2), -- Fatura 1, Produto A, Quantidade 2
(1, 2, 1), -- Fatura 1, Produto B, Quantidade 1
(2, 3, 3), -- Fatura 2, Produto C, Quantidade 3
(2, 4, 2), -- Fatura 2, Produto D, Quantidade 2
(3, 5, 1), -- Fatura 3, Produto E, Quantidade 1
(3, 1, 1), -- Fatura 3, Produto A, Quantidade 1
(4, 2, 2), -- Fatura 4, Produto B, Quantidade 2
(4, 3, 1), -- Fatura 4, Produto C, Quantidade 1
(5, 4, 3), -- Fatura 5, Produto D, Quantidade 3
(5, 5, 2); -- Fatura 5, Produto E, Quantidade 2