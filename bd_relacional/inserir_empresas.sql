INSERT INTO empresas (nome, cnpj) VALUES ('Bradesco', 09811410000180);
INSERT INTO empresas (nome, cnpj) VALUES ('Vale', 05135808000015);
INSERT INTO empresas (nome, cnpj) VALUES ('Cielo', 01234567891012);

DESC empresas;

SELECT * FROM `empresas`;
SELECT * FROM `unidades_empresas`;

ALTER TABLE empresas MODIFY cnpj VARCHAR(14);

INSERT INTO unidades_empresas (empresa_id, cidade_id, sede) VALUES (1,1,1);
INSERT INTO unidades_empresas (empresa_id, cidade_id, sede) VALUES (1,2,0);
INSERT INTO unidades_empresas (empresa_id, cidade_id, sede) VALUES (2,1,0);
INSERT INTO unidades_empresas (empresa_id, cidade_id, sede) VALUES (2,2,1);