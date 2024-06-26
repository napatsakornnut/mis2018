"""deleted staff_attend_assoc table which collected list of attendee in staff_seminar_attends record

Revision ID: 2988a9a1005c
Revises: d89c3a0fc59d
Create Date: 2022-08-16 14:05:00.430564

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2988a9a1005c'
down_revision = 'd89c3a0fc59d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('staff_attend_assoc')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff_attend_assoc',
    sa.Column('staff_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('attend_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['attend_id'], [u'staff_seminar_attends.id'], name=u'staff_attend_assoc_attend_id_fkey'),
    sa.ForeignKeyConstraint(['staff_id'], [u'staff_account.id'], name=u'staff_attend_assoc_staff_id_fkey'),
    sa.PrimaryKeyConstraint('staff_id', 'attend_id', name=u'staff_attend_assoc_pkey')
    )
    # ### end Alembic commands ###
