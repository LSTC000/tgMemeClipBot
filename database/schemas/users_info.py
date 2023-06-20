import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, Integer, DateTime, sql, func


class UsersInfo(BaseModel):
    __tablename__ = 'users_info'

    # Auto increment id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'users_info_id_seq\')'))
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # Viewed user memes.
    viewed_memes = Column(Integer, nullable=False)
    # Posted user memes.
    posted_memes = Column(Integer, nullable=False)
    # Likes that the user has received from other users.
    own_likes = Column(Integer, nullable=False)
    # Dislikes that the user has received from other users.
    own_dislikes = Column(Integer, nullable=False)
    # Likes that the user has put.
    other_likes = Column(Integer, nullable=False)
    # Dislikes that the user has put.
    other_dislikes = Column(Integer, nullable=False)
    # Number of approved complaints sent by the user.
    own_confirm_complaint = Column(Integer, nullable=False)
    # Number of approved complaints sent by other users.
    other_confirm_complaint = Column(Integer, nullable=False)
    # Created user date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update user date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
