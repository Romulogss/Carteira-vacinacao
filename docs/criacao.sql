create database vacinacao;
use vacinacao;
create table core_crianca (
    id int primary key not null auto_increment,
    nome varchar(50) not null,
    cpf varchar(11) not null unique
);

create table core_vacina (
    id int primary key not null auto_increment,
    nome varchar(50) not null,
    fabricante varchar(20)
);

create table core_vacinacao (
    id int primary key not null auto_increment,
    lote varchar(10),
    data datetime,
    crianca_id int,
    vacina_id int,
    foreign key (crianca_id) references core_crianca(id),
    foreign key (vacina_id) references core_vacina(id)
);