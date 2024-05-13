from alembic import op
import sqlalchemy as sa

def upgrade():
    op.create_table(
        'items',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', sa.String),
        sa.Column('quantity', sa.Integer),
        sa.Column('type', sa.Integer),
        sa.Column('brand', sa.String),
        sa.Column('color', sa.String),
        sa.Column('price', sa.Float),
    )

def downgrade():
    op.drop_table('items')
    