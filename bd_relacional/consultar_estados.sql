SELECT * FROM `estados`

SELECT NOME, SIGLA FROM `estados` WHERE regiao = "SUL"

SELECT NOME, SIGLA FROM `estados` 
WHERE populacao >= 10
order by populacao desc