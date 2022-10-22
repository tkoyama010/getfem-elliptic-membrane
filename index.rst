===============================================
GetFEMによるElliptic Membraneベンチマークテスト
===============================================

GetFEMによるElliptic Membraneベンチマークテストというタイトルでお話をさせていただきます。

背景
====

まずは、背景について説明させていだきます。
現在、FEABerというプロジェクトに参加しています。
このプロジェクトは複数のオープンソースプロジェクトの
FEAコードをベンチマークするプロジェクトです。
ベンチマークテストは `The Standard NAFEMS Benchmarks <http://www.caesarsystems.co.uk/NAFEMS_benchmarks/le1.html>`_ から引用しています。
参加プログラムにはCalculiX, Code-Aster, FrontISTR があります。
この発表ではそれらの結果とGetFEMの結果を比べた途中経過を報告したいと思います。
ベンチマークテストの解析にPythonスクリプトを使用していますが、今回はそれらについても詳細に解説いたします。

問題の説明
==========

今回対象とした問題は The Standard NAFEMS Benchmarks に `LE1 <http://www.caesarsystems.co.uk/NAFEMS_benchmarks/le1.html>`_ として掲載されている問題です。
圧力を負荷された楕円形状に発生する応力を確認するベンチマークになっています。

.. image:: http://www.caesarsystems.co.uk/NAFEMS_benchmarks/le1_1.gif
   :align: center
   :alt: モデル図

入力する物性値は次の通りです。

.. table:: 入力した材料物性

   ========== ==========
   材料物性   入力値
   ========== ==========
   ヤング率   210000 MPa
   ポアソン比 0.3
   要素種別    平面応力要素
   厚さ       0.1 mm
   ========== ==========

メッシュ作成
============

ベンチマークに使用するメッシュパターンは粗いメッシュと細いメッシュの2種類です。
使用した要素は1次要素、2次要素およびそれらの低減要素です。
粗いメッシュと細いメッシュ図は以下の通りです。

.. tabs::

   .. tab:: 粗いメッシュ

       .. image:: http://www.caesarsystems.co.uk/NAFEMS_benchmarks/le1_2.gif
           :align: center
           :alt: 粗いメッシュ

   .. tab:: 細いメッシュ

       .. image:: http://www.caesarsystems.co.uk/NAFEMS_benchmarks/le1_3.gif
           :align: center
           :alt: 細いメッシュ

これらのメッシュをどのように作成しているかを説明します。
まず、GetFEMとNumPyをインポートして空の2次元メッシュを作成します。

.. literalinclude:: coarse-quadrilateron-1d.py
   :linenos:
   :lines: 1-4

次に幾何変換のオブジェクトを定義します。
``GT_QK(2,1)`` は2次元の1次4角形(quadrangle)幾何変換を表しています。

.. literalinclude:: coarse-quadrilateron-1d.py
   :linenos:
   :lines: 5-5

変数 ``x`` と変数 ``y`` に節点の座標を定義しておき要素の節点番号の構成を定義します。

.. literalinclude:: coarse-quadrilateron-1d.py
   :linenos:
   :lines: 34-39

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

      メッシュはPyVistaを使用したPythonスクリプトで描画しています。

      .. literalinclude:: coarse-quadrilateron-1d.py
         :linenos:
         :lines: 43-62

荷重の検討
==========

今回は検討として等価節点荷重の比較を行いました。
1次要素は参照値との相対誤差が0.01%でした。

.. tabs::

   .. tab:: 粗い4角形1次要素の等価節点荷重(GetFEM)
       .. figure:: coarse-quadrilateron-1d-02.png
          :align: center
          :scale: 50

       .. table::

          ================ ================ ================== ================ ==================
          荷重負荷点       X方向荷重        参照値との相対誤差 Y方向荷重        参照値との相対誤差
          ================ ================ ================== ================ ==================
          P1               0.22539711         0.01%            0.89149999         0.01%
          P2               0.70099997         0.00%            1.41638279         0.01%
          P3               1.14960289         0.00%            0.73350000         0.00%
          P4               0.67400002         0.00%            0.20861721         0.00%
          ================ ================ ================== ================ ==================

   .. tab:: 粗い4角形2次要素の等価節点荷重(GetFEM)
       .. figure:: coarse-quadrilateron-2d-02.png
          :align: center
          :scale: 50

       .. table::

          ================ ================ ================== ================ ==================
          荷重負荷点       X方向荷重        参照値との相対誤差 Y方向荷重        参照値との相対誤差
          ================ ================ ================== ================ ==================
          P1               1.60599000e-03     97.88%            3.23130648e-01    7.88%
          P2               3.00529480e-01      0.79%            1.18866666e+00    0.79%
          P3               2.71656828e-01     13.35%            4.91136831e-01    3.23%
          P4               6.34137153e-01      0.71%            6.99843727e-01    0.71%
          P5               4.03582216e-01      4.34%            2.67912545e-01    8.68%
          P6               8.98666700e-01      1.08%            2.78156280e-01    1.08%
          P7               2.39821632e-01      5.59%            1.15331000e-03   98.36%
          ================ ================ ================== ================ ==================

等価節点力の計算方法
====================

等価節点力は仮想変位 :math:`\delta u\left(\eta \right)` と仮想仕事 :math:`\delta W` の関係から計算されます。

.. math::
    \delta W=ph\int _0^1\delta u\left(\eta \right)d\eta 

ただし、 :math:`p` は分布荷重の値、 :math:`h` は要素厚さ :math:`\eta (0 \leqq \eta \leqq 1)` は分布荷重が加わる面の接線方向座標とします。

.. tabs::

   .. tab:: 1次要素

       1次要素の場合、変位は次の式で与えられます。

       .. math::
           \delta u\left(\eta \right)=\left\{N\left(\eta \right)\right\}^T\left\{U\right\}=\begin{Bmatrix}1-\eta &\eta \end{Bmatrix}\begin{Bmatrix}\delta u_1\\\delta u_2\end{Bmatrix}

       ただし、 :math:`u_1` と :math:`u_2` はそれぞれ :math:`\eta = 0` と :math:`\eta = 1` の節点における変位です。

       この式を仮想変位の式に代入すると以下の式が得られます。

       .. math::
          \delta W=ph\left(\frac{1}{2}\delta u_1+\frac{1}{2}\delta u_2\right)


   .. tab:: 2次要素

       2次要素の場合、変位は次の式で与えられます。

       .. math::
           \delta u\left(\eta \right)=\left\{N\left(\eta \right)\right\}^T\left\{U\right\}=\begin{Bmatrix}2\left(\eta -\frac{1}{2}\right)\left(\eta -1\right)&-4\eta \left(\eta -1\right)&2\eta \left(\eta -\frac{1}{2}\right)\end{Bmatrix}\begin{Bmatrix}\delta u_1\\\delta u_2\\\delta u_3\end{Bmatrix}

       この式を仮想変位の式に代入すると以下の式が得られます。

       .. math::
           \delta W=ph\left(\frac{1}{6}\delta u_1+\frac{4}{6}\delta u_2+\frac{1}{6}\delta u_3\right)

まとめ
======

* GetFEMの機能を使用して The Standard NAFEMS Benchmarks のメッシュを作成できることを確認しました。
* GetFEMを使用して等価節点荷重の値を計算しました。1次要素は参照値との相対誤差が0.01%以下でした。2次要素は参照値との相対誤差が0.50%以上98%以下でした。
* 等価節点力の計算方法について定式化を確認しました。
* 今後は単純なモデルで2次要素の等価節点荷重について確認をする予定です。
