"""added columns start_travel_datetime and end_travel_datetime in table StaffLeaveRequest

Revision ID: 002806480308
Revises: 9231935211aa
Create Date: 2020-08-13 13:36:54.975892

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '002806480308'
down_revision = '9231935211aa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff_leave_requests', sa.Column('end_travel_datetime', sa.DateTime(timezone=True), nullable=True))
    op.add_column('staff_leave_requests', sa.Column('start_travel_datetime', sa.DateTime(timezone=True), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('staff_leave_requests', 'start_travel_datetime')
    op.drop_column('staff_leave_requests', 'end_travel_datetime')
    # ### end Alembic commands ###
