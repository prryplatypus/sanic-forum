UPDATE forum.categories
SET display_order = display_order + 1
WHERE parent_category_id = $parent_category_id
AND display_order >= $display_order;
