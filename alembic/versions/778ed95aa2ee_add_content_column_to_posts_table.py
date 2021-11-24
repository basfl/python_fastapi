"""add content column to  posts table

Revision ID: 778ed95aa2ee
Revises: 1e692306be41
Create Date: 2021-11-23 10:34:42.214486

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '778ed95aa2ee'
down_revision = '1e692306be41'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column('content', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column('posts', 'content')
    pass
