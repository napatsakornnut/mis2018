"""removed unused fields from KPI model

Revision ID: 1b936e3ffa98
Revises: 937bf7807ea1
Create Date: 2024-01-29 19:20:59.905176

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1b936e3ffa98'
down_revision = '937bf7807ea1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('kpi_cascades',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('kpi_id', sa.Integer(), nullable=True),
    sa.Column('parent_id', sa.Integer(), nullable=True),
    sa.Column('goal', sa.String(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['kpi_id'], ['kpis.id'], ),
    sa.ForeignKeyConstraint(['parent_id'], ['kpi_cascades.id'], ),
    sa.ForeignKeyConstraint(['staff_id'], ['staff_account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    with op.batch_alter_table('kpis', schema=None) as batch_op:
        batch_op.drop_constraint('kpis_parent_kpi_id_fkey', type_='foreignkey')
        batch_op.drop_column('parent_kpi_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('kpis', schema=None) as batch_op:
        batch_op.add_column(sa.Column('parent_kpi_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('kpis_parent_kpi_id_fkey', 'kpis', ['parent_kpi_id'], ['id'])

    op.drop_table('kpi_cascades')
    # ### end Alembic commands ###