"""Added cost center iocode assoc in IOCode model

Revision ID: a7e185660373
Revises: 8c8ef2c96a89
Create Date: 2022-11-18 17:49:12.428000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a7e185660373'
down_revision = '8c8ef2c96a89'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cost_center_iocode_assoc',
    sa.Column('cost_center_id', sa.String(), nullable=False),
    sa.Column('iocode_id', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['cost_center_id'], ['cost_centers.id'], ),
    sa.ForeignKeyConstraint(['iocode_id'], ['iocodes.id'], ),
    sa.PrimaryKeyConstraint('cost_center_id', 'iocode_id')
    )
    op.drop_constraint(u'iocodes_cost_center_id_fkey', 'iocodes', type_='foreignkey')
    op.drop_column(u'iocodes', 'cost_center_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'iocodes', sa.Column('cost_center_id', sa.VARCHAR(), autoincrement=False, nullable=False))
    op.create_foreign_key(u'iocodes_cost_center_id_fkey', 'iocodes', 'cost_centers', ['cost_center_id'], ['id'])
    op.drop_table('cost_center_iocode_assoc')
    # ### end Alembic commands ###
