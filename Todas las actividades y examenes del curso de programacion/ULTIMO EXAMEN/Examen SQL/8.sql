SELECT 
    COUNT(*) AS total_ventas,
    SUM(monto) AS ingresos_totales,
    AVG(monto) AS promedio_ticket
FROM Pedidos;