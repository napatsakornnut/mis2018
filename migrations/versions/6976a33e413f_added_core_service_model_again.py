"""added core service model again

Revision ID: 6976a33e413f
Revises: 8e801061f6c3
Create Date: 2022-02-23 04:28:39.291364

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6976a33e413f'
down_revision = '8e801061f6c3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('db_core_services',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('service', sa.String(length=255), nullable=False),
    sa.Column('mission_id', sa.Integer(), nullable=True),
    sa.Column('creator_id', sa.Integer(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), nullable=True),
    sa.ForeignKeyConstraint(['creator_id'], ['staff_account.id'], ),
    sa.ForeignKeyConstraint(['mission_id'], ['missions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('db_core_services')
    # ### end Alembic commands ###