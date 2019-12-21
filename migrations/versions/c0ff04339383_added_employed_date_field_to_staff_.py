"""added employed date field to staff personal info

Revision ID: c0ff04339383
Revises: 93a8aad4010b
Create Date: 2019-12-20 08:40:30.844298

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0ff04339383'
down_revision = '93a8aad4010b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff_personal_info', sa.Column('employed_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('staff_personal_info', 'employed_date')
    # ### end Alembic commands ###