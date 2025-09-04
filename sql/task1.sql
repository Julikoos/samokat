SELECT c."login", count(o.id) 
FROM "Couriers" AS c
JOIN "Orders" AS o ON o."courierId" = c.id
WHERE o."inDelivery"=true
GROUP BY c.id;