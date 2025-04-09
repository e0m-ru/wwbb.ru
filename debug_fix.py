#!/usr/bin/env python3
import re
import sys

def replace_debug_flag(file_path):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
        
        new_content = re.sub(r'DEBUG\s*=\s*True', 'DEBUG = False', content)
        
        if new_content != content:
            with open(file_path, 'w') as file:
                file.write(new_content)
            print(f"Обновлено DEBUG=False в {file_path}")
            return True
        else:
            print("DEBUG=True не найден или уже False")
            return False
    
    except Exception as e:
        print(f"Ошибка: {e}", file=sys.stderr)
        return False

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Использование: ./debug_fix.py /путь/к/файлу.py", file=sys.stderr)
        sys.exit(1)
    
    file_path = sys.argv[1]
    replace_debug_flag(file_path)