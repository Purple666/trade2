機械学習（ランダムフォレスト）を使用したFXトレードサンプル

使用ツール

Anaconda・・・機械学習ライブラリー及びPython3

  https://www.continuum.io/downloads

TA-LIB・・・・ローソク足--->MA.Rsi等の指標算出

  http://mrjbq7.github.io/ta-lib/install.html

Python-MySQL・・・MySQL操作

  http://www.python-izm.com/contents/external/mysql.shtml


◎このサンプルソースは以下について掲載しております。

※機械学習（参照・・・main2.py)

１．PythoからMySQLのFXのローソク足

２．FXのローソク足を元にTA-LIB及び一目均衡表を元にした指標算出

３．指標値を元にxx期間のパターン算出

４．機械学習用データの正則化及び未来xx期間の値のラベル付け

５．ランダムフォレストによる機械学習

６．機械学習結果のシリアライズ


※学習結果の利用（参照・・・trade.py)

１．シリアライズ結果の読み込み

２．MySQLよりFXのローソク足の取得

３．FXのローソク足を元にTA-LIB及び一目均衡表を元にした指標、値動きパターン算出

４．予測結果をMySQLへ書き込み

