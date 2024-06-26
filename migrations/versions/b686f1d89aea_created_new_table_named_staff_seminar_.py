"""created new table named staff_seminar_documents

Revision ID: b686f1d89aea
Revises: bf58e74ef23d
Create Date: 2023-05-31 13:20:03.060981

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b686f1d89aea'
down_revision = 'bf58e74ef23d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('staff_seminar_documents',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('seminar_proposal_id', sa.Integer(), nullable=True),
    sa.Column('document_no', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['seminar_proposal_id'], ['staff_seminar_proposals.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column(u'doc_orgs', sa.Column('detail', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column(u'doc_orgs', 'detail')
    op.drop_table('staff_seminar_documents')
    # ### end Alembic commands ###
