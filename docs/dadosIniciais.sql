use vacinacao;

insert into core_crianca values
(1, 'Rômulo Gabriel Sousa Sá', '15452658245'),
(2, 'Ramon Santana de Sousa', '47585654215'),
(3, 'Geovana Daniele Alves Fontenele', '58245163258'),
(4, 'Arthur Manoel Oliveira', '54158954291'),
(5, 'Diego Caiena Rodrigues', '00400545285'),
(6, 'Wagner Oliveira Juniro', '47859654215');

insert into core_vacina values
(1, 'BCG-ID', 'Fundação Ataulpho de Paiva', 'Imuniza contra a tuberculose e também contra as suas formas graves.'),
(2, 'HEPATITE B', 'Instituto Butantan', 'Imuniza contra HEPATITE B.'),
(3, 'DTPa', 'Instituto Butantan/GlaxoSmithKline/Fio Cruz', 'Previne infecção bacteriana de difteria, tétano e pertussis acelular.'),
(4, 'HIB', 'Fio Cruz', 'Previne doenças causadas pelo Haemophilus influenzae tipo b, principalmente meningite.'),
(5, 'VIP/VOP', 'Fio Cruz', 'Previne a doença poliomielite e assim, a paralisia infantil.'),
(6, 'VRH1', 'Fio Cruz/GlaxoSmithKline', 'A vacina protege as crianças dos quadros relacionados ao vírus, que incluem vômito e diarreia.'),
(7, 'VPC10', 'Fio Cruz/GlaxoSmithKline', 'A vacina ajuda a proteger as crianças das doenças causadas pela bactéria Streptococcus pneumoniae. Entre elas estão: meningite, pneumonia, otite média aguda, sinusite e bacteremia.'),
(8, 'Vacina Meningocócica ACWY', 'Fio Cruz/GlaxoSmithKline', 'A vacina ajuda a proteger as crianças das doenças causadas pela bactéria Streptococcus pneumoniae. Entre elas estão: meningite, pneumonia, otite média aguda, sinusite e bacteremia.');

insert into core_vacinacao values
(1, 'AGHE1547HJ', '2019-06-27', 'Gabriela Santos', 1, 1),
(2, 'KJHE5148KL', '2019-07-17', 'Nicoli Dias', 1, 3),
(3, 'LOPI5263KO', '2018-06-30', 'Antonio Sousa', 2, 2),
(4, 'AKHJ4526OP', '2018-08-21', 'João da Silva', 2, 4),
(5, 'YHJO1524KP', '2016-01-19', 'José de Sousa', 3, 5),
(6, 'KLOP5847HJ', '2016-05-25', 'Mateus Trindade', 3, 6),
(7, 'QRTU5263PO', '2020-04-20', 'Mateus Rocha', 4, 7),
(8, 'HETR5287HJ', '2017-04-20', 'Lutero Rocha', 5, 8),
(9, 'MNKJ5632KP', '2020-10-10', 'Gabriela Silva', 6, 3);