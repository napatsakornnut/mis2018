"""made name field of the container model not nullable

Revision ID: 32ae8b2b8152
Revises: 66a06a2faab8
Create Date: 2020-01-23 21:22:53.611745

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32ae8b2b8152'
down_revision = '66a06a2faab8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comhealth_containers', 'code',
               existing_type=sa.VARCHAR(length=64),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('comhealth_containers', 'code',
               existing_type=sa.VARCHAR(length=64),
               nullable=True)
    # ### end Alembic commands ###