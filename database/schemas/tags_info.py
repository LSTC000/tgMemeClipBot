import datetime

from database.database_setup import BaseModel

from sqlalchemy import Column, BigInteger, VARCHAR, Integer, DateTime, sql, func


class TagsInfo(BaseModel):
    __tablename__ = 'tags_info'

    # Auto increment id.
    id = Column(BigInteger, primary_key=True, autoincrement=True,
                server_default=sql.text('nextval(\'tags_info_id_seq\')'))
    # Tag name.
    tag_name = Column(VARCHAR(64), nullable=False)
    # Videos for tag.
    videos = Column(Integer, nullable=False)
    # Photo for tag.
    photo = Column(Integer, nullable=False)
    # Only text for tag.
    only_text = Column(Integer, nullable=False)
    # Likes for tag.
    likes = Column(Integer, nullable=False)
    # Dislikes for tag.
    dislikes = Column(Integer, nullable=False)
    # Number of approved complaints sent by the users.
    confirm_complaint = Column(Integer, nullable=False)
    # Created tag date.
    created_date = Column(DateTime(True), server_default=func.now())
    # Update tag date.
    updated_date = Column(
        DateTime(True),
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        server_default=func.now()
    )

    query: sql.select
