"""empty message

Revision ID: c220d07f07cf
Revises: 973914b9b2e5
Create Date: 2021-01-30 15:35:00.741487

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c220d07f07cf'
down_revision = '973914b9b2e5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tweets',
    sa.Column('tweet_id', sa.BigInteger(), nullable=False),
    sa.Column('tweet', sa.String(), nullable=True),
    sa.Column('tweet_sentiment', sa.Integer(), nullable=True),
    sa.Column('tweet_name', sa.String(), nullable=True),
    sa.Column('tweet_username', sa.String(), nullable=True),
    sa.Column('tweet_likes', sa.Integer(), nullable=True),
    sa.Column('tweet_datestamp', sa.Date(), nullable=True),
    sa.Column('day1Price', sa.Float(), nullable=True),
    sa.Column('day2Price', sa.Float(), nullable=True),
    sa.Column('day3Price', sa.Float(), nullable=True),
    sa.Column('day4Price', sa.Float(), nullable=True),
    sa.Column('day5Price', sa.Float(), nullable=True),
    sa.Column('day1', sa.String(), nullable=True),
    sa.Column('day2', sa.String(), nullable=True),
    sa.Column('day3', sa.String(), nullable=True),
    sa.Column('day4', sa.String(), nullable=True),
    sa.Column('day5', sa.String(), nullable=True),
    sa.Column('company', sa.String(), nullable=True),
    sa.Column('numOfTweets', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('tweet_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tweets')
    # ### end Alembic commands ###
