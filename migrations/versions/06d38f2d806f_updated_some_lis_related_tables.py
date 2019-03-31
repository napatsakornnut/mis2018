"""updated some lis related tables

Revision ID: 06d38f2d806f
Revises: 1debe5deb17a
Create Date: 2019-01-29 15:18:27.457315

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '06d38f2d806f'
down_revision = '1debe5deb17a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lis_orders', sa.Column('test_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'lis_orders', 'lis_tests', ['test_id'], ['id'])
    op.alter_column('lis_results', 'reported_by',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.drop_constraint(u'lis_results_test_id_fkey', 'lis_results', type_='foreignkey')
    op.drop_column('lis_results', 'test_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('lis_results', sa.Column('test_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'lis_results_test_id_fkey', 'lis_results', 'lis_tests', ['test_id'], ['id'])
    op.alter_column('lis_results', 'reported_by',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(None, 'lis_orders', type_='foreignkey')
    op.drop_column('lis_orders', 'test_id')
    # ### end Alembic commands ###