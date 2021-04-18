"""made degrees and personal info a a one-to-many relationship

Revision ID: e19ce0373a4f
Revises: 7d048ab06595
Create Date: 2021-03-04 09:41:21.032186

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e19ce0373a4f'
down_revision = '7d048ab06595'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eduqa_degrees',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eduqa_programs',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('degree_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['degree_id'], ['eduqa_degrees.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eduqa_curriculums',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('program_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['program_id'], ['eduqa_programs.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'staff_edu_degree', sa.Column('personal_info_id', sa.Integer(), nullable=True))
    op.add_column(u'staff_edu_degree', sa.Column('received_date', sa.Date(), nullable=True))
    op.create_foreign_key(None, 'staff_edu_degree', 'staff_personal_info', ['personal_info_id'], ['id'])
    op.drop_constraint(u'staff_personal_info_highest_degree_id_fkey', 'staff_personal_info', type_='foreignkey')
    op.drop_column(u'staff_personal_info', 'highest_degree_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(u'staff_personal_info', sa.Column('highest_degree_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'staff_personal_info_highest_degree_id_fkey', 'staff_personal_info', 'staff_edu_degree', ['highest_degree_id'], ['id'])
    op.drop_constraint(None, 'staff_edu_degree', type_='foreignkey')
    op.drop_column(u'staff_edu_degree', 'received_date')
    op.drop_column(u'staff_edu_degree', 'personal_info_id')
    op.drop_table('eduqa_curriculums')
    op.drop_table('eduqa_programs')
    op.drop_table('eduqa_degrees')
    # ### end Alembic commands ###