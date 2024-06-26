"""added date field and changed start, end datetime to time field

Revision ID: 496af2df56ed
Revises: ea7c4d5b5102
Create Date: 2023-09-11 14:44:17.691029

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '496af2df56ed'
down_revision = 'ea7c4d5b5102'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('ot_compensation_rate', schema=None) as batch_op:
        batch_op.add_column(sa.Column('detail', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('abbr', sa.String(), nullable=True))

    with op.batch_alter_table('ot_record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.Date(), nullable=True))
        batch_op.add_column(sa.Column('start_time', sa.Time(), nullable=True))
        batch_op.add_column(sa.Column('end_time', sa.Time(), nullable=True))
        batch_op.drop_column('start_datetime')
        batch_op.drop_column('end_datetime')

    with op.batch_alter_table('staff_shift_schedule', schema=None) as batch_op:
        batch_op.add_column(sa.Column('detail', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('abbr', sa.String(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('staff_shift_schedule', schema=None) as batch_op:
        batch_op.drop_column('abbr')
        batch_op.drop_column('detail')

    with op.batch_alter_table('ot_record', schema=None) as batch_op:
        batch_op.add_column(sa.Column('end_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.add_column(sa.Column('start_datetime', postgresql.TIMESTAMP(), autoincrement=False, nullable=True))
        batch_op.drop_column('end_time')
        batch_op.drop_column('start_time')
        batch_op.drop_column('date')

    with op.batch_alter_table('ot_compensation_rate', schema=None) as batch_op:
        batch_op.drop_column('abbr')
        batch_op.drop_column('detail')

    # ### end Alembic commands ###
