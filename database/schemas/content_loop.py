import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, TEXT, Integer, DateTime, sql, func


class ContentLoop(BaseModel):
    __tablename__ = 'content_loop'

    # Auto increment id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'content_loop_id_seq\')'))
    # Tag name.
    tag_name = Column(VARCHAR(64), nullable=False)
    # Telegram user id.
    user_id = Column(BigInteger, nullable=False)
    # Telegram user name.
    user_name = Column(VARCHAR(128), nullable=True)
    # Content type.
    type = Column(VARCHAR(16), nullable=False)
    # Video telegram id.
    video = Column(TEXT, nullable=True)
    # Photo telegram id.
    photo = Column(TEXT, nullable=True)
    # Content description.
    description = Column(TEXT, nullable=True)
    # Content likes.
    likes = Column(Integer, nullable=False)
    # Content dislikes.
    dislikes = Column(Integer, nullable=False)
    # Number of complaints sent by the users.
    complaint = Column(Integer, nullable=False)
    # Created content date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update content date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
