SELECT * FROM prefeitos;
SELECT * FROM cidades;

SELECT * FROM cidades c inner join prefeitos p on c.id = p.cidade_id;
SELECT * FROM cidades c left join prefeitos p on c.id = p.cidade_id;
SELECT * FROM cidades c right join prefeitos p on c.id = p.cidade_id;

-- FULL join funciona apenas em alguns bancos (neste caso trocamos para o union)
--SELECT * FROM cidades c FULL join prefeitos p on c.id = p.cidade_id;

SELECT * FROM cidades c left outer join prefeitos p on c.id = p.cidade_id
union
SELECT * FROM cidades c right join prefeitos p on c.id = p.cidade_id;