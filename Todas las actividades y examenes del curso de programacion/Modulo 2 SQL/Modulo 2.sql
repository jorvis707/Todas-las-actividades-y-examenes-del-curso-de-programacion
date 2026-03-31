-- 1. CREAR TABLA: Inventario de libreria
CREATE TABLE Libros (
    id INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(100) NOT NULL,
    autor VARCHAR(100) NOT NULL,
    precio DECIMAL(10, 2) NOT NULL
);

-- 2. INSERTAR: Agregando registros
INSERT INTO Libros (titulo, autor, precio) VALUES 
('Cien Anos de Soledad', 'Gabriel Garcia Marquez', 25.50),
('Don Quijote de la Mancha', 'Miguel de Cervantes', 30.00),
('Rayuela', 'Julio Cortazar', 18.75),
('Ficciones', 'Jorge Luis Borges', 22.00),
('El Aleph', 'Jorge Luis Borges', 45.00);

-- 3. CONSULTAR TODO: Recuperar todos los registros
SELECT * FROM Libros;

-- 4. FILTRO BASICO: Buscar por autor especifico
SELECT titulo, precio FROM Libros WHERE autor = 'Jorge Luis Borges';

-- 5. ACTUALIZAR: Modificar precio por rebaja
UPDATE Libros SET precio = precio * 0.90 WHERE id = 1;

-- 6. ELIMINAR: Retirar libro descatalogado
DELETE FROM Libros WHERE id = 3;

-- 7. ORDENAR Y LIMITAR: Los 5 libros mas caros
SELECT * FROM Libros ORDER BY precio DESC LIMIT 5;

-- 8. TABLA RELACIONADA: Ventas vinculadas a Libros
CREATE TABLE Ventas (
    id_venta INT AUTO_INCREMENT PRIMARY KEY,
    fecha DATE NOT NULL,
    cantidad INT NOT NULL,
    libro_id INT,
    FOREIGN KEY (libro_id) REFERENCES Libros(id)
);

-- Insertando datos de prueba para las ventas
INSERT INTO Ventas (fecha, cantidad, libro_id) VALUES 
('2026-03-20', 2, 1),
('2026-03-21', 5, 2),
('2026-03-22', 1, 4),
('2026-03-23', 3, 5);

-- 9. INNER JOIN: Reporte de titulos y cantidad vendida
SELECT Libros.titulo, Ventas.cantidad 
FROM Libros 
INNER JOIN Ventas ON Libros.id = Ventas.libro_id;

-- 10. AGREGACION: Total de libros y precio promedio
SELECT COUNT(*) AS total_libros, AVG(precio) AS precio_promedio FROM Libros;