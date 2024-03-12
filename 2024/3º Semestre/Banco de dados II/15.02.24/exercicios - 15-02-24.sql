-- 1)
CREATE TABLE NotasAlunos (
    Matricula INT PRIMARY KEY,
    Nome VARCHAR(50) NOT NULL,
    Disciplina VARCHAR(30) NOT NULL,
    Nota FLOAT,
    Status VARCHAR(15)
);

-- 2)
INSERT INTO NotasAlunos (Matricula, Nome, Disciplina, Nota, Status)
VALUES
    (1, 'João Silva', 'Matemática', 8.5, 'Aprovado'),
    (2, 'Maria Oliveira', 'História', 7.2, 'Aprovado'),
    (3, 'Carlos Santos', 'Inglês', 5.8, 'Reprovado'),
    (4, 'Ana Pereira', 'Ciências', 9.3, 'Aprovado'),
    (5, 'Pedro Costa', 'Geografia', 6.5, 'Em andamento');

-- 3)
UPDATE NotasAlunos
SET Nota = 9.0
WHERE Matricula = 1;

UPDATE NotasAlunos
SET Status = 'Concluído'
WHERE Matricula = 5;

ALTER TABLE NotasAlunos
ADD COLUMN Frequencia FLOAT DEFAULT 75;

ALTER TABLE NotasAlunos
RENAME COLUMN Status TO Resultado;

ALTER TABLE NotasAlunos
DROP COLUMN Disciplina;

-- 4)
DELETE FROM NotasAlunos
WHERE Nota < 6.0;