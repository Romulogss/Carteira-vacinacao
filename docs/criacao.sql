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
    fabricante varchar(50) not null,
    descricao varchar(200) not null
);

create table core_vacinacao (
    id int primary key not null auto_increment,
    lote varchar(10) not null,
    data datetime not null,
    enfermeiro varchar(50) not null,
    crianca_id int not null,
    vacina_id int not null,
    foreign key (crianca_id) references core_crianca(id),
    foreign key (vacina_id) references core_vacina(id)
);
