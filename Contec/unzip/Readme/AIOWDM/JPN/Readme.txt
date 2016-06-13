=====================================================================
=           Windows版アナログ入出力用ドライバについて               =
=                                             API-AIO(WDM) Ver4.72  =
=                                                  CONTEC Co.,Ltd.  =
=====================================================================

◆ 目次
=======
  はじめに
  注意事項
  インストール方法
  インストールされるファイル
  サンプルプログラム
  バージョンアップ履歴


◆ はじめに
===========
  日頃から格別のお引き立てを賜りまして厚く御礼申し上げます。

  ここにはAPI-AIO(WDM)に関する補足説明を記載しています。
  API-AIO(WDM)の使用方法は、オンラインヘルプ(APITOOL.CHM)
  を参照ください。


◆注意事項
==========
  API-AIO(WDM)は、従来版アナログ入出力用ドライバとは異なる製品です。
  両者製品の違いに関しては、オンラインヘルプ(API-AIO(WDM).CHM)
  をご参照ください。

  C++ Builderサンプルのコンパイルに関して
  C++ Builderでは、パスに"-"(ハイフン)を含んでいるとビルドに失敗します。
  API-AIO(WDM)をデフォルトでインストールした場合、
  パスに「API-PAC(W32)」が含まれるため、そのままでは使用できません。
  サンプルプロジェクトが含まれるフォルダを、
  パスにハイフンが含まれない場所へコピーしてビルドを行ってください。

  以下のケースでは、バスマスタ用バッファが最大1MByte以下に制限されます。

  <4GByte以上のメモリ搭載時>
  Windows 64bit版 および Windows 32bit版 で、PAE(物理アドレス拡張) 有効の場合

  <4GByte未満のメモリ搭載時>
  Windows 64bit版 もしくは Windows 32bit版 で、PAE(物理アドレス拡張) が有効であり
  ボードを実装するPC(マザーボード)のBIOS設定で、[Memory Reclaiming] 機能が有効の場合

  ※PC(マザーボード)によっては、BIOS設定で、[Memory Reclaiming] 機能の有効・無効が変更できない
  ケースもありますので、事前にご確認頂きますようお願いいたします。

  対象デバイス
  AIO-163202F-PE, ADA16-32/2(PCI)F, AI-1204Z-PCI, ADA16-32/2(CB)F


◆インストール方法
==================
  ・開発環境(ヘルプ、サンプル、ツール等)のインストール

    古いバージョンの開発環境がインストールされている場合、
    先に「コントロールパネル」からアンインストールを行ってください。

    <WEBダウンロードファイルからインストールする場合>
      ダウンロードファイルを解凍して、以下のセットアップを実行します。
      Apipac\AioWdm\Disk1\Setup.exe

    <API-PAC(W32) CD-ROMからインストールする場合>
      Autorun.exeからインストールを行ってください。

  ・デバイスドライバのインストール

    古いバージョンのドライバがインストールされている場合、
    先にアンインストールを行ってください。

    <WEBダウンロードファイルからインストールする場合>
      アンインストールならびにインストールの手順については、
      ダウンロードファイル解凍後に作成される以下のヘルプを参照してください。
      Help\AIOWDM\JPN\Apitool.chm

    <API-PAC(W32) CD-ROMからインストールする場合>
      アンインストールならびにインストールの手順については、
      API-PAC(W32) CD-ROM内の以下のヘルプを参照してください。
      <CD-ROM>\Apipac\Help\Hwinst\Jpn\Apitool.chm


◆インストールされるファイル
============================
  ・本製品のセットアッププログラムは、次の様な構成で ファイルをシステ
    ムディレクトリあるいは、ユーザー指定のディレクトリにインストール
    します。
  ・また、既に他のAPI-TOOLドライバがインストールされている場合は、そ
    のディレクトリへインストールします。

  \<User Directory>
    CONTEC.ICO                    アイコンファイル
    CONTEC_APIPACW32_HOMEPAGE.URL API-PAC(W32)HPへのショートカット
    AIOWDM\API-AIO(WDM).CHM       ヘルプファイル
    AIOWDM\README.TXT             このファイル
    AIOWDM\SAMPLES\               サンプルプログラム
    AIOWDM\SAMPLES\EXE            サンプルプログラムの実行ファイル
    AIOWDM\UTILITY                ユーティリティプログラム


◆サンプルプログラム
====================
  サンプルプログラムは、各言語ごとに以下のディレクトリで構成されてい
  ます｡

  ・32ビット版API-AIO(WDM)
    \<User Directory>
    |
    +--\AIOWDM
       |
       +--\SAMPLES
          |
          +--\INC       各言語用インクルードファイル
          |
          +--\LIB_I386  32bit版ライブラリファイル
          |
          +--\MODULE    各言語用サブルーチンファイル
          |
          +--\VB6       Visual Basic 6.0用サンプルプログラム
          |
          +--\VBNET     Visual Basic .Net用サンプルプログラム
          |
          +--\VC6       Visual C++ 6.0用サンプルプログラム
          |
          +--\VCNET     Visual C++ .Net用サンプルプログラム
          |
          +--\VCNET2005 Visual C++ .Net用サンプルプログラム
          |
          +--\VCNET2013 Visual C++ .Net用サンプルプログラム
          |
          +--\VCNETCLI  Visual C++ .Net(C++/CLI)用サンプルプログラム
          |
          +--\VCS       Visual C# .Net用サンプルプログラム
          |
          +--\BUILDER5  C++ Builder 5用サンプル
          |
          +--\DELPHI5   Delphi 5用サンプル
          |
          +--\CONSOLE   Visual C++ 6.0コンソールサンプル

  ・64ビット版API-AIO(WDM)
    \<User Directory>
    |
    +--\AIOWDM
       |
       +--\SAMPLES
          |
          +--\INC       各言語用インクルードファイル
          |
          +--\LIB_I386  32bit版ライブラリファイル
          |
          +--\LIB_amd64 64bit版ライブラリファイル
          |
          +--\MODULE    各言語用サブルーチンファイル
          |
          +--\VBNET     Visual Basic .Net用サンプルプログラム
          |
          +--\VCNET2005 Visual C++ .Net用サンプルプログラム
          |
          +--\VCNET2013 Visual C++ .Net用サンプルプログラム
          |
          +--\VCNETCLI  Visual C++ .Net(C++/CLI)用サンプルプログラム
          |
          +--\VCS       Visual C# .Net用サンプルプログラム


◆バージョンアップ履歴
=======================

  ※Fシリーズ：ADA16-32/2(PCI)F, ADA16-32/2(CB)F, AIO-163202F-PE
    Lシリーズ：ADA16-8/2(LPCI)L, ADA16-8/2(CB)L,
               AD16-64(LPCI)LA, AD16-16(LPCI)L,
               DA16-16(LPCI)L, DA16-8(LPCI)L, DA16-4(LPCI)L
               ADAI16-8/2(LPCI)L, ADI16-16(LPCI)L, DAI16-4(LPCI)L,
               AIO-160802L-LPE, AI-1616L-LPE, AO-1604L-LPE
               AIO-121602AH-PCI, AIO-121602AL-PCI
               AI-1216AH-PCI, AI-1216AL-PCI
               AIO-160802LI-PE, AI-1616LI-PE
               AO-1604LI-PE, AI-1664LA-LPE
               AO-1608L-LPE, AO-1616L-LPE
    Eシリーズ：AD12-16(PCI)E, AD12-16U(PCI)E, AD12-16U(PCI)EH,
               AD16-16(PCI)E, AD16-16U(PCI)EH, ADI12-16(PCI),
               AD12-16(PCI)EV, AD12-16U(PCI)EV,
               AD16-16(PCI)EV, AD16-16U(PCI)EV
               AIO-121601E3-PE, AIO-121601UE3-PE
               AIO-161601E3-PE, AIO-161601UE3-PE
    Bシリーズ：AI-1216B-RB1-PCI, AI-1216B-RU1-PCI
    Zシリーズ：AI-1204Z-PCI
    Mシリーズ：AIO-121601M-PCI


  Ver4.71->Ver4.72 (Web Release)
  --------------------------------
  ・USBデバイスで特定のサンプリングクロックにおいてサンプリングクロックエラーが発生しない問題を修正
　・USBデバイスでアナログ出力を実行中にAioResetAoMemoryが実行できる問題を修正
　・校正プログラム(caiocal.exe)のバージョンを更新

  Ver4.70->Ver4.71 (Web Release)
  --------------------------------
  ・AO-1604LX-USBで外部クロックを立ち上がりに設定できない不具合を修正
　・USBデバイスを使用するWOW64にて、32bitアプリケーションを実行すると、AioInit関数でエラーコード10003が発生するのを修正。

  Ver4.603->Ver4.70 (Web Release)
  --------------------------------
  ・対応OSを追加
    対応OS: Microsoft Windows 10
            Microsoft Windows 10 x64 Edition
  ・F, Lシリーズで、カウント一致パルスが出力されない不具合を修正
  ・AIO-121601M-PCIにて、AioCntmReadStatusEx関数による汎用入力状態の取得
    及び、AioCntmInputDIByte関数 による汎用入力の読み込みが動作しない不具合を修正。
  ・L, MシリーズにてAioSetAoClockEdge関数によるエッジ設定が反映されない不具合を修正
  ・AIO-121602LN-USB, AIO-120802LN-USB, AIO-163202FX-USB, AI-1664LAX-USB, AO-1604LX-USB において
    比較カウント一致機能使用時に、動作が不安定になる不具合を修正。
  ・AYシリーズ、AIO-160802GY-USBにおいて、AioSetAiClockType関数、AioSetAiClockEdge関数
    の順で実行するとエッジ設定が反映されない不具合を修正

  Ver4.60->Ver4.603 (API-USBP(WDM) Ver4.70)
  --------------------------------
  ・新規デバイスサポート
    AIO-160802GY-USB
  ・AIO-163202FX-USBにおいて、AioGetAiStopTriggerCount関数にて、正常にサンプリング回数が取得できない不具合を修正

  Ver4.53->Ver4.60 (Ver.Dec.2014)
  --------------------------------
  ・対応OSを追加
    対応OS:       Microsoft Windows 8.1
                  Microsoft Windows 8.1 x64 Edition
  ・対応開発言語を追加
    対応開発言語: Microsoft Visual Basic 2013
                  Microsoft Visual C# 2013
                  Microsoft Visual C++ 2013
  ・日本語環境以外にて、エラーコード 28000 ～ 28032 の間に定義されているエラー文字列を、
    AioGetErrorString関数で取得できない不具合を修正
  ・AIO-163202FX-USBにおいて、AO デバイスバッファ RINGモード時に、AioStopAo関数実行時に処理が完了しない場合
    がある不具合を修正
  ・USBデバイスにおいて、AO デバイス動作終了イベント が、条件成立時に2回通知される場合がある不具合を修正
    (DAI12-4(USB)GY, DAI16-4(USB)を除く)

  Ver4.50->Ver4.53 (Web Release 2014/04)
  --------------------------------
  ・Fシリーズにおいて、FIFOモード使用時、バッファの最大値までサンプリングすると、
    サンプリング回数が0となりデータ取得ができない不具合を修正
  ・L, Mシリーズにおいて、AIのサンプリングでデバイス動作終了イベントが未設定の場合、
    ２度目のAioStartAi関数実行時に処理が完了しない不具合を修正
  ・L, Mシリーズにおいて、校正プログラムがフリーズする問題を修正

  Ver4.45->Ver4.50 (Web Release 2014/02)
  --------------------------------
  ・対応OSを追加
    対応OS:       Microsoft Windows 8
                  Microsoft Windows 8 x64 Edition
  ・対応開発言語を追加
    対応開発言語: Microsoft Visual Basic 2012
                  Microsoft Visual C# 2012
                  Microsoft Visual C++ 2012
  ・AI-1204Z-PCIにおいて、関数実行速度測定プログラムを4GByte以上のメモリを認識している環境にて、
    AioGetAiSamplingData関数の実行時間を計測する際に「AioStartAi: ユーザーバッファが
    設定されていません。」とのエラーが発生する場合がある不具合を修正
  ・Fシリーズ、AIO-121601M-PCIにおいて、変換開始条件にイベントコントローラ出力を
    指定している場合、開始トリガ待ちステータスが通知されないように修正
  ・サンプリング動作を正常に開始できない場合がある不具合を修正
  ・AioSetTmEvent関数、及びAioStartTmCount関数にて、20002エラーが発生する場合がある不具合を修正
  ・Lシリーズ、AIO-121601M-PCIにおいて、AIリピート機能が正常動作しない場合がある不具合を修正
  ・AI-1204Z-PCIにおいて、AioExit関数実行時に例外が発生する場合がある不具合を修正
  ・Lシリーズ、AIO-121601M-PCIにおいて、AO連続関数の使用後に、AioMultiAo関数、
    及びAioMultiAoEx関数による出力が正常に動作しない場合がある不具合を修正
  ・ドライバをアンインストールせずにUSBデバイスを取り外した場合、イベントログに「Contec USB Service」が
    開始できなかった旨のエラーが記録される不具合を修正。

  Ver4.36->Ver4.45 (Web Release 2013/11)
  --------------------------------
  ・カウンタ機能搭載USBデバイスにおいて、カウントのスタート、ストップを繰り返すと
    カウントできない場合がある不具合を修正
  ・AIO-163202FX-USBにて、AOのリピート中に回数終了以外で停止させた場合に、
    サンプリングクロックエラー(20000H)となる場合がある不具合を修正。
  ・F, Lシリーズにて、AO リピート ソフトウェアスタート に設定している場合に、
    リピートカウントがインクリメントしない不具合を修正
  ・AIO-163202FX-USBにて、AOリピート機能使用時に、指定した回数以上に
    リピートする場合が有る不具合を修正
  ・AioGetErrorString関数にて取得できる、戻り値12381、12382に対応する文字列の誤りを修正
  ・AI-1204Z-PCI にて「デバイス動作終了イベント」後に「指定サンプリング回数格納イベント」
    が発生する場合がある不具合を修正
  ・AYシリーズにてDO03への出力ができない不具合を修正
  ・簡易入出力関数実行時にブルースクリーンになる場合が有る不具合を修正(USBデバイス以外)

  Ver4.30->Ver4.35 (Ver.July.2013)
  --------------------------------
  ・Fシリーズ, Lシリーズにおいて、AOリピート機能が正常動作しない不具合を修正
  ・AioSetAoStopTrigger関数の引数に2を設定すると23260エラーが返る不具合を修正(Lシリーズ)
  ・AI-1664LAX-USB にてレベルトリガによるサンプリング開始が正常に行えない不具合を修正
  ・DA12-16(PCI), DA12-8(PCI), DA12-4(PCI), DAI16-4C(PCI)にて、
    AioStartAo→AioGetAoStatus→AioStopAoを繰り返すと、サンプリングクロックエラーが発生する
    場合がある不具合を修正。

  Ver4.27->Ver4.30
  --------------------------------
  ・DEMO DEVICE においてAioSetAiStopTimes、AioSetAiRangeAll関数を実行すると、
    ブルースクリーンが発生する場合がある不具合を修正。
  ・カウンタ機能を有さないUSBデバイスでAioGetCntMaxChannels関数を実行すると、
    カウンタ機能が存在しないにも関わらず CntMaxChannels=1 が返る不具合を修正。
  ・カウンタ機能を有するUSBデバイスにてAioResetProcess関数を実行すると、
    定義されていない不定値がエラーとして返る不具合を修正。
  ・AI, AO両方の機能を持つLシリーズにおいて、AI, AOの順にサンプリングを開始すると
    AIのサンプリング途中でステータスがビジーのまま停止する不具合を修正。
  ・AI-1204Z-PCIにおいて、SingleAi等のサンプルをデバッグモードで実行し、
    AioInit関数を実行後デバッガを強制終了するとブルースクリーンが発生する場合がある不具合を修正。

  Ver4.25->Ver4.27
  --------------------------------
  ・4GByte以上のメモリを認識している環境において、AioResetDevice関数を実行すると、
    エラーコード21985が発生する場合があるのを修正。
  ・AIO-163202FX-USBにて、AioInit関数もしくはAioResetDevice関数を実行時にパルス状の波形が
    出力される場合がある不具合を修正。

  Ver4.22->Ver4.25
  --------------------------------
  ・Windows98環境において、2回目のサンプリング開始時にエラーコード11460が発生する不具合を修正。
  ・AioGetAiSamplingData関数実行時、FIFOが空(取得データが0)の状態であっても
    エラーコード21584を返していなかったのを修正。

  Ver4.21->Ver4.22 (Web Release)
  --------------------------------
  ・複数のプロセスにおいて、AioResetProcess関数実行後にAio関数を実行すると、
    ブルースクリーンが発生する場合がある不具合を修正。

  Ver4.20->Ver4.21 (Web Release)
  --------------------------------
  ・Zシリーズ、Fシリーズにおいて、Windows 64bit版、4GByte以上のメモリを搭載しているPCで、
    バッファを1MByte以上設定した場合、AioSetAiTransferData、AioSetAiMemorySize関数でエラーコード21985が
    返るように修正。
    上記PCの条件において、C-LOGGER Ver1.27を使用する場合、本バージョンのドライバを使用する必要があります。

  Ver4.11->Ver4.20
  --------------------------------
  ・WOW64対応(Windows 7 以降)
  ・AI-1204Z-PCI で、AioMultiAi→AioStartAiの順で実行するとAioStartAiが完了しない不具合を修正。
  ・AioGetAiSamplingData関数にてAioSetAiStopTimes関数で設定したデータ数分
    取得できない場合があるのを修正。
  ・64bitOSにおいてユーザバッファモード(バスマスタ)によるサンプリングデータが
    正常に取得できない場合があるのを修正。
  ・サンプリング中に終了処理をせずにアプリケーションを終了させた場合の不具合を修正。
  ・USBデバイスにおいて外部クロックを使用した場合に、
    サンプリングクロックエラーがバッファオーバーフローと返る不具合を修正。
  ・USBデバイス使用時、AioStartAiを連続実行するとメモリーリークが発生していたのを修正。
  ・Lシリーズにおいて、カウント一致イベント発生時、イベントルーチンに渡る引数(lParam)に
    現在のカウント値が格納されるのを、イベント発生時のカウント値(比較値)が渡るように変更。
  ・AioSetCntPresetReg関数の引数PresetNumberを変更し、AioStartCnt関数実行すると、
    カウント一致イベントが発生していないのに、カウント値が引数PresetNumber設定値になるのを修正。
  ・AI-1604CI2-PCI（ADI16-4C(PCI)）使用時、AioGetAiSamplingData等での取得テータが
    ch間でデータが入れ替わる場合がある不具合を修正。
  ・AIO-163202FX-USBで、内部クロックが外部出力できない不具合を修正。
  ・AIO-163202FX-USBで、AioGetCntMaxChannelsが使用できない不具合を修正。
  ・Eシリーズにおいて、AioSetAiScanClock関数の引数AiScanClockを小数点にすると、
    スキャンクロックが正常に設定できず、サンプリングが異常に早くなるのを修正。

  Ver4.10->Ver4.11 (Web Release)
  --------------------------------
  ・同一プロセス内において、他カテゴリを含む複数種のUSBデバイスを制御すると
    正常に動作しなくなる場合がある不具合を修正。
  ・AioSetAiMemorySize/AioGetAiMemorySize関数を使用できるデバイスにおいて、
    本関数実行すると、戻り値に20001が返ってくるデバイスが存在する不具合を修正。
  ・AIO-163202FX-USBでの簡易関数及び、サンプリング関数の混合使用における動作不具合を修正

  Ver4.01->Ver4.10 (API-USBP(WDM) Ver4.60)
  --------------------------------
  ・新規デバイスサポート
    AIO-121602LN-USB、AIO-120802LN-USB
  ・Visual Studio 2010に対応
 
  Ver4.00->Ver4.01
  --------------------------------
  ・AioExit関数がマルチプロセス時に20003エラーを返すのを修正。
  ・特定条件でアナログ出力測定(AoSpec.exe)を使用すると、ハングアップする不具合を修正(L,Mシリーズ) 
 
  Ver3.90->Ver4.00 (API-USBP(WDM) Ver4.40)
  --------------------------------
  ・新規デバイスサポート
    AI-1664LAX-USB
  ・64ビット版Windowsに対応(USBデバイス)
  ・Visual Basic.NET用関数宣言ファイルを修正
  ・AioSetAiMemorySize/AioGetAiMemorySize関数を使用できないデバイスにおいて、
    本関数実行すると、戻り値に0(正常終了)が返ってくるデバイスが存在するのを修正。
  ・DEMO デバイスにてAioGetAiStopTriggerCount関数を実行すると、
    取得値が常にゼロとなるのを修正。
  ・AioSetAiSamplingClock関数にて、クロックを1.4usec、1.3usec、0.9usec、0.7usecに設定した場合、
    指定クロックより若干短いクロック設定がなされるのを修正。

  Ver3.80->Ver3.90 (API-USBP(WDM) Ver4.20)
  --------------------------------
  ・新規デバイスサポート
    AO-1604LX-USB
  ・AioSetControlFilter関数が機能しない不具合を修正(AIO-163202FX-USB)
  ・AD変換を繰り返し行うと、最後のデータが異常値になることがある不具合を修正(AIO-163202FX-USB)
  ・AD変換中にAioStopAiで動作停止した後、AioGetAiStopTriggerCount関数を実行すると
    値が0となる不具合を修正(Lシリーズ)
  ・AioSetAoStopTriggerの引数に2を設定すると23260エラーが返る不具合を修正(Lシリーズ)

  Ver3.70->Ver3.80 (Web提供 2010.04.09)
  --------------------------------
　・AioStartAiとAioStopAi関数を繰り返し実行すると、
　　アプリケーションがロックする不具合を修正(AI-1204Z-PCI)
　・AioSetAoStartTrigger関数を実行すると23241エラーが発生する不具合を修正

  Ver3.62->Ver3.70 (API-USBP(WDM) Ver4.10, Web提供 2009.11.27)
  --------------------------------
  ・Windows 7に対応
  ・初期化処理→動作開始→終了処理のシーケンスを2回繰り返すと、
  　アプリケーションがロックする不具合を修正(AI-1204Z-PCI)
　・アプリケーションの強制終了後にAioInitを実行すると、
　　20003エラーが発生する不具合を修正(AI-1204Z-PCI)
　・オーバーフローイベントが発生しない不具合を修正(AI-1204Z-PCI)
　・転送処理が間に合わない場合に、サンプリングクロックエラーステータスを
　　返していなかった不具合を修正(AI-1204Z-PCI)
　・1CHのみ使用時でサンプリングが奇数回行われた場合、
	データを取得すると最後のデータがバイナリ値で0となる不具合を修正(AI-1204Z-PCI)
　・インターバルタイマやストップウォッチの
　　時間間隔が正しくない不具合を修正(AI-1204Z-PCI)
　・RINGメモリ使用時のいくつかの不具合を修正(AI-1204Z-PCI)

  Ver3.61->Ver3.62 (API-USBP(WDM) Ver4.00)
  --------------------------------
  ・RINGメモリ設定でAioGetAiSamplingData関数を実行した場合、
    ハングアップする事がある不具合を修正(Eシリーズ)
  ・AioInit、AioStartAo、AioExit関数を繰り返し実行すると、
    ハングアップする事がある不具合を修正(AO機能を持つデバイス)
  ・AioSetAiTransferMode関数でデバイスバッファモードを設定すると
  　21960エラーが発生する不具合を修正(Zシリーズ)
  ・Winndows 2000でのインストール時にエラーが発生する問題を修正

  Ver3.52->Ver3.61 (Web提供 2009.05.19)
  --------------------------------
  ・AioSetAiTransferMode,AioSetAoTransferMode関数を使用すると、
   「エラーコード 20001:使用しているデバイスではこの関数を使用することができません」
    が発生する不具合を修正
  ・アナログ入力の開始トリガ待ち状態でAioExitを実行した場合、
    ハングアップする不具合を修正(Eシリーズ)
  ・バッファオーバーフローが発生するする不具合を修正(AI-1204Z-PCI)
  ・ソフトウェアスタート～設定回数変換終了でサンプリングを繰り返すと
    ロックが発生する不具合を修正(Eシリーズ)
  ・AioStartAi～AioStopAi、もしくはAioStartAi～AioResetDeviceを繰り返すと
    ロックが発生する不具合を修正(AI-1204Z-PCI)

  Ver3.52->Ver3.60 (API-USBP(WDM) Ver3.90)
  --------------------------------
  ・新規デバイスサポート
    AIO-163202FX-USB

  Ver3.51->Ver3.52 2009.03.04 (Ver.Mar.2009)
  --------------------------------
  ・AIO-121601M-PCIのカウンタ機能の不具合を修正

  Ver3.50->Ver3.51 (Web提供 2009.02.16)
  --------------------------------
  ・Windows Server 2008に対応
  ・Windows Server 2008 64bit editionに対応(USBデバイス以外)

  Ver3.47->Ver3.50 2009.01.16 (Ver.Jan.2009)
  --------------------------------
  ・新規デバイスサポート
    AIO-121601M-PCI,
  ・新規関数サポート
    AioGetCntmMaxChannels
    AioSetCntmZMode, AioSetCntmZLogic 
    AioSelectCntmChannelSignal, AioSetCntmCountDirection
    AioSetCntmOperationMode, AioSetCntmDigitalFilter
    AioSetCntmOutputHardwareEvent, AioSetCntmInputHardwareEvent 
    AioSetCntmCountMatchHardwareEvent, AioSetCntmPresetRegister
    AioGetCntmZMode, AioGetCntmZLogic
    AioGetCntmChannelSignal, AioGetCntmCountDirection
    AioGetCntmOperationMode, AioGetCntmDigitalFilter
    AioCntmStartCount, AioCntmStopCount
    AioCntmPreset, AioCntmZeroClearCount
    AioCntmReadCount
    AioCntmNotifyCountUp, AioCntmStopNotifyCountUp
    AioCntmCountUpCallbackProc, AioCntmNotifyCounterError
    AioCntmStopNotifyCounterError, AioCntmCounterErrorCallbackProc
    AioCntmNotifyCarryBorrow, AioCntmStopNotifyCarryBorrow
    AioCntmCarryBorrowCallbackProc, AioCntmNotifyTimer
    AioCntmStopNotifyTimer, AioCntmTimerCallbackProc
    AioSetCntmTestPulse, AioCntmReadStatusEx
    AioCntmInputDIByte, AioCntmOutputDOBit
  ・Visual C++.NET C++/CLI に対応。

  Ver3.46->Ver3.47 2008.10.10 (Web提供 2008.10.10)
  --------------------------------
  ・外部クロック設定時に内部クロックを設定する。
    サンプリングを開始し、サンプリング動作可能な外部クロックを入力すると
    サンプリングクロックエラーでデバイスが停止する不具合を修正(AI-1204Z-PCI)。

  Ver3.45->Ver3.46 2008.10.01 (Ver.Oct.2008)
  --------------------------------
  ・サンプルAiLongなどを使った連続サンプリングが機能しない不具合を修正
    (DEMOデバイスを含むF,L,Eシリーズ以外のデバイス)
  ・複数チャネル、RINGメモリで動作中、データ取得を行うことができる機能を追加
    (Eシリーズ。ただし使用チャネルが偶数時のみ)
  ・AioStartAi～AioStopAi、もしくはAioStartAi～AioResetDeviceを繰り返すと
    ロックが発生する不具合を修正(AI-1204Z-PCI)
  ・バスマスタの入力データが化ける不具合を修正(バスマスタ搭載ボード全て)
  ・条件により、イベントが発生しない不具合を修正(F,L,Eシリーズ以外のデバイス)
  ・API-TIMER(WDM)に対応。

  Ver3.44->Ver3.45 (Web提供 2008.07.11)
  --------------------------------
  ・複数回のリピート、外部トリガスタートの条件を設定すると
    次回リピート動作時にトリガ待ちの状態にならず、
    出力が進行してしまう不具合を修正(F, L, Eシリーズ以外のデバイス)。
  ・Visual Studio 2008に対応(VB, C#のみExpressEditionにも対応)

  Ver3.43->Ver3.44 (Web提供 2008.05.30)
  --------------------------------
  ・関数AioSetAiRangeAll, AioSetAiRangeを実行すると、
    サンプリングしたデータが正常に取得できない不具合を修正(F,Lシリーズ)

  Ver3.42->Ver3.43 (Web提供 2008.05.09)
  --------------------------------
  ・CPU-CA10+FITデバイスとAI-1608AY-USBかAIO-160802AY-USBを同時に使用すると
    AI-1608AY-USBかAIO-160802AY-USBの診断プログラムが起動しない不具合を修正
  ・CPU-CA10+FITデバイスとAI-1608AY-USBかAIO-160802AY-USBを同時に使用すると
    AI-1608AY-USBかAIO-160802AY-USBの関数が実行できない不具合を修正

  Ver3.41->Ver3.42 (Web提供 2008.04.30)
  --------------------------------
  ・校正プログラムを実行すると「22204：ドライバ内部エラー」が発生する不具合を修正
    (ADA16-32/2(CB)F)
  ・リピート無限、リピート終了コールバックで動作中にAioStopAi関数を実行すると、
    不定期的にアプリケーションがロックする不具合を修正
  ・メモリ容量一杯までサンプリングするとデータが取得できなくなる不具合を修正
    AioGetSamplingDataEx関数の「エラーコード 21885FIFOが空です」を削除
    (Fシリーズ)

  Ver3.40->Ver3.41 2008.03.31 (Ver.Apr.2008)
  --------------------------------
  ・USBデバイス使用時、レベルトリガ設定が反映されない不具合を修正
  ・リピートを用いて連続サンプリング入力を行うと、
    一定回数以降イベントが上がらなくなり、
    オーバーフローで動作が停止する不具合を修正
    (DEMOデバイスを含むF,L,Eシリーズ以外のデバイス)
  ・リピート設定した場合、正常に機能しない不具合を修正(Lシリーズ)
  ・デバイス名の間違いを修正(AI-1664LA-LPE, AO-1608L-LPE, AO-1616L-LPE)
  ・AI-1204Z-PCIで、以下の関数に対応
    AioSetAiStartInRangeEx, AioGetAiStartInRangeEx
    AioSetAiStartOutRangeEx, AioGetAiStartOutRangeEx
    AioSetAiStopInRangeEx, AioGetAiStopInRangeEx
    AioSetAiStopOutRangeEx, AioGetAiStopOutRangeEx
  ・関数AiSamplingClockを実行する際、
    1chあたりの最速サンプリングクロック10usecの設定ができず、
   「エラーコード 21140:AiSamplingClockの値が使用しているデバイスの指定範囲外です」
    が発生する不具合を修正(ADA16-8/2(CP)L, AD16-64(LPCI)LA, AI-1664LA-LPE)

  Ver3.31->Ver3.40 2008.02.04 (Ver.Jan.2008 for AIO)
  --------------------------------
  ・新規デバイスサポート
    AI-1204Z-PCI,
    AIO-160802LI-PE, AI-1616LI-PE
    AO-1604LI-PE, AI-1664LA-LPE
    AO-1608L-LPE, AO-1616L-LPE

  Ver3.30->Ver3.31 (Web提供 2008.01.25)
  --------------------------------
  ・AD12-8(PM)を使用し、デバイスマネージャ上のプロパティページにて
    共通設定タグを選択すると"DeviceType Unknown Error"のダイアログが
    表示される不具合を修正
  ・DEMO Device使用時にハングアップしていた不具合を修正

  Ver3.21->Ver3.30 2007.12.21 (Ver.Jan.2008)
  --------------------------------
  ・アプリケーションを動作させる度にタスクマネージャ上の
    ハンドル数が多くなっていく不具合を修正。
  ・校正プログラムを実行すると「エラーコード 22204：ドライバ内部エラー」
    が発生する不具合を修正。
  ・関数AioSetDiFilter、AioGetDiFilterを実行すると
   「20001:使用しているデバイスではこの関数を使用することができません」
    が発生する不具合を修正。
  ・関数AioSetAiRangeAll, AioSetAiRangeが正常に動作しない不具合を修正。

  Ver3.20->Ver3.21 2007.10.12 (Web提供 2007.10.22)
  --------------------------------
  ・ACX-PAC(W32)上で発生する不具合を修正

  Ver3.10->Ver3.20 2007.09.30 (Ver.Oct.2007)
  --------------------------------
  ・新規デバイスサポート
    AIO-121601E3-PE, AIO-121601UE3-PE
    AIO-161601E3-PE, AIO-161601UE3-PE
  ・Visual C# 2005 Express Edition, Visual Basic 2005 Express Editionに対応
  ・AioSetAiRangeAll関数を繰り返し実行すると21061エラーが
    発生する不具合を修正(Eシリーズ)
  ・DemoDeviceを使用してデバイスマネージャ上のプロパティページにて
    共通設定タグを選択すると"DeviceType Unknown Error"のダイアログが
    表示される不具合を修正
  ・USBデバイス使用時、Ringメモリ形式、有限サンプリング、
    コールバックルーチン設定にして、AiStartを繰り返すと
    サンプリング動作が途中で停止する不具合を修正

  Ver3.00->Ver3.10 2007.06.11 (Ver.Jun.2007)
  --------------------------------
  ・64ビット版Windowsに対応(USBデバイス以外)
  ・新規デバイスサポート
    AI-1216B-RB1-PCI, AI-1216B-RU1-PCI

  Ver2.30->Ver3.00 2007.02.28 (Ver.Feb.2007)
  --------------------------------
  ・Windows Vistaに対応
  ・新規デバイスサポート
    AIO-121602AH-PCI, AIO-121602AL-PCI, AI-1216AH-PCI, AI-1216AL-PCI
  ・ドライバにデジタル著名を追加
  ・ドライバの自動インストール機能追加(W2000系OSのみ)
  ・DLLとSYSファイルのバージョンチェック機能を追加
  ・スタンバイモードに対応
  ・新規関数サポート
    AioResetProcess, AioStartAiSync
    AioSetAiStartInRangeEx, AioGetAiStartInRangeEx
    AioSetAiStartOutRangeEx, AioGetAiStartOutRangeEx
    AioSetAiStopInRangeEx, AioGetAiStopInRangeEx
    AioSetAiStopOutRangeEx, AioGetAiStopOutRangeEx
  ・Visual Studio.NET用ユーティリティを追加
  ・DEMO Device使用時にハングアップしていた不具合を修正
  ・簡易関数使用時、AD変換エラーまたはDA変換エラーが発生する事がある不具合を修正
    (Fシリーズ、Lシリーズ以外のデバイス)
  ・関数実行速度測定プログラムで、AioGetAiSamplingDataをクリックすると
    ハングアップする不具合を修正(Eシリーズ)
  ・指定したサンプリング回数+1回のクロックが入力されないと
    動作終了しない不具合を修正(E, F, Lシリーズ以外のデバイス)
  ・複数チャネルを使用、外部トリガ開始、変換回数停止、リピート回数複数回設定の条件で
    収集を行うと、チャネル間のデータずれが発生する不具合を修正(Lシリーズ)

  Ver2.20->Ver2.30 2006.12.04 (Web提供 2006.12.15)
  --------------------------------
  ・マルチコアCPUで使用時に、AioGetAiSamplingCount関数が
    異常な値を返す事がある不具合を修正(Eシリーズ)
  ・AioStartAi, AioStartAo, AioStartTmTimer, AioStartCnt関数の
    実行時間を短縮、ばらつきを軽減
  ・条件により、指定サンプリング回数格納イベントが
    発生しない事がある不具合を修正

  Ver2.10->Ver2.20 2006.09.01 (Web提供 2006.09.01)
  --------------------------------
  ・ML-DAQ使用時に起こる不具合を修正

  Ver1.90->Ver2.10 2006.07.14 (Ver.Aug.2006)
  --------------------------------
  ・新規デバイスサポート
    AIO-160802L-LPE, AI-1616L-LPE, AO-1604L-LPE

  Ver1.80->Ver1.90 2006.03.24 (Ver.Apr.2006)
  --------------------------------
  ・新規デバイスサポート
    AIO-163202F-PE, DA16-8(LPCI)L, DA16-4(LPCI)L
  ・Visual Studio 2005に対応

  Ver1.70->Ver1.80 2005.12.01 (Ver.Feb.2006)
  --------------------------------
  ・C-LOGGER Ver1.0に対応

  Ver1.60->Ver1.70 2005.09.29 (Ver.Nov.2005)
  --------------------------------
  ・新規デバイスサポート
    AD12-16(PCI)EV, AD12-16U(PCI)EV,
    AD16-16(PCI)EV, AD16-16U(PCI)EV,
    AD16-64(LPCI)LA

  Ver1.50->Ver1.60 2005.07.22 (Ver.Aug.2005)
  --------------------------------
  ・Windows Server 2003に対応
  ・新規デバイスサポート
    ADAI16-8/2(LPCI)L, ADI16-16(LPCI)L, DAI16-4(LPCI)L
  ・新規関数追加
    AioSetAiClockEdge, AioGetAiClockEdge
    AioSetAoClockEdge, AioGetAoClockEdge

  Ver1.42->Ver1.50 2005.03.31 (Ver.Apr.2005)
  --------------------------------
  ・MATLAB Data Acquisition Toolboxに対応

  Ver1.41->Ver1.42 2005.01.25 (Web提供 2005.01.31)
  --------------------------------
  ・ACX-AIO使用時にオートメーションエラーが発生する不具合を修正

  Ver1.40->Ver1.41 2004.11.30 (Ver.Jan.2005)
  --------------------------------
  ・ハイパースレッディングPCに対応
  ・PCIバス上でボードの診断プログラムを実行すると
    レジストリの読込みエラー(エラーコード4)が発生する
    事がある不具合を修正
  ・複数チャネルの出力を行うと、チャネル間のデータがずれる
    不具合を修正(Lシリーズ)

  Ver1.31->Ver1.40 2004.08.25 (Ver.Oct.2004)
  --------------------------------
  ・新規デバイスサポート
    ADA16-8/2(CB)L
  ・校正プログラムでAD調整時に手動でゲイン調整ができない
    不具合を修正(Fシリーズ,ADA12-8/2(LPCI),AD16-16(LPCI)L)

  Ver1.30->Ver1.31 2004.06.18 (Ver.Jun.2004)
  --------------------------------
  ・Visual C#.NET2002, 2003に対応
  ・スキャンクロックの設定に対応(Eシリーズ, Fシリーズ)
  ・基盤温度の取得に対応(ADI16-4L(PCI))
  ・AioSetEcuSignal関数でAiの停止条件を変更すると、
    Ai動作が停止しない不具合を修正(Fシリーズ)
  ・AioSetEcuSignal関数でAoの停止条件を変更すると、
    Ao動作が停止しない不具合を修正(Fシリーズ)
  ・外部トリガ開始または外部トリガ停止を使用する際に、
    立ち下りを設定できない不具合を修正(AD12-64(PCI), AD12-16(PCI))
  ・バスマスタを使用して64Mb以上の転送を行なうと、AioGetAiTransferLapで
    取得するLapの値が異常になる不具合を修正(Fシリーズ)
  ・AioMultiAi関数使用時にチャネル変換順序の設定
    (AioSetAiChannelSequence)が有効にならない不具合を修正(Eシリーズ)

  Ver1.21->Ver1.30 2003.10.31 (Ver.Nov.2003)
  --------------------------------
  ・新規デバイスサポート
    ADA16-8/2(LPCI)L, AD16-16(LPCI)L, DA16-4(LPCI)L

  Ver1.20->Ver1.21 2003.06.02 (Web提供 2003.06.11)
  --------------------------------
  ・アンインストーラに以下の機能を追加
    システムに複製されたセットアップ情報ファイルを削除
    デバイスマネージャに登録されているデバイスを削除
  ・JPでレンジをユニポーラ設定にすると、
    診断プログラムが強制終了する不具合を修正(Eシリーズ)
  ・AiSpec、AoSpecで動作中に×ボタンを押すと強制終了する不具合を修正
  ・AiSetAiSamplingClock、AiSetAoSamplingClock関数で
    正常に値が設定できないことがある不具合を修正(全デバイス)
  ・DIデータが添付されない不具合を修正(Fシリーズ)
  ・AI,AOで外部トリガを連続で入力したままAioExit関数を実行すると
    ハングアップする不具合を修正(Fシリーズ)
  ・AioSetAiRangeAll関数で±10V、0～10V、4mA～20mA以外の
    レンジが設定できない不具合を修正(ADI12-16(PCI))
  ・RINGメモリでリピート出力の際、出力データに抜けが発生する
    不具合を修正(DA12-16(PCI), DA12-8(PCI), DA12-4(PCI))
  ・AioSetAiChannelSequence、AioGetAiChannelSequenceの書式誤りを修正
    (CAIO.BAS, CAIO.VB, CAIO.PAS)

  Ver1.10->Ver1.20 2003.03.01 (Web提供 2003.03.14)
  --------------------------------
  ・英語版対応
  ・API-USBP(WDM)で使用するCAIO.DLLとの共存が可能に
  ・変換データが正常に取得できない不具合を修正(AD16-4L(PCI))
  ・サンプルAiExで、保存ファイルの変換データが文字化けする不具合を修正
  ・AioSetAiStartInRange, AioSetAiStartOutRange,
    AioSetAiStopInRange, AioSetAiStopOutRange関数でエラーが発生する不具合を修正

  Ver1.04->Ver1.10 2002.12.25 (Ver.Dec.2002)
  --------------------------------
  ・新規デバイスサポート
    ADA16-32/2(PCI)F, ADA16-32/2(CB)F
  ・新規関数追加
  ・Visual C++.NET, Visual Basic.NET対応
  ・新規サンプル追加
  ・AioInit関数に失敗した際、そのまま他の関数を使用すると
    アプリケーションがロックする不具合を修正(全デバイス)
  ・ボードのＪＰが割り込み未使用の状態でも
    AioInit関数が成功していた不具合を修正(Eシリーズ)
  ・アナログ入出力で高速動作を行うと、サンプリングクロックエラー発生時、
    まれににハングアップする不具合を修正(全デバイス)
  ・AioQueryDeviceName, AioGetDeviceType関数に
    NULLチェックとエラーコードを追加(全デバイス)
  ・AioEnableAo, AioDisableAoでチャネル0を指定すると
    エラーが発生していた不具合を修正(DAI16-4C(PCI))
  ・複数チャネルの出力が異常になる不具合を修正(DAI16-4C(PCI))
  ・10820エラーが発生しても正常終了を返していた不具合を修正(Eシリーズ)
  ・バッファオーバーフローエラーが発生した場合、
    その後メモリをリセットせずにAioStartAi関数を実行すると
    エラーを返すように修正(全デバイス)
  ・AioSingleAi関数でまれにAD変換エラーが発生する不具合を修正(AD16-16U(PCI)EH)
  ・±10V、0～10V、4mA～20mA以外のレンジが設定できない不具合を修正(ADI12-16(PCI))
  ・AioSingleAo, AioMultiAo関数でまれにD/A変換エラーが発生する不具合を修正
    (DA12-16(PCI), DA12-8(PCI), DA12-4(PCI))
  ・AioStartAi実行時に使用したハンドルが開放されない不具合を修正(Eシリーズ)
  ・ユーティリティAiSpec, AoSpecのグラフ描画部分が、
    複数チャネルに対応していなかった不具合を修正(AD12-16U(PCI)EH, AD16-16U(PCI)EH)
  ・AioSingleAi関数で過去のデータが取得される不具合を修正(ADI16-4C(PCI))
  ・AioSetAiRange関数で±2.5V設定ができない不具合を修正(AD12-16U(PCI)EH)

  Ver1.03->Ver1.04 2002.06.18 (Ver.Aug.2002)
  --------------------------------
  ・旧ASICで発生するサンプリング回数取得失敗を、
    より出にくくなるよう修正(Eシリーズ)
  ・サンプルAiLongで動作を行うと、65535回目のイベントでサンプリング
    クロックエラーが発生する不具合を修正(Eシリーズ)
  ・チャネル増設を行った際に、増設チャネルの変換データが
    正常に取得できない不具合を修正(Eシリーズ)
  ・ノートPCでカード使用時、カードを挿入したまま
    W9xが起動できない不具合を修正(AD12-8(PM))
  ・サンプリングクロックを上げるとメモリ違反を起こす不具合を修正(AD12-8(PM))
  ・サンプリングクロックを10usec近くまで早めると、
    異常な変換データが取得される不具合を修正(AD12-8(PM))
  ・外部開始トリガを使用したときに、サンプリングクロックを変更できない
    不具合を修正(DA12-16(PCI), DA12-8(PCI), DA12-4(PCI))

  Ver1.02->Ver1.03 2002.02.01 (Web提供 2002.02.15)
  --------------------------------
  ・ヘルプにドライバのアップデート方法を追加
  ・ヘルプに簡易デジタル入出力チュートリアルを追加
  ・ヘルプのドライバ仕様－デバイス別仕様に、
    JP設定やピンアサインを図入りで記述
  ・W9xでサンプルAiLong使用時、指定サンプリング数格納イベント発生時に
    ウィンドウを移動させるとその後のイベントが発生しなくなる不具合を修正
  ・サンプルMultiAoでハングする不具合を修正(AD12-8(PM))
  ・サンプルMultiAiでデータがずれる不具合を修正(AD12-8(PM))
  ・サンプルAiExで実際の変換速度が異常になり、データがずれる不具合を修正
    （AD12-8(PM)）
  ・サンプリングを１回に設定すると動作中ステータスがOFFにならない不具合を修正
  ・サンプルプログラムの不具合を修正
  ・ヘルプの記述ミスを修正

  Ver1.01->Ver1.02 2002.01.15
  --------------------------------
  ・W2000系のUSERモードログインでドライバが使用できなかった不具合を修正
  ・AioMultiAiで21441エラーを0として返していた不具合を修正
  ・指定サンプリング数格納ステータスがデータ取得を行ってもOFFにならない
    不具合を修正(Eシリーズ)
  ・レベルトリガ開始待ちの状態でAioStopAiを実行したときに
    21480エラーが発生していた不具合を修正(Eシリーズ)
  ・サンプルプログラムの不具合を修正
  ・ヘルプの記述ミスを修正

  Ver1.00->Ver1.01 2001.12.16
  --------------------------------
  ・リピート動作が正常に行かえなかった不具合を修正(Eシリーズ)
  ・リピート動作の全終了時にはリピート終了イベントを発生させないよう
    変更(Eシリーズ)
  ・ドライバがセットしたクロックエラーはAioResetAiStatusまたは
    AioStartAiでリセットするよう変更(Eシリーズ)
  ・変換速度が速すぎてドライバの処理が間に合わない際にクロックエラー
    だけでなく変換終了イベントが発生していた不具合を修正(Eシリーズ)

  Ver1.00 2001.12.01 (Ver.Jan.2002)
  --------------------------------
  ・ファーストリリース

