===============================================
GetFEMによるElliptic Membraneベンチマークテスト
===============================================

.. 小山です。
   GetFEMによるElliptic Membraneベンチマークテストというタイトルでお話をさせていただきます。

背景
====

.. まずは、背景について説明させていだきます。
   現在、FEABerというプロジェクトに参加しています。
   このプロジェクトは複数のオープンソースプロジェクトの
   FEAコードをベンチマークするプロジェクトです。
   参加プログラムにはCalculiX, Code-Aster, FrontISTR があります。
   ベンチマークテストは"The Standard NAFEMS Benchmarks"から引用しています。
   その際にPythonスクリプトを使用していますが、今回はそれらについても解説する予定です。

問題の説明
==========

.. 今回対象とした問題はThe Standard NAFEMS BenchmarksにLE1として掲載されている問題です。
   圧力を負荷された楕円形状に発生する応力を確認するベンチマークになっています。

メッシュ図
==========

ベンチマークに使用するメッシュパターンは粗いメッシュと細いメッシュの2種類としました。
使用した要素は1次要素、2次要素およびそれらの低減要素です。

.. tabs::

   .. tab:: 粗い4角形1次要素

      .. figure:: coarse-quadrilateron-1d.png
         :align: center
         :scale: 50

   .. tab:: 粗い4角形2次要素

      .. figure:: coarse-quadrilateron-2d.png
         :align: center
         :scale: 50

   .. tab:: 粗い3角形1次要素

      .. figure:: coarse-triangle-1d.png
         :align: center
         :scale: 50

   .. tab:: 粗い3角形2次要素

      .. figure:: coarse-triangle-2d.png
         :align: center
         :scale: 50

   .. tab:: 細い4角形1次要素

      .. figure:: fine-quadrilateron-1d.png
         :align: center
         :scale: 50

   .. tab:: 細い4角形2次要素

      .. figure:: fine-quadrilateron-2d.png
         :align: center
         :scale: 50

   .. tab:: 細い3角形1次要素

      .. figure:: fine-triangle-1d.png
         :align: center
         :scale: 50

   .. tab:: 細い3角形2次要素

      .. figure:: fine-triangle-2d.png
         :align: center
         :scale: 50

   .. tab:: Pythonスクリプト

      このメッシュはPyVistaを使用したPythonスクリプトで描画しています。

      .. literalinclude:: coarse-quadrilateron-1d.py
         :linenos:
         :lines: 43-62


細いメッシュ
------------

.. 細いメッシュのメッシュはこちらの通りです。
   todo::タブを使用してスクリプトとメッシュを表示する。

メッシュ作成
============

.. これらのメッシュをどのように作成しているかを説明します。

1次要素
-------

2次要素
-------

荷重の検討
==========

荷重計算方法
------------

1次要素
-------

2次要素
-------

2次要素の荷重の調査
===================

正方形1要素
-----------

正方形3要素
-----------

正方形1要素斜め
---------------

正方形3要素斜め
---------------

中間節点位置を水平移動した場合
------------------------------

1次要素の解析結果
-----------------

まとめ
======

