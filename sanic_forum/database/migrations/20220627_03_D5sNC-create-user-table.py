"""
Create User table
"""

from yoyo import step

__depends__ = {'20220627_02_n96OM-create-auth-schema'}


MIGRATE = """
CREATE TABLE auth.users(
    id UUID DEFAULT uuid_generate_v4(),
    username CITEXT NOT NULL,
    CONSTRAINT pk_user PRIMARY KEY (id),
    CONSTRAINT uk_username UNIQUE (username)
)
"""

ROLLBACK = """
DROP TABLE auth.users
"""

steps = [
    step(MIGRATE, ROLLBACK)
]
