SELECT 
    cliente_id, 
    COUNT(id_pedido) AS numero_pedidos, 
    SUM(monto) AS gasto_total
FROM Pedidos 
GROUP BY cliente_id;