"""created new 2 columns verified_at and verified_by_account_id and verified_by relationship in ot_round_request

Revision ID: c6bd42254613
Revises: ab92db7ccb8e
Create Date: 2022-05-18 15:22:04.113502

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c6bd42254613'
down_revision = 'ab92db7ccb8e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('ot_round_request', sa.Column('verified_at', sa.DateTime(timezone=True), nullable=True))
    op.add_column('ot_round_request', sa.Column('verified_by_account_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'ot_round_request', 'staff_account', ['verified_by_account_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'ot_round_request', type_='foreignkey')
    op.drop_column('ot_round_request', 'verified_by_account_id')
    op.drop_column('ot_round_request', 'verified_at')
    # ### end Alembic commands ###
