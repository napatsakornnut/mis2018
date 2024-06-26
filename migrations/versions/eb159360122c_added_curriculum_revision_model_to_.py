"""added curriculum revision model to allow multiple versions of the same curriculumn

Revision ID: eb159360122c
Revises: 6f591970e8c4
Create Date: 2021-03-04 14:17:16.162420

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb159360122c'
down_revision = '6f591970e8c4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eduqa_curriculum_revisions',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('curriculum_id', sa.Integer(), nullable=True),
    sa.Column('revision_year', sa.Date(), nullable=False),
    sa.ForeignKeyConstraint(['curriculum_id'], ['eduqa_curriculums.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('eduqa_academic_staff',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('roles', sa.String(), nullable=True),
    sa.Column('curriculumn_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['curriculumn_id'], ['eduqa_curriculum_revisions.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'eduqa_curriculums', sa.Column('en_name', sa.String(), nullable=False))
    op.add_column(u'eduqa_curriculums', sa.Column('th_name', sa.String(), nullable=False))
    op.add_column(u'eduqa_programs', sa.Column('degree', sa.String(), nullable=False))
    op.drop_constraint(u'eduqa_programs_degree_id_fkey', 'eduqa_programs', type_='foreignkey')
    op.drop_column(u'eduqa_programs', 'degree_id')
    op.drop_table('eduqa_degrees')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('eduqa_degrees',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name=u'eduqa_degrees_pkey')
    )
    op.add_column(u'eduqa_programs', sa.Column('degree_id', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_foreign_key(u'eduqa_programs_degree_id_fkey', 'eduqa_programs', 'eduqa_degrees', ['degree_id'], ['id'])
    op.drop_column(u'eduqa_programs', 'degree')
    op.drop_column(u'eduqa_curriculums', 'th_name')
    op.drop_column(u'eduqa_curriculums', 'en_name')
    op.drop_table('eduqa_academic_staff')
    op.drop_table('eduqa_curriculum_revisions')
    # ### end Alembic commands ###
