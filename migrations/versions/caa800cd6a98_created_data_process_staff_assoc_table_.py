"""created data_process_staff_assoc table and added staff relationship in db_process table

Revision ID: caa800cd6a98
Revises: ffa7d9d8720b
Create Date: 2023-07-26 15:22:21.367969

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'caa800cd6a98'
down_revision = 'ffa7d9d8720b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('data_process_staff_assoc',
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('process_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['process_id'], ['db_processes.id'], ),
    sa.ForeignKeyConstraint(['staff_id'], ['staff_account.id'], ),
    sa.PrimaryKeyConstraint('staff_id', 'process_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('data_process_staff_assoc')
    # ### end Alembic commands ###
