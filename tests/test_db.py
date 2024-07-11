from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    user = User(
        username='filipe', email='filipe@mail.com', password='senha-123'
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    result = session.scalar(
        select(User).where(User.email == 'filipe@mail.com')
    )

    assert result.username == 'filipe'
