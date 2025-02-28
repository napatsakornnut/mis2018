"""Added ServiceSample model

Revision ID: 165ba4716aed
Revises: 088b5cbb87bb
Create Date: 2025-02-05 10:04:19.824358

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '165ba4716aed'
down_revision = '088b5cbb87bb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('service_samples',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('appointment_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('ship_type', sa.String(), nullable=True),
    sa.Column('location', sa.String(), nullable=True),
    sa.Column('tracking_number', sa.String(), nullable=True),
    sa.Column('received_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('receiver_id', sa.Integer(), nullable=True),
    sa.Column('expected_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('started_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('starter_id', sa.Integer(), nullable=True),
    sa.Column('finished_at', sa.DateTime(timezone=True), nullable=True),
    sa.Column('finish_id', sa.Integer(), nullable=True),
    sa.Column('request_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['finish_id'], ['staff_account.id'], ),
    sa.ForeignKeyConstraint(['receiver_id'], ['staff_account.id'], ),
    sa.ForeignKeyConstraint(['request_id'], ['service_requests.id'], ),
    sa.ForeignKeyConstraint(['starter_id'], ['staff_account.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('service_samples')
    # ### end Alembic commands ###
