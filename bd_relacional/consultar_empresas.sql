SELECT e.nome, c.nome as 'Cidades' FROM empresas e, unidades_empresas ue, cidades c WHERE e.id = ue.empresa_id AND c.id = ue.cidade_id;