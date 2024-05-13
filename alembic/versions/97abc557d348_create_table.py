"""create db

Revision ID: 97abc557d348
Revises: 
Create Date: 2024-05-07 07:59:11.118494

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '97abc557d348'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.create_table(
        'items',
        sa.Column('name', sa.String, primary_key=True),
        sa.Column('quantity', sa.Integer),
        sa.Column('type', sa.String),
        sa.Column('brand', sa.String),
        sa.Column('color', sa.String),
        sa.Column('price', sa.Float),
    )

def downgrade():
    op.drop_table('items')
    