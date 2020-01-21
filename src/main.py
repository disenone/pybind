# -*- coding:utf-8 -*

from pybind import PyBind


def run():
    cfolder = r'd:\libs\llvm-project\clang\bindings\python'
    pb = PyBind(cfolder)
    pb.Start()


if __name__ == '__main__':
    run()
