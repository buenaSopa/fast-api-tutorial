"""add content column to posts table

Revision ID: 8199bd07fece
Revises: 9cc9d048ea40
Create Date: 2022-03-27 07:20:12.574870

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8199bd07fece'
down_revision = '9cc9d048ea40'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("content", sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "content")
    pass
