"""create item_id column in pa_score_sheet_item table

Revision ID: 50d838e3251f
Revises: 1f3303650047
Create Date: 2023-06-16 08:04:19.991499

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '50d838e3251f'
down_revision = '1f3303650047'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pa_score_sheet_items', schema=None) as batch_op:
        batch_op.add_column(sa.Column('item_id', sa.Integer(), nullable=True))
        batch_op.create_foreign_key(None, 'pa_items', ['item_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('pa_score_sheet_items', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_column('item_id')

    # ### end Alembic commands ###
