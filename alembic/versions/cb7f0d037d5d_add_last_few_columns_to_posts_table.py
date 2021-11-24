"""add last few columns  to  posts table

Revision ID: cb7f0d037d5d
Revises: a3a369911283
Create Date: 2021-11-23 10:57:16.577926

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cb7f0d037d5d'
down_revision = 'a3a369911283'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column('posts', sa.Column(
                'published', sa.Boolean(), nullable=False, server_default='TRUE'),)
    op.add_column('posts', sa.Column(
                'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')),)
    pass


def downgrade():
    op.drop_column('posts', 'published')
    op.drop_column('posts', 'created_at')
    pass 
