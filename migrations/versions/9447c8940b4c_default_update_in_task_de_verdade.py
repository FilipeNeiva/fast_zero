"""default update in task de verdade

Revision ID: 9447c8940b4c
Revises: 5b93bfdb1661
Create Date: 2024-07-22 09:55:36.975496

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '9447c8940b4c'
down_revision: Union[str, None] = '5b93bfdb1661'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
