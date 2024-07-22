"""create created todo

Revision ID: c7c478ebbf17
Revises: 9447c8940b4c
Create Date: 2024-07-22 09:59:53.161600

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c7c478ebbf17'
down_revision: Union[str, None] = '9447c8940b4c'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
