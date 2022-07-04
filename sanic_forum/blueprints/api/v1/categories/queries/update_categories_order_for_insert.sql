UPDATE forum.categories
SET display_order = display_order + 1
WHERE display_order >= $display_order
AND (
    parent_category_id = $parent_category_id
    OR (parent_category_id IS NULL AND $parent_category_id IS NULL)
);
