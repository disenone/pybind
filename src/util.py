# -*- coding:utf-8 -*


class Config(dict):
    def __init__(self, *args, **kwargs):
        super(Config, self).__init__(*args, **kwargs)
        self.__dict__ = self


libclang = None
TranslationUnit = None
Cursor = None


def InitLibclang():
    from config import config
    import sys
    sys.path.insert(0, config.libclang_path)

    from clang import cindex
    cindex.conf.set_library_path(config.libclang_path)
    global libclang, TranslationUnit, Cursor
    libclang = cindex
    TranslationUnit = cindex.TranslationUnit
    Cursor = cindex.Cursor


def GetTranslationUnit(file, compile_flags=None, options=None):
    compile_flags = list(compile_flags) if compile_flags else []
    options = options if options else 0
    return libclang.TranslationUnit.from_source(file, compile_flags, options=options)


def GetCursor(source, spelling):
    root_cursor = source if isinstance(source, Cursor) else source.cursor

    for cursor in root_cursor.walk_preorder():
        if cursor.spelling == spelling:
            return cursor

    return None


def GetCursors(source, spelling):
    root_cursor = source if isinstance(source, Cursor) else source.cursor

    cursors = []
    for cursor in root_cursor.walk_preorder():
        if cursor.spelling == spelling:
            cursors.append(cursor)

    return cursors
