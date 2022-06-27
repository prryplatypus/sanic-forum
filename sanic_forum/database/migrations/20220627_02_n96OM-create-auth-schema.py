"""
Create auth schema
"""

from yoyo import step

__depends__ = {'20220627_01_7XYRw-enable-needed-extensions'}

steps = [
    step(
        "CREATE SCHEMA auth",
        "DROP SCHEMA auth",
    )
]
