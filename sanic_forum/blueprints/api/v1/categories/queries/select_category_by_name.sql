SELECT id, parent_category_id, name, display_order
FROM forum.categories
WHERE name = $name
AND (
    parent_category_id = $parent_category_id
    OR (parent_category_id IS NULL AND $parent_category_id IS NULL)
)
LIMIT 1;
