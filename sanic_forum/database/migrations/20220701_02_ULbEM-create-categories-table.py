"""
Create categories table
"""

from yoyo import step

__depends__ = {'20220701_01_oieqe-create-forum-schema'}

MIGRATE = """
CREATE TABLE forum.categories(
    id UUID DEFAULT uuid_generate_v4(),
    parent_category_id UUID NULL DEFAULT NULL,
    name CITEXT NOT NULL,
    display_order SMALLINT NOT NULL,
    CONSTRAINT pk_category PRIMARY KEY (id),
    CONSTRAINT fk_category_parent_category_id FOREIGN KEY (parent_category_id)
        REFERENCES forum.categories(id)
)
"""

ROLLBACK = """
DROP TABLE forum.categories
"""

steps = [
    step(MIGRATE, ROLLBACK),
    # UNIQUE (parent_category_id, name) IF parent_category_id IS NOT NULL
    step(
        """
        CREATE UNIQUE INDEX uk_category_name_with_parent
        ON forum.categories (parent_category_id, name)
        WHERE parent_category_id IS NOT NULL
        """,
        """
        DROP INDEX forum.uk_category_name_with_parent
        """
    ),
    # UNIQUE (name) IF parent_category_id IS NULL
    step(
        """
        CREATE UNIQUE INDEX uk_category_name_without_parent
        ON forum.categories (name)
        WHERE parent_category_id IS NULL
        """,
        """
        DROP INDEX forum.uk_category_name_without_parent
        """
    ),
    # UNIQUE (parent_category_id, display_order)
    # IF parent_category_id IS NOT NULL
    step(
        """
        CREATE UNIQUE INDEX uk_category_display_order_with_parent
        ON forum.categories (parent_category_id, display_order)
        WHERE parent_category_id IS NOT NULL
        """,
        """
        DROP INDEX forum.uk_category_display_order_with_parent
        """
    ),
    # UNIQUE (display_order) IF parent_category_id IS NULL
    step(
        """
        CREATE UNIQUE INDEX uk_category_display_order_without_parent
        ON forum.categories (display_order)
        WHERE parent_category_id IS NULL
        """,
        """
        DROP INDEX forum.uk_category_display_order_without_parent
        """
    )
]
