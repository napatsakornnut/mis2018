"""Added taxpayer_identification_no column in ServiceCustomerInfo model

Revision ID: db9b11a0ba27
Revises: 4b4f0ba52300
Create Date: 2024-04-30 13:44:16.067701

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db9b11a0ba27'
down_revision = '4b4f0ba52300'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('service_customer_infos', schema=None) as batch_op:
        batch_op.add_column(sa.Column('taxpayer_identification_no', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('service_customer_infos', schema=None) as batch_op:
        batch_op.drop_column('taxpayer_identification_no')

    # ### end Alembic commands ###