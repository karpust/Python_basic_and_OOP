# Модуль OS предоставляет множество функций для работы с операционной системой, причем их
# поведение, как правило, не зависит от ОС, поэтому программы остаются переносимыми.
import os

os.name
os.getcwd()  # 'C:\\Users\\k\\PycharmProjects\\Python basic and OOP'
'''
os.chdir(path)
----------------------
смена текущей директории;

os.chmod(path, mode, *, dir_fd=None, follow_symlinks=True)
-----------------------------------------------------------------
смена прав доступа к объекту (mode — восьмеричное число);

os.chown(path, uid, gid, *, dir_fd=None, follow_symlinks=True)
---------------------------------------------------------------------
меняет id владельца и группы (Unix);

os.getcwd()
-------------------
текущая рабочая директория;

os.mkdir(path, mode=0o777, *, dir_fd=None)
--------------------------------------------------
создает директорию. OSError, если директория существует;

os.remove(path, *, dir_fd=None)
--------------------------------------
удаляет путь к файлу;

os.rename(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
---------------------------------------------------------------
переименовывает файл или директорию из src в dst;

os.renames(old, new)
----------------------------
переименовывает old в new, создавая промежуточные директории;

os.replace(src, dst, *, src_dir_fd=None, dst_dir_fd=None)
----------------------------------------------------------------
переименовывает из src в dst с принудительной заменой;

os.rmdir(path, *, dir_fd=None)
---------------------------------------
удаляет пустую директорию;

os.symlink(source, link_name, target_is_directory=False, *, dir_fd=None)
-----------------------------------------------------------------------------
создает символическую ссылку на объект;

os.urandom(n)
-----------------------
n случайных байт. Возможно использование этой функции в криптографических целях;

os.path
------------
модуль, реализующий некоторые полезные функции для работы с путями.

'''

