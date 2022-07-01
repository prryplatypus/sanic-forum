"""
Create forum schema
"""

from yoyo import step

__depends__ = {'20220627_03_D5sNC-create-user-table'}

steps = [
    step(
        "CREATE SCHEMA forum",
        "DROP SCHEMA forum",
    )
]
