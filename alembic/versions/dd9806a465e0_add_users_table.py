"""add users table

Revision ID: dd9806a465e0
Revises: 8199bd07fece
Create Date: 2022-03-27 07:26:23.699512

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dd9806a465e0'
down_revision = '8199bd07fece'
branch_labels = None
depends_on = None


def upgrade():
    op.create_table("users", 
                    sa.Column("id", sa.Integer(), nullable=False),
                    sa.Column("email", sa.String(), nullable=False),
                    sa.Column("password", sa.String(), nullable=False),
                    sa.Column("created_at", sa.TIMESTAMP(timezone=True),
                              server_default=sa.text("now()"), nullable=False),
                    sa.PrimaryKeyConstraint("id"),
                    sa.UniqueConstraint("email")
                    )
    pass


def downgrade():
    op.drop_table("users")
    pass
