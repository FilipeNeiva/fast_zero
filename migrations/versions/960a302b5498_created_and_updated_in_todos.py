"""created and updated in todos

Revision ID: 960a302b5498
Revises: 4a168eb7a2ac
Create Date: 2024-07-19 17:23:36.812580

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '960a302b5498'
down_revision: Union[str, None] = '4a168eb7a2ac'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
