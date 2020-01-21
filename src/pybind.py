# -*- coding:utf-8 -*
import os
import sys

import util


def GetAllHeader(folder):
    files = []
    for dirpath, dirnames, filenames in os.walk(folder):
        for file in filenames:
            if file.endswith('.h') or file.endswith('.hpp'):
                files.append(os.path.join(dirpath, file))
    return files


class PyBind(object):
    def __init__(self, folder):
        self.folder = folder

    def Start(self):
        util.InitLibclang()
        files = GetAllHeader(self.folder)

        for file in files:
            self.ParseOneFile(file)

    # TODO: 改并行
    def ParseOneFile(self, file):
        tu = util.GetTranslationUnit(file, options=util.TranslationUnit.PARSE_SKIP_FUNCTION_BODIES)
        if not tu:
            print('file not found: {}'.format(file), file=sys.stderr)
            return
        else:
            print('file loaded: {}'.format(file))

        for child in tu.cursor.get_children():
            if child.kind == util.libclang.CursorKind.INCLUSION_DIRECTIVE:
                print(child.spelling)

        for cursor in tu.cursor.walk_preorder():
            print(cursor.kind, cursor.spelling)