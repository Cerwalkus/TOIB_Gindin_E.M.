import hashlib
import itertools
import string

def brute_force_password(target_password_hash, characters, max_length):
    count = 0  

    for length in range(1, max_length + 1):  
        for combination in itertools.product(characters, repeat=length):
            candidate_password = ''.join(combination)
            candidate_password_hash = hashlib.sha256(candidate_password.encode()).hexdigest()
            
            count += 1  

            if count % 10000 == 0:
                print(f"Проверено паролей: {count}")

            if candidate_password_hash == target_password_hash:
                return candidate_password, count

    return None, count

if __name__ == "__main__":
    input("Программа готова к работе. Нажмите Enter для продолжения...")

    target_password = input("Введите пароль, который нужно подобрать (не более 8 символов): ")
    
    if len(target_password) > 8:
        print("Ошибка: длина пароля должна быть не более 8 символов.")
    else:
        target_password_hash = hashlib.sha256(target_password.encode()).hexdigest()

        print(f"Хеш пароля: {target_password_hash}")

        characters = string.ascii_letters + string.digits  # Заглавные и строчные буквы, цифры

        max_length = 8

        input("Нажмите Enter, чтобы начать подбор пароля...")

        result, checked_count = brute_force_password(target_password_hash, characters, max_length)

        if result:
            print(f"Пароль найден: {result}")
            print(f"Всего проверено паролей: {checked_count}")
        else:
            print("Пароль не найден в указанном диапазоне.")
            print(f"Всего проверено паролей: {checked_count}")