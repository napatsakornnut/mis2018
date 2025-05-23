"""Deleted status column in ServiceQuotation model

Revision ID: c837f1a718d3
Revises: ea682c670c9e
Create Date: 2025-01-28 14:35:40.418497

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = 'c837f1a718d3'
down_revision = 'ea682c670c9e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('service_quotations', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('service_quotations', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.BOOLEAN(), autoincrement=False, nullable=True))
    # ### end Alembic commands ###
