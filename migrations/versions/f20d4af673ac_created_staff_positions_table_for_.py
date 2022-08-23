"""created staff_positions table for collect staff_position

Revision ID: f20d4af673ac
Revises: b3d6f4fe96e5
Create Date: 2022-07-08 12:19:06.174424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f20d4af673ac'
down_revision = 'b3d6f4fe96e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff_positions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('position', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('staff_positions')
    # ### end Alembic commands ###