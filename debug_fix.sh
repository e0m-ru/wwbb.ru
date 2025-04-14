#!/bin/bash

FILE="djsite/settings.py"  # Путь к файлу

# Проверяем, есть ли строка "DEBUG = True"
if grep -q "DEBUG = True" "$FILE"; then
    echo "Найден DEBUG = True, меняем на False..."
    sed -i 's/DEBUG = True/DEBUG = False/' "$FILE"
    
    # Перезапускаем сервис (если нужно sudo, см. ниже)
    systemctl restart wwbb.service
    echo "Сервис wwbb.service перезапущен."
else
    echo "DEBUG уже False, ничего не меняем."
fi
