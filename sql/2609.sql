SELECT
	c.name,
    SUM(p.amount) as sum
FROM products p
JOIN categories c ON p.id_categories = c.id
GROUP BY c.id, c.name;