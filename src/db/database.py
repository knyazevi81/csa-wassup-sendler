#from models import User, Club, db, DoesNotExist
from db.models import User, db
from config import ROOT_USER

def check_user(telegram_id: int) -> bool:
    """
    Проверка юзера на существование
    """
    try:
        data = User.get(User.user_id==telegram_id)
        return data == 1
    except:
        return False

async def add_user(user_id: int,  name: str, status: str) -> bool:
    if True:
        data = User.select(user_id, name).where(user_id=user_id)
        print(data)
        User(
            user_id=user_id,
            status=status
        ).save()
        db.close()
    return True

def get_user_info():
    
    pass
