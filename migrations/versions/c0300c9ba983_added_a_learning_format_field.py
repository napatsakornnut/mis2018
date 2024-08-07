"""added a learning format field

Revision ID: c0300c9ba983
Revises: ea2409755ae7
Create Date: 2022-12-07 04:41:51.219984

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c0300c9ba983'
down_revision = 'ea2409755ae7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('eduqa_course_session_detail_role_items', sa.Column('format', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('eduqa_course_session_detail_role_items', 'format')
    # ### end Alembic commands ###
