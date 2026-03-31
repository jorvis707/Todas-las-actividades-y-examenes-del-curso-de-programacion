CREATE TABLE estudiantes (
    cedula INT PRIMARY KEY,
    nombre VARCHAR(100),
    apellido VARCHAR(100),
    edad INT,
    pelicula_favorita VARCHAR(100)
);

INSERT INTO estudiantes (cedula, nombre, apellido, edad, pelicula_favorita) VALUES
(31698444, 'Rafael', 'Pino', 20, 'Chainsmaw'),
(31594561, 'Eduardo', 'Portillo', 19, 'El conjuro'),
(29505772, 'Joe', 'Ortega', 27, 'Termineitor'),
(33317226, 'Jose', 'Rondon', 16, 'Volver al futuro'),
(33141768, 'Nervin', 'Ortega', 19, 'Harri potter'),
(25801555, 'Jonthan', 'Cadenas', 28, 'El tierno abrazo de una madre mocha'),
(32124105, 'Nelson', 'Quintero', 18, 'DragonballZ'),
(29999215, 'Geralber', 'Molero', 24, 'Shek');