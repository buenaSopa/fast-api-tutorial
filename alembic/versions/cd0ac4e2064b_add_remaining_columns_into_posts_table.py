"""add remaining columns into posts table

Revision ID: cd0ac4e2064b
Revises: 4a133d24de88
Create Date: 2022-03-27 10:02:10.049562

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'cd0ac4e2064b'
down_revision = '4a133d24de88'
branch_labels = None
depends_on = None


def upgrade():
    op.add_column("posts", sa.Column("published", sa.Boolean(), nullable=False, 
                                    server_default = 'TRUE'),)
    op.add_column("posts", sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                                    server_default=sa.text("now()"), nullable=False))
    pass


def downgrade():
    op.drop_column("posts", "created_at")
    op.drop_column("posts", "published")
    pass
