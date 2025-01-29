import vk_api
import os
from djsite.settings import VK_SERVICE_KEY, VK_WWBB

def get_wall_posts():
    
    token = VK_SERVICE_KEY
    owner_id = VK_WWBB

    try:
        vk_session = vk_api.VkApi(token=token)
        vk = vk_session.get_api()

        response = vk.wall.get(owner_id=owner_id, count=100)

        if response and 'items' in response:
            return response['items']
        else:
            print("Не удалось получить посты.")
            return e 
    except vk_api.exceptions.ApiError as e:
        print(f"Произошла ошибка VK API: {e}")
        return owner_id
    except Exception as e:
        print(f"Произошла непредвиденная ошибка: {e}")
        return e


if __name__ == '__main__':
    # Пример использования:
    user_id = 1  # ID пользователя Павла Дурова
    group_id = -1  # ID группы VK (например, официальная группа VK)

    # Получаем 5 последних постов со стены пользователя
    user_posts = get_wall_posts(owner_id=user_id, count=5)
    if user_posts:
        print(f"Посты пользователя {user_id}:")
        for post in user_posts:
            print(f"  - {post.get('text', '[Без текста]')}")
            print("-" * 30)

    # Получаем 3 последних поста со стены группы
    group_posts = get_wall_posts(owner_id=group_id, count=3)
    if group_posts:
        print(f"\nПосты группы {group_id}:")
        for post in group_posts:
            print(f"  - {post.get('text', '[Без текста]')}")
            print("-" * 30)


