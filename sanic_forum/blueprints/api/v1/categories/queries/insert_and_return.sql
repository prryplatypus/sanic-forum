INSERT INTO forum.categories (parent_category_id, name, display_order)
VALUES ($parent_category_id, $name, $display_order)
RETURNING id, parent_category_id, name, display_order;
