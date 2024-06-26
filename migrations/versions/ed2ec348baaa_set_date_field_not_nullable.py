"""set date field not nullable

Revision ID: ed2ec348baaa
Revises: 526bfec2f5b8
Create Date: 2021-05-18 17:35:36.440415

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ed2ec348baaa'
down_revision = '526bfec2f5b8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('doc_rounds', 'date',
               existing_type=sa.DATE(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('doc_rounds', 'date',
               existing_type=sa.DATE(),
               nullable=True)
    # ### end Alembic commands ###
