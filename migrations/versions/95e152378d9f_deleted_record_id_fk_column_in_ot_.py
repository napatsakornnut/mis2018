"""deleted record_id fk column in ot_record_approval table

Revision ID: 95e152378d9f
Revises: d8bba556c410
Create Date: 2022-03-21 21:49:39.698886

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '95e152378d9f'
down_revision = 'd8bba556c410'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(u'ot_record_approval_record_id_fkey', 'ot_record_approval', type_='foreignkey')
    op.drop_column('ot_record_approval', 'record_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ot_record_approval', sa.Column('record_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'ot_record_approval_record_id_fkey', 'ot_record_approval', 'ot_record', ['record_id'], ['id'])
    # ### end Alembic commands ###
