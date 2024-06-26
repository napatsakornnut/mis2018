"""deleted evaluator_id in pa_score_sheets table

Revision ID: 184117bbe4d7
Revises: df9375f0daac
Create Date: 2023-06-19 11:45:17.645628

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '184117bbe4d7'
down_revision = 'df9375f0daac'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pa_score_sheets', schema=None) as batch_op:
        batch_op.drop_constraint('pa_score_sheets_evaluator_id_fkey', type_='foreignkey')
        batch_op.drop_column('evaluator_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pa_score_sheets', schema=None) as batch_op:
        batch_op.add_column(sa.Column('evaluator_id', sa.INTEGER(), autoincrement=False, nullable=True))
        batch_op.create_foreign_key('pa_score_sheets_evaluator_id_fkey', 'staff_account', ['evaluator_id'], ['id'])

    # ### end Alembic commands ###
