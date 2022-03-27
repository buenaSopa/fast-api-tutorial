"""add foreign key to posts table

Revision ID: 4a133d24de88
Revises: dd9806a465e0
Create Date: 2022-03-27 07:35:05.078965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a133d24de88'
down_revision = 'dd9806a465e0'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("owner_id", sa.Integer(), nullable=False))
    op.create_foreign_key("posts_users_fk", source_table="posts", referent_table="users", 
    local_cols=['owner_id'], remote_cols=["id"], ondelete="CASCADE")
    pass


def downgrade():
    op.drop_constraint("posts_users_fk", "posts")
    op.drop_column("posts", "owner_id")
    pass
