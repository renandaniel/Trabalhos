/*CREATE*/
CREATE TABLE IF NOT EXISTS Grupo
(
GrupoCodigo INT auto_increment PRIMARY KEY,
GrupoNome VARCHAR(50),
GrupoRazaoSocial VARCHAR(50),
GrupoCNPJ varchar(20)
);

create table IF NOT EXISTS Clientes
(
ClienteCodigo int auto_increment PRIMARY KEY,
ClienteNome varchar (50),
ClienteRua varchar (50),
ClienteCidade varchar (50),
ClienteNascimento datetime
);

CREATE TABLE IF NOT EXISTS Agencias
(
AgenciaCodigo INT auto_increment PRIMARY KEY,
AgenciaNome VARCHAR (50),
AgenciaCidade varchar (50),
AgenciaFundos decimal(8,2),
GrupoCodigo int
);

CREATE TABLE IF NOT EXISTS Contas
(
AgenciaCodigo int,
ContaNumero VARCHAR (10) PRIMARY KEY,
ClienteCodigo int,
ContaSaldo DECIMAL(8,2),
ContaAbertura datetime
);

create table IF NOT EXISTS Emprestimos
(
AgenciaCodigo INT,
ClienteCodigo int,
EmprestimoCodigo varchar (10),
EmprestimoTotal DECIMAL(8,2)
);

create table Depositantes
(
AgenciaCodigo INT,
ContaNumero varchar(10),
ClienteCodigo int,
DepositoValor DECIMAL(8,2),
DepositoData DATETIME
);

create table Devedores
(
AgenciaCodigo INT,
ClienteCodigo int,
EmprestimoCodigo varchar (10),
DevedorSaldo DECIMAL(8,2)
);

create table CartaoCredito
(
AgenciaCodigo INT,
ClienteCodigo int,
CartaoCodigo varchar (20),
CartaoLimite DECIMAL(8,2)
)
