"""
Enable needed extensions
"""

from yoyo import step

__depends__ = {}

steps = [
    # Case insensitive text
    step(
        "CREATE EXTENSION IF NOT EXISTS citext",
        "DROP EXTENSION IF EXISTS citext",
    ),
    # Auto UUIDs
    step(
        "CREATE EXTENSION IF NOT EXISTS \"uuid-ossp\"",
        "DROP EXTENSION IF EXISTS \"uuid-ossp\"",
    ),
]
