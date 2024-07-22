"""default update in task

Revision ID: 5b93bfdb1661
Revises: 87fe0d77d4b2
Create Date: 2024-07-22 09:54:56.451681

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '5b93bfdb1661'
down_revision: Union[str, None] = '87fe0d77d4b2'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    pass


def downgrade() -> None:
    pass
