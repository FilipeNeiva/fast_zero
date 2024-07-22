"""default update

Revision ID: 87fe0d77d4b2
Revises: 960a302b5498
Create Date: 2024-07-22 09:36:34.586622

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '87fe0d77d4b2'
down_revision: Union[str, None] = '960a302b5498'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
