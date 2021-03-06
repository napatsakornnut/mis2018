"""added 2 columns in StaffWorkFromHomeCheckedJob for record finished and checked time

Revision ID: 8d65b1430a21
Revises: f871a5230a71
Create Date: 2020-05-26 20:44:04.114868

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d65b1430a21'
down_revision = 'f871a5230a71'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('staff_work_from_home_checked_job', sa.Column('approver_id', sa.Integer(), nullable=True))
    op.add_column('staff_work_from_home_checked_job', sa.Column('check_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('staff_work_from_home_checked_job', sa.Column('finish_at', sa.DateTime(timezone=True), nullable=True))
    op.create_foreign_key(None, 'staff_work_from_home_checked_job', 'staff_account', ['approver_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'staff_work_from_home_checked_job', type_='foreignkey')
    op.drop_column('staff_work_from_home_checked_job', 'finish_at')
    op.drop_column('staff_work_from_home_checked_job', 'check_at')
    op.drop_column('staff_work_from_home_checked_job', 'approver_id')
    # ### end Alembic commands ###
