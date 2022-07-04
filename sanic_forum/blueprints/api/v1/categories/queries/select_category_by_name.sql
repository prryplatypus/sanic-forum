SELECT id, parent_category_id, name, display_order
FROM forum.categories
WHERE parent_category_id = $parent_category_id
AND name = $name
LIMIT 1;
