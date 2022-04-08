"""Added ProcurementRequire and Updated ProcurementMaintanance model

Revision ID: 6f8a43811e6d
Revises: 2d87a70b8b55
Create Date: 2022-01-11 17:26:40.107000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f8a43811e6d'
down_revision = '2d87a70b8b55'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('procurement_maintenances',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('repair_date', sa.Date(), nullable=True),
    sa.Column('detail', sa.Text(), nullable=True),
    sa.Column('note', sa.String(), nullable=True),
    sa.Column('type', sa.String(), nullable=True),
    sa.Column('company_name', sa.String(length=255), nullable=True),
    sa.Column('contact_name', sa.String(length=255), nullable=True),
    sa.Column('tel', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('company_des', sa.String(), nullable=True),
    sa.Column('require', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['staff_id'], ['staff_account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('procurement_requires',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('staff_id', sa.Integer(), nullable=False),
    sa.Column('service', sa.String(length=255), nullable=True),
    sa.Column('explan', sa.Text(), nullable=True),
    sa.Column('start_date', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['staff_id'], ['staff_account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_table('procurement_maintanances')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('procurement_maintanances',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('staff_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('service', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('explan', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('start_date', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('repair_date', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('detail', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('note', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('company_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('contact_name', sa.VARCHAR(length=255), autoincrement=False, nullable=True),
    sa.Column('tel', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('cost', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('company_des', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('require', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['staff_id'], [u'staff_account.id'], name=u'procurement_maintanances_staff_id_fkey'),
    sa.PrimaryKeyConstraint('id', name=u'procurement_maintanances_pkey')
    )
    op.drop_table('procurement_requires')
    op.drop_table('procurement_maintenances')
    # ### end Alembic commands ###