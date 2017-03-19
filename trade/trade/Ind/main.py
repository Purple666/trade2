#!python
# -*- coding: utf-8 -*-

import multiprocessing as mulp
import itertools as itrt

def main():
    tester = MultiTest()
    tester.execute()
    
class MultiTest(object):
    def func(self, n):
        return n ** 10
        
    def execute(self):
        pool = mulp.Pool(4)  # 引数に数字を入れると同時起動数。引数なしなら勝手にcpu情報見に行って最大プロセス数を割り当てる

        # 成功する関数版
        # args = itrt.izip(itrt.repeat(self), itrt.repeat('func'), range(10))
        # r = pool.map(tomap, args)

        # 成功する関数版2
        # r = pool.apply(toapply, (self, 'func', 2))

        # 成功するクラス版
        r = pool.map(MulHelper(self, 'func'), range(1000000))

        print('result:', r)

def tomap(args):
    return getattr(args[0], args[1])(*args[2:])

def toapply(cls, mtd_name, *args, **kwargs):
    return getattr(cls, mtd_name)(*args, **kwargs)

class MulHelper(object):
    def __init__(self, cls, mtd_name):
        self.cls = cls
        self.mtd_name = mtd_name

    def __call__(self, *args, **kwargs):
        return getattr(self.cls, self.mtd_name)(*args, **kwargs)

if __name__ == '__main__':
    main()