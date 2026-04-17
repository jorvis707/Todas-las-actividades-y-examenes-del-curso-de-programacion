SELECT 
    Clientes.nombre, 
    Pedidos.monto, 
    Pedidos.fecha_pedido
FROM Clientes
INNER JOIN Pedidos ON Clientes.id_cliente = Pedidos.cliente_id;