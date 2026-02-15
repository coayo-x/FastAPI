from sqlalchemy import select
from sqlalchemy.orm import Session

from models.token_blacklist import TokenBlacklist


def blacklist_token(db: Session, token: str) -> TokenBlacklist:
    entry = TokenBlacklist(token=token)
    db.add(entry)
    db.commit()
    db.refresh(entry)
    return entry


def is_token_blacklisted(db: Session, token: str) -> bool:
    return db.scalar(select(TokenBlacklist).where(TokenBlacklist.token == token)) is not None
