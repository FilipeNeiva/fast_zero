"""test

Revision ID: dc59ea949554
Revises: c7c478ebbf17
Create Date: 2024-07-22 10:11:10.148469

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dc59ea949554'
down_revision: Union[str, None] = 'c7c478ebbf17'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
