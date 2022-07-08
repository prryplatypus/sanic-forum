SELECT count(*)
FROM forum.categories
WHERE id = $id
LIMIT 1;
