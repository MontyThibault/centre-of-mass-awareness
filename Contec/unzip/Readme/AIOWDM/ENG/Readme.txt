=====================================================================
=            Windows Driver for Analog I/O Driver                   =
=                                             API-AIO(WDM) Ver4.72  =
=                                                  CONTEC Co.,Ltd.  =
=====================================================================

- Contents
==========
  Introduction
  Notes
  Installation
  The files installed
  Sample programs
  The history of version-up


- Introduction
==============
  Thank you for purchasing this product.

  The following description is a supplementary explanation for API-AIO(WDM).
  Please refer to Online Help(APITOOL.CHM) for how to use API-AIO(WDM).


- Notes
=======
  API-AIO(WDM) is different from the earlier editions of analog I/O driver.
  Please refer to Online Help(API-AIO(WDM).CHM) for the difference.

  About compiling the C++ Builder samples
  If the path contaiins "-"(hyphen), the C++ Builder will fail in the building.
  If API-AIO(WDM) has been installed by default,
  it can not be used "as is" because "API-PAC(W32)" is included
  in the path.
  You should first copy the folder that include the sample project to a path
  not containing the hyphen and then build it.

  In the following case, the buffer for bus master is limited to maximum 1M Byte.

  <a PC has the memory more than 4G Byte>
  In Windows 64 bit OS and Windows 32 bit OS, PAE (Physical Address Extension) is enabled.

  <a PC has the memory less than 4G Byte>
  In Windows 64 bit OS or Windows 32 bit OS, PAE (Physical Address Extension) is enabled, 
  and [Memory Reclaiming] functionality is enabled by BIOS setting of the PC (matherboard) 
  in which a board is plugged.

  * According to PC (motherboard), there is the case that [Memory Reclaiming] functionality 
  cannot be changed to Enabled/Disabled by BIOS setting, therefore, please confirm in advance.

  The target device
  AIO-163202F-PE, ADA16-32/2(PCI)F, AI-1204Z-PCI, ADA16-32/2(CB)F


- Installation
==============
  - Installation of development environment(help, sample, tool, etc)

    You must uninstall older version of development environment from
    [control panel] before installing newer version.

    <Install from WEB downloaded file>
      Unzip downloaded file and execute following setup file.
      Apipac\AioWdm\Disk1\Setup.exe

    <Install from API-PAC(W32) CD-ROM>
      Install from Autorun.exe.

  - Installation of device driver

    You must uninstall older version of device driver 
    before installing newer driver.

    <Install from API-PAC(W32) CD-ROM>
      For uninstallation or installation procedure, 
      refer to following help file in API-PAC(W32) CD-ROM.
      <CD-ROM>\Apipac\Help\Hwinst\Eng\Apitool.chm

    <Install from WEB downloaded file>
      For uninstallation or installation procedure, 
      refer to following help file which is created after 
      unzipping the downloaded file.
      Help\AIOWDM\ENG\Apitool.chm


- The files installed
=====================
  - This product uses a setup program to install files in the System 
    directory or other directory designated by the user in the 
    following configuration. 
  - If other API-TOOL drivers have already been installed, the 
    files will be installed in that directory.

  \<User Directory>
    CONTEC.ICO                    Icon file
    CONTEC_APIPACW32_HOMEPAGE.URL Shortcut of API-PAC(W32)HP
    AIOWDM\API-AIO(WDM).CHM       Help file
    AIOWDM\README.TXT             This file
    AIOWDM\SAMPLES\               Sample programs
    AIOWDM\SAMPLES\EXE            Executive files of sample programs
    AIOWDM\UTILITY                Utility programs


- Sample programs
=================
  The sample programs consist of the following directories for every
  language.

  - API-AIO(WDM) 32 bit Edition
    \<User Directory>
    |
    +--\AIOWDM
       |
       +--\SAMPLES
          |
          +--\INC       Include file for every language
          |
          +--\LIB_I386  Library file for 32 bit application
          |
          +--\MODULE    Subroutine file for every language
          |
          +--\VB6       Sample program for Visual Basic 6.0
          |
          +--\VBNET     Sample program for Visual Basic .Net
          |
          +--\VC6       Sample program for Visual C++ 6.0
          |
          +--\VCNET     Sample program for Visual C++ .Net
          |
          +--\VCNET2005 Sample program for Visual C++ .Net
          |
          +--\VCNET2013 Sample program for Visual C++ .Net
          |
          +--\VCNETCLI  Sample program for Visual C++ .Net (C++/CLI)
          |
          +--\VCS       Sample program for Visual C# .Net
          |
          +--\BUILDER5  Sample program for C++ Builder 5
          |
          +--\DELPHI6   Sample program for Delphi 6
          |
          +--\CONSOLE   Sample Console program for Visual C++ 6.0

  - API-AIO(WDM) 64 bit Edition
    \<User Directory>
    |
    +--\AIOWDM
       |
       +--\SAMPLES
          |
          +--\INC       Include file for every language
          |
          +--\LIB_I386  Library file for 32 bit application
          |
          +--\LIB_amd64 Library file for 64 bit application
          |
          +--\MODULE    Subroutine file for every language
          |
          +--\VBNET     Sample program for Visual Basic .Net
          |
          +--\VCNET2005 Sample program for Visual C++ .Net
          |
          +--\VCNET2013 Sample program for Visual C++ .Net
          |
          +--\VCNETCLI  Sample program for Visual C++ .Net (C++/CLI)
          |
          +--\VCS       Sample program for Visual C# .Net


- The history of version-up
===========================

  * F-Series : ADA16-32/2(PCI)F, ADA16-32/2(CB)F, AIO-163202F-PE
    L-Series : ADA16-8/2(LPCI)L, ADA16-8/2(CB)L,
               AD16-64(LPCI)LA, AD16-16(LPCI)L,
               DA16-16(LPCI)L, DA16-8(LPCI)L, DA16-4(LPCI)L
               ADAI16-8/2(LPCI)L, ADI16-16(LPCI)L, DAI16-4(LPCI)L
               AIO-160802L-LPE, AI-1616L-LPE, AO-1604L-LPE
               AIO-121602AH-PCI, AIO-121602AL-PCI
               AI-1216AH-PCI, AI-1216AL-PCI
               AIO-160802LI-PE, AI-1616LI-PE
               AO-1604LI-PE, AI-1664LA-LPE
               AO-1608L-LPE, AO-1616L-LPE
    E-Series : AD12-16(PCI)E, AD12-16U(PCI)E, AD12-16U(PCI)EH
               AD16-16(PCI)E, AD16-16U(PCI)EH, ADI12-16(PCI)
               AD12-16(PCI)EV, AD12-16U(PCI)EV,
               AD16-16(PCI)EV, AD16-16U(PCI)EV
               AIO-121601E3-PE, AIO-121601UE3-PE
               AIO-161601E3-PE, AIO-161601UE3-PE
    B-Series : AI-1216B-RB1-PCI, AI-1216B-RU1-PCI
    Z-series : AI-1204Z-PCI
    M-series : AIO-121601M-PCI

  Ver4.71->Ver4.72 (Web Release)
  --------------------------------
  - Fixed a bug where the sampling clock error will not occur in a particular sampling clock in USB device.
  - Fixed a bug where AioResetAoMemory can perform during the execution of the analog output in USBdevice.
  - Update the version of the calibration program(caiocal.exe).

  Ver4.70->Ver4.71 (Web Release)
  --------------------------------
  - Fixed a bug that can not be set the external clock to the rising in the AO-1604LX-USB.
  - Fixed a bug the error code 10003 occurs in AioInit function when you run a 32bit application in WOW64 to use the USB device.

  Ver4.603->Ver4.70 (Web Release)
  --------------------------------
  - Add support OS
    Support OS:                   Microsoft Windows 10
                                  Microsoft Windows 10 x64 Edition
  - For F series and L series, fault correction that count match pulse isn't output.
  - For AIO-121601M-PCI, fault correction that the general-purpose input status cannot be retrieved by 
    function AioCntmReadStatusEx, and the general-purpose input data can not be read by function AioCntmInputDIByte.
  - For L series and M series, fault correction that the edge setting isn't reflected by AioSetAoClockEdge.
  - For AIO-121602LN-USB, AIO-120802LN-USB, AIO-163202FX-USB, AI-1664LAX-USB, AO-1604LX-USB, 
    fault correction that operation becomes unstable when using comparison count match function.
  - For AY series and AIO-160802GY-USB, fault correction that the edge setting isn't reflected 
    if you run functions in the order of AioSetAiClockType->AioSetAiClockEdge.

  Ver4.60->Ver4.603 (API-USBP(WDM) Ver4.70)
  --------------------------------
  - Supports new devices
    AIO-160802GY-USB
  - The defect which can't normally acquire a sampling count is corrected in the AioGetAiStopTriggerCount function 
    in AIO-163202FX-USB.

  Ver4.53->Ver4.60 (Ver.Dec.2014)
  --------------------------------
  - Add support OS
    Support OS:                   Microsoft Windows 8.1
                                  Microsoft Windows 8.1 x64 Edition
  - Add support development language
    Support development language: Microsoft Visual Basic 2013
                                  Microsoft Visual C# 2013
                                  Microsoft Visual C++ 2013
  - If not in Japanese language environment, the fault which the defined error string of error code 28000 - 28032 
    cannot be retrieved by funtion AioGetErrorString is corrected. 
  - For AIO-163202FX-USB, fault correction that processing is not completed by performing AioStopAo function 
    when AO device buffer is RING mode. 
  - For USB device, fault correction that event of AO device operation end is notified for two times 
    when conditions are satisfied. 
    (Except DAI12-4(USB)GY, DAI16-4(USB))

  Ver4.50->Ver4.53 (Web Release 2014/04)
  --------------------------------
  - In F series, if it samples to the maximum of a buffer at the time of FIFO mode use, 
    the fault where the number of times of a sampling is set to 0 and which cannot do data acquisition will be corrected. 
  - In L series and AIO-121601M-PCI, when not setting up the end event of device operation by the sampling of AD,
    the fault which processing does not complete by the 2nd AioStartAi function execution is corrected. 
  - The problem which a proofreading program freezes is corrected in L series and AIO-121601M-PCI. 

  Ver4.45->Ver4.50 (Web Release 2014/02)
  --------------------------------
  - Add support OS
    Support OS:                   Microsoft Windows 8
                                  Microsoft Windows 8 x64 Edition
  - Add support development language
    Support development language: Microsoft Visual Basic 2012
                                  Microsoft Visual C# 2012
                                  Microsoft Visual C++ 2012
  - For AI-1204Z-PCI, fault correction that [AioStartAi: A user buffer isn't set up] error occurs 
    by measuring the executive time of function AioGetAiSamplingData, when the program for 
    measuring the executive speed of function is running in an OS which recognizes memory more than 4G Byte.
  - For F series and AIO-121601M-PCI, if the conversion start condition is specified 
    to [Event controller output], [Wait the start trigger] status will not be notified.
  - Fault correction that the sampling operation can't be started normally.
  - Fault correction that error 20002 occurs by function AioSetTmEvent and AioStartTmCount.
  - For L series and AIO-121601M-PCI, fault correction that AI repeat function doesn't work normally.
  - For AI-1204Z-PCI, fault correction that exception error occurs by performing function AioExit.
  - For L series and AIO-121601M-PCI, fault correction that data doesn't output normally 
    by function AioMultiAo and AioMultiAoEx, after calling AO continuous functions.
  - The fault is corrected, which an error indicating that [Contec USB Service] has failed to start is recorded 
    in the event log, if a USB device was removed without uninstalling the driver.

  Ver4.36->Ver4.45 (Web Release 2013/11)
  --------------------------------
  - For USB device with counter function, fault correction that it can't count, 
    if count start and count stop are performed repeatedly.
  - For AIO-163202FX-USB, fault correction that sampling clock error (20000H) occurs, 
    if AO repeat is terminated by the conversion stop conditions other than times stop.
  - For F series and L series, fault correction that the repeat count doesn't increase, 
    if AO repeat and software start are set.
  - For AIO-163202FX-USB, fault correction that repeat runs over the specified times, 
    when using AO repeat function.
  - Mistake correction of the strings can be retrieved by function AioGetErrorString 
    corresponding to the return values 12381 and 12382.
  - For AI-1204Z-PCI, fault correction that [Event that the specified number of data are stored] 
    occurs after [Event that device operation end].
  - For AY series, fault correction that it can't output to DO03.
  - Fault correction that blue screen occurs, when simple I/O functions are performed.(Except USB device)

  Ver4.30->Ver4.35 (Ver.July.2013)
  --------------------------------
  - In F series and L series, AO repeat function corrects the fault which does not operate normally.
  - In L series, if 2 is set to the argument of AioSetAoStopTrigger, 
    the fault to which 23260 errors return will be corrected. 
  - The fault which cannot perform the sampling start by a level trigger normally 
    by "AI-1664 LAX-USB" is corrected. 
  - If AioStartAo, AioGetAoStatus, and AioStopAo are repeated in order 
    in DA12-16(PCI), DA12-8(PCI), DA12-4(PCI), and DAI16-4C(PCI), 
    it will correct that a sampling clock error may occur. 

  Ver4.27->Ver4.30
  --------------------------------
  - It will correct that BSoD may occur, if AioSetAiStopTimes or AioSetAiRangeAll is performed in DEMO DEVICE. 
  - If AioGetCntMaxChannels is performed by the USB device which does not have a counter function, 
    although a counter function does not exist, the fault to which CntMaxChannels=1 returns will be corrected. 
  - If AioResetProcess is performed in the USB device which has a counter function, 
    the unfixed value which is not defined will correct the fault which returns as an error. 
  - In L series with the function of AI and AO both, if a sampling is started in order of AI and AO, 
    the fault stopped in the middle of the sampling of AI while status has been busy will be corrected. 
  - In AI-1204Z-PCI, if samples, such as SingleAi, are performed by a debug mode, 
    and a debugger is forced to terminate after performing AioInit, it will correct that BSoD may occur.

  Ver4.25->Ver4.27
  --------------------------------
  - In PC which recognizes the memory of 4 GByte or more, execution of AioResetDevice will correct that 
    an error code 21985 may occur. 
  - It corrects that a pulse-like waveform may be outputted to instruction execution time 
   in AioInit or AioResetDevice by "AIO-163202 FX-USB." 

  Ver4.22-> Ver4.25
  --------------------------------
  - Fault correction that 11460 error code is generated, at the start of the second sampling in Windows98.
  - Fault correction that FIFO is empty (data retrieved 0) does not return an error code 21584, 
    even at run-time state of AioGetAiSamplingData.

  Ver4.21-> Ver4.22 (Web Release)
  --------------------------------
  - Fault correction that there is a possibility that BSoD occurs, 
    when execute a function after execution AioResetProcess, in multiple processes.

  Ver4.20-> Ver4.21 (Web Release)
  --------------------------------
  - Z-series and F series, on Windows 64bit OS, and has the memory more than 4G Byte,
    If you set more than 1MByte the buffer, so that the error returned by 21985 Fix 
    and AioSetAiMemorySize AioSetAiTransferData.
    PC in this condition, if you want to use the C-LOGGER Ver1.27, you must use this version of the driver.

  Ver4.11-> Ver4.20
  --------------------------------
  - Support WOW64 (Since Windows 7)
  - Fault correction that AioStartAi does not complete, 
    when it is executed in the order of AioMultiAi->AioStartAi with AI-1204Z-PCI.
  - Fault correction that function AioGetAiSamplingData can not acquire the data, 
    which's number is set by function AioSetAiStopTimes.
  - Fault correction that the sampling data can not be acquired successfully 
    by User buffer mode (bus master) in 64bit OS.
  - Fault correction that the application is exited without performed AioExit when sampling.
  - Fault correction that the sampling clock error is returned as a buffer overflow error,
    when a USB device is used with external clock.
  - Fault correction that memory leak occurs when AioStartAi is performed continuously 
    with a USB device.
  - When a count match event occurs with L series, the value passed to the parameter (lParam) of the event routine 
    is modified from current count value to the count value (comparison value) when event has occurred. 
  - Fault correction when the parameter PresetNumber of function AioSetCntPresetReg is changed and 
    funtion AioStartCnt is executed, even if a count match event doesn't occur, the count value is 
    changed to be the value set by parameter PresetNumber.
  - Fault correction that the data is interchanged between channels which is acquired by AioGetAiSamplingData etc., 
    when using AI-1604CI2-PCI (ADI16-4C(PCI)).
  - Fault correction that the internel clock of AIO-163202FX-USB can not be output to external.
  - Fault correction that AioGetCntMaxChannels can not be used with AIO-163202FX-USB.
  - Fault correction that the scan clock can not be set successfully and the sampling is to be unusually fast, 
    if the parameter AiScanClock of function AioSetAiScanClock is set a decimal point when using E-Series board.

  Ver4.10->Ver4.11 (Web Release)
  --------------------------------
  - Fault correction when two or more USB devices including the other categories are used in the same process,
    the USB devices doesn't work normally.
  - Fault correction that the return value is 20001, when function 
    AioSetAiMemorySize/AioGetAiMemorySize is called for the devices which can 
    support the functions.
  - Fault in mixed use of a simple function and a sampling function is corrected at the time of AIO-163202FX-USB use. 

  Ver4.01->Ver4.10 (API-USBP(WDM) Ver4.60)
  --------------------------------
  - Supports new devices
    AIO-121602LN-USBAAIO-120802LN-USB
  - Visual Studio 2010 support

  Ver4.00->Ver4.01
  --------------------------------
  - Solves the problem that the function returns 20003 errors at multiprocessing. 
  - Under specific conditions "AoSpec.exe" to be used to hang fixes.

  Ver3.90->Ver4.00 (API-USBP(WDM) Ver4.40)
  --------------------------------
  - Supports new devices
    AI-1664LAX-USB
  - Supports Windows x64 Edition(USB devices)
  - Fault correction with the function declaration file of Visual Basic.NET
  - Fault correction that the return value is 0 (Normality completion), when function 
    AioSetAiMemorySize/AioGetAiMemorySize is called for the devices which can not 
    support the functions.
  - Fault correction that the acquisition value is always 0, when function AioGetAiStopTriggerCount 
    is called for DEMO board.
  - Fault correction that the clock is shorter than the specified value of function AioSetAiSamplingClock,
    when clock is set to be 1.4usec, 1.3usec, 0.9usec, 0.7usec.

  Ver3.80->Ver3.90 (API-USBP(WDM) Ver4.20)
  --------------------------------
  - Supports new devices
    AO-1604LX-USB
  - Solves the problem that AioSetControlFilter function 
    doesn't work correctly.(AIO-163202FX-USB)
  - Solves the problem that the last data may collapse 
    when AD conversion is repeated.(AIO-163202FX-USB)
  - Solves the problem that the value of AioGetAiStopTriggerCount function becomes 0 
    after executing AioStopAi function.(L-Series)
  - Solves the problem that 23260 error occures when
    value 2 is set to AioSetAoStopTrigger function.(L-Series)

  Ver3.70->Ver3.80 (supplied on Web, 2010.04.09)
  --------------------------------
  - Solves the problem that the application locks up when 
    AioStartAi and AioStopAi functions are executed repeatedly.(AI-1204Z-PCI)
  - Solves the problem that 23341 error occurs when executing 
    AioSetAoStartTrigger function.

  Ver3.62->Ver3.70 (API-USBP(WDM) Ver4.10, supplied on Web, 2009.11.27)
  --------------------------------
  - Supports Windows 7.
  - Solves the problem that the application locks up when 
    initialization->initiation->termination process is repeated twice.(AI-1204Z-PCI)
  - Solves the problem that 20003 error occurs when executing 
    AioInit after the application crashed.(AI-1204Z-PCI)
  - Solves the problem that overflow event doesn't ocuur.(AI-1204Z-PCI)
  - Solves the problem that sampling clock error status doesn't ocuur 
    when transfer process is not on time.(AI-1204Z-PCI)
  - Solves the problem that the last bainary data is set to 0 when acquireing data 
    under single-channel and odd number of sampling.(AI-1204Z-PCI)
  - Solves the problem that time interval of timer and 
    stopwatch is not correct.(AI-1204Z-PCI)
  - Solves some problems about RING memory mode.(AI-1204Z-PCI)

  Ver3.61->Ver3.62 (API-USBP(WDM) Ver4.00)
  --------------------------------
  - Solves the problem that hang-up may occurs when using
    AioGetAiSamplingData funcrion with RING memory.(E-Series)
  - Solves the problem that hang-up may occurs when executing
    AioInit, AioStartAo and AioExit funcrion repeatedly.(AO devices)
  - Solves the problem that 21960 error occurs when
    specifies device-buffer-mode by AioSetAiTransferMode function.(Z-Series)
  - Solves the problem that error occurs while hardware-installation
    on Windows 2000.

  Ver3.52->Ver3.61 (supplied on Web, 2009.05.19)
  --------------------------------
  - Solves the problem that 20001 error occures when setting 
    the function AioSetAiTransferMode, AioSetAoTransferMode, everytime.
  - Solves the problem that, under the state of "Wait the start trigger",
    the hang-up occurs when AioExit is performed (E-Series)
  - Solves the problem that overflow error was occured.(AI-1204Z-PCI).
  - Solves the problem that repeating operation software start - 
    stop conversion by the specified times, rock the devices(AI-1204Z-PCI).
  - Solves the problem that repeating operation AioStartAi - AioStopAi, 
    or AioStartAi - AioResetDevice, rock the devices(AI-1204Z-PCI).

  Ver3.52->Ver3.60 (API-USBP(WDM) Ver3.90)
  --------------------------------
  - Supports new devices
    AIO-163202FX-USB

  Ver3.51->Ver3.52 2009.03.04 (Ver.Mar.2009)
  --------------------------------
  - Solves the problem that counter's trouble(AIO-121602M-PCI).

  Ver3.50->Ver3.51 (supplied on Web, 2009.02.16)
  --------------------------------
  - Supports Windows Server 2008
  - Supports Windows Server 2008 64bit edition(other than USB devices)

  Ver3.47->Ver3.50 2009.01.16 (Ver.Jan.2009)
  --------------------------------
  - Supports new devices
    AIO-121601M-PCI
  - Adds new functions
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
  - Supports Visual C++ .Net C++/CLI.

  Ver3.46->Ver3.47 (supplied on Web, 2008.10.10)
  --------------------------------
  - Solves the problem that when set External clock, and set internal clock.
    Next, start sampling by external clock, sampling clock error was occured.(AI-1204Z-PCI).

  Ver3.45->Ver3.46 2008.10.01 (Ver.Oct.2008)
  --------------------------------
  - Solves the problem that when continuous sampling like sample AiLong, 
    sampling is stopped(DEMO devices, L-Series, and Non-F,ESeries devices).
  - Add the function that when operating sampling used ring memory, 
    it is able to get a sampling data(E-series).
  - Solves the problem that repeating operation AioStartAi - AioStopAi, 
    or AioStartAi - AioResetDevice, rock the devices(AI-1204Z-PCI).
  - Solves the problem that using Busmaster, sampling data is odd data
    (Busmaster device).
  - Solve the problem that events are not occured by setteing condition.
  - Supports API-TIMER(WDM).

  Ver3.44->Ver3.45 (supplied on Web, 2008.07.11)
  --------------------------------
  - Solves the problem that when using Analog Output devuces
    (except E, F, L-Series PCI devices),
    setting External trigger start, many times repeat,
    it is not enter the state of the trigger waiting at the next repeat.
  - Supports VisualStudio2008(except VC++, supports ExpressEdition).

  Ver3.43->Ver3.44 (supplied on Web, 2008.05.30)
  --------------------------------
  - Solves the problem that if using the function AioSetAiRange, and AioSetAiRangeAll,
    it is not able to get correct sampling data from devices(F, L-Series).

  Ver3.42->Ver3.43 (supplied on Web, 2008.05.09)
  --------------------------------
  - Solves the problem that Diagnosis Program can't be operated normally,
    when using CPU-CA10+FIT device with AI-1608AY-USB or AIO-160802AY-USB.
  - Solves the problem that API Functions for AI-1608AY-USB or AIO-160802AY-USB
    can't be operated normally, when using CPU-CA10+FIT device 
    with AI-1608AY-USB or AIO-160802AY-USB.

  Ver3.41->Ver3.42 (supplied on Web, 2008.04.30)
  --------------------------------
  - Solves the problem that a calibration program can't be ,
    and returns 22204 error(ADA16-32/2(CB)F).
  - Solve problems that it changes to unlimited Repeat, 
    and the callback setting, and call AioStopAi on sampling,
    application hangs irregularly.
  - Solves the problem when sampling Memory full, it is not able to 
    get sampling data from devices.

  Ver3.40->Ver3.41 2008.03.31 (Ver.Apr.2008)
  --------------------------------
  - Solves the problem that repeat function can't be operated normally.
    (DEMO devices, L-Series, and Non-F,ESeries devices)
  - Solve problems The level trigger setting is not reflected
    using USB-devices.
  - The mistake device name were corrected
    (AI-1664LA-LPE, AO-1608L-LPE, AO-1616L-LPE). 
  - AI-1204Z-PCI supports functions
    AioSetAiStartInRangeEx, AioGetAiStartInRangeEx
    AioSetAiStartOutRangeEx, AioGetAiStartOutRangeEx
    AioSetAiStopInRangeEx, AioGetAiStopInRangeEx
    AioSetAiStopOutRangeEx, AioGetAiStopOutRangeEx.
  - Solves the problem that 21440 error occures when
    using the function AiSamplingClock set 10usec everytime
    (ADA16-8/2(CP)L, AD16-64(LPCI)LA, AI-1664LA-LPE).

  Ver3.31->Ver3.40 2008.02.04 (Ver.Jan.2008 for AIO)
  --------------------------------
  - Supports new devices
    AI-1204Z-PCI,
    AIO-160802LI-PE, AI-1616LI-PE
    AO-1604LI-PE, AI-1664LA-LPE
    AO-1608L-LPE, AO-1616L-LPE

  Ver3.30->Ver3.31 (supplied on Web, 2008.01.25)
  --------------------------------
  - Solves the problem that the dialog of "DeviceType Unknown Error" is displayed
    when using AD12-8(PM) using on the property  page on the device manager. 
  - Solves the problem that OS hangs when using DEMO Device

  Ver3.21->Ver3.30 2007.12.21 (Ver.Jan.2008)
  --------------------------------
  - Solves the problem that the number of handle on the task manager 
    increases every time the application is operated. 
  - Solves the problem that a calibration program can't be adjusted,
    and returns 22204 error(L-Series).
  - Solves the problem that 20001 error occures when setting 
    the function AioSetDiFilter, AioGetDiFilter, everytime.
  - Solves the problem that correct Range can't be set 
    by the function AioSetAiRange, AioSetAiRangeAll.

  Ver3.20->Ver3.21 2007.10.12 (supplied on Web, 2007.10.22)
  --------------------------------
  - Solves the problem that occures while using ACX-PAC(W32)

  Ver3.10->Ver3.20 2007.09.30 (Ver.Oct.2007)
  --------------------------------
  - Supports new devices
    AIO-121601E3-PE, AIO-121601UE3-PE
    AIO-161601E3-PE, AIO-161601UE3-PE
  - Visual C# 2005 Express Edition, Visual Basic 2005 Express Edition support
  - Solves the problem that 21061 error occures when
    setting the function AioSetAiRangeAll everytime.
  - Solves the problem that the dialog of "DeviceType Unknown Error" is displayed
    when using DemoDevice using on the property  page on the device manager. 
  - Solve problems that it changes to Ring memory form, a limited sampling, 
    and the callback setting using USB-devices, and AiStart is repeated,
    sampling operation stoped.

  Ver3.00->Ver3.10 2007.06.11 (Ver.Jun.2007)
  --------------------------------
  - Supports Windows x64 Edition(other than USB devices)
  - Supports new devices
    AI-1216B-RB1-PCI, AI-1216B-RU1-PCI

  Ver2.30->Ver3.00 2007.02.28 (Ver.Feb.2007)
  --------------------------------
  - Supports Windows Vista
  - Supports new devices
    AIO-121602AH-PCI, AIO-121602AL-PCI, AI-1216AH-PCI, AI-1216AL-PCI
  - Adds digital-signing to device driver
  - Adds device driver auto-installation function (W2000 series only)
  - Adds version check of DLL and SYS function
  - Supports standby mode
  - Adds new functions
    AioResetProcess, AioStartAiSync
    AioSetAiStartInRangeEx, AioGetAiStartInRangeEx
    AioSetAiStartOutRangeEx, AioGetAiStartOutRangeEx
    AioSetAiStopInRangeEx, AioGetAiStopInRangeEx
    AioSetAiStopOutRangeEx, AioGetAiStopOutRangeEx
  - Adds utility for Visual Studio.NET
  - Solves the problem that OS hangs when using DEMO Device
  - Solves the problem that sometimes  AD or DA conversion error 
    occures when using simple functions (other than F and L series)
  - Solves the problem that OS hangs by clicking AioGetAiSamplingData
    when using CAIOSPEC.EXE (E series)
  - Solves the problem that motion doesn't complete unless one more
    sampling clock number which is specified (other than E, F and L series)
  - Solves the problem that data misalignment occures among channels
    under conditions of using multi channels, external trigger start,
    stop conversion by the specified times and multiple repeat times (L series)

  Ver2.20->Ver2.30 2006.12.04 (supplied on Web, 2006.12.15)
  --------------------------------
  - Solves the problem that AioGetAiSamplingCount function may
    return invalid value on multi-core CPU (E-Series)
  - Shorten the execution time and reduce the time variation of
    AioStartAi, AioStartAo, AioStartTmTimer and AioStartCnt function
  - Solves the problem that the event that specified number of data are stored
    may not occur depend on the process conditions

  Ver2.10->Ver2.20 2006.09.01 (supplied on Web, 2006.09.01)
  --------------------------------
  - Solves the problem that occures while using ML-DAQ

  Ver1.90->Ver2.10 2006.07.14 (Ver.Aug.2006)
  --------------------------------
  - Supports new devices
    AIO-160802L-LPE, AI-1616L-LPE, AO-1604L-LPE

  Ver1.80->Ver1.90 2006.03.24 (Ver.Apr.2006)
  --------------------------------
  - Supports new devices
    AIO-163202F-PE, DA16-8(LPCI)L, DA16-4(LPCI)L
  - Visual Studio 2005 support

  Ver1.70->Ver1.80 2005.12.01 (Ver.Feb.2006)
  --------------------------------
  - Supports C-LOGGER Ver1.0

  Ver1.60->Ver1.70 2005.09.29 (Ver.Nov.2005)
  --------------------------------
  - Supports new devices
    AD12-16(PCI)EV, AD12-16U(PCI)EV,
    AD16-16(PCI)EV, AD16-16U(PCI)EV,
    AD16-64(LPCI)LA

  Ver1.50->Ver1.60 2005.07.22 (Ver.Aug.2005)
  --------------------------------
  - Supports Windows Server 2003
  - Supports new devices
    ADAI16-8/2(LPCI)L, ADI16-16(LPCI)L, DAI16-4(LPCI)L
  - Adds new functions
    AioSetAiClockEdge, AioGetAiClockEdge
    AioSetAoClockEdge, AioGetAoClockEdge

  Ver1.42->Ver1.50 2005.03.31 (Ver.Apr.2005)
  --------------------------------
  - Supports MATLAB Data Acqiosition Toolbox

  Ver1.41->Ver1.42 2005.01.25 (supplied on Web, 2005.01.31)
  --------------------------------
  - Solves the problem that an automation error occurs
    while using ACX-AIO.

  Ver1.40->Ver1.41 2004.11.30 (Ver.Jan.2005)
  --------------------------------
  - Supports Hyper-Threading PC
  - Solves the problem that diagnosis program occurs error code 4
    occasionally with PCI boards
  - Solves the problem that acquired data become misaligned
    between each channels when using multi channels (L-Series)

  Ver1.31->Ver1.40 2004.08.26 (Ver.Oct.2003)
  --------------------------------
  - Supports new devices
    ADA16-8/2(CB)L
  - Solves the problem that gain adjustment cannot do 
    a calibration program manually.
    (F-Series,ADA12-8/2(LPCI),AD16-16(LPCI)L)

  Ver1.30->Ver1.31 2004.06.18 (Ver.Jun.2004)
  - Visual C#.NET2002, 2003 support
  - Supports scan clock setting (E-Series, F-Series)
  - Supports acquiring substrate temperature (ADI16-4L(PCI))
  - Solves the problem that AI motion does not stop normally
    if stop condition is changed by AioSetEcuSignal function
    (F-Series)
  - Solves the problem that AO motion does not stop normally
    if stop condition is changed by AioSetEcuSignal function
    (F-Series)
  - Solves the problem that the falling edge can't be specified
    when using external trigger start or stop mode
    (AD12-64(PCI), AD12-16(PCI))
  - Solves the problem that Lap value of AioGetAiTransferLap
    becomes unusual when transfering more than 64Mb data in
    bus master mode (F-Series)
  - Solves the problem that AioSetAiChannelSequence is invalid
    to AioMultiAi function (E-Series)

  Ver1.21->Ver1.30 2003.10.31 (Ver.Nov.2003)
  --------------------------------
  - Supports new devices
    ADA16-8/2(LPCI)L, AD16-16(LPCI)L, DA16-4(LPCI)L

  Ver1.20->Ver1.21 2003.06.02 (supplied on Web, 2003.06.11)
  --------------------------------
  - The following functions are added to uninstaller
    Delete setup information files that reproduced by the system
    Delete the device registered into the device manager
  - Solves the problem that a diagnostic program forces to terminate
    when a range is made a uni-Poral setup (E-Series)
  - Solves the problem which will be forced to terminate
    if x button is pushed during operation by AiSpec and AoSpec
  - Solves the problem which may be unable to set up a value normally
    with AiSetAiSamplingClock and AiSetAoSamplingClock function
    is corrected (all devices)
  - Solves the problem that DI data is not appended 
    (F-Series)
  - Solves the problem that will hang-up if AioExit function is performed
    inputting an external trigger continuously by Ai and Ao function
    (F-Series)
  - Solves the problem that cannot set up any ranges other than
    -10V - +10V or 0V - +10V and 4mA - 20mA with AioSetAiRangeAll function
    (ADI12-16(PCI))
  - Solves the problem that an omission generates to output data
    when a repeat output function is used by the RING memory
    (DA12-16(PCI), DA12-8(PCI), DA12-4(PCI))
  - Solves the form error of AioSetAiChannelSequence and AioGetAiChannelSequence
    (CAIO.BAS, CAIO.VB, CAIO.PAS)

  Ver1.10->Ver1.20 2003.03.01 (supplied on Web, 2003.03.14)
  --------------------------------
  - Supports English OS, Language, Tools
  - CAIO.DLL is sharable between API-AIO(WDM) and API-USBP(WDM)
  - Solves the problem that the converted data isn't right (AD16-4L(PCI))
  - Solves the problem that error occurs in
    AioSetAiStartInRange, AioSetAiStartOutRange,
    AioSetAiStopInRange and AioSetAiStopOutRange functions
  - Fixed the problem in sample AiEx 
    that the converted data in saved file is broken

  Ver1.04->Ver1.10 2002.12.25 (Ver.Dec.2002)
  --------------------------------
  - Supports new devices
    ADA16-32/2(PCI)F, ADA16-32/2(CB)F
  - Adds new functions
  - Visual C++.NET, Visual Basic.NET support
  - Adds new samples
  - Fixed the problem that the application is locked if other functions
    are used when the AioInit function failed (all devices)
  - Solves the problem that AioInit function succeeds even if the board JP
    is in the state that the interrupt is disabled (E-Series)
  - Solves the problem that the system exceptionally hangs up when the sampling clock error
    occurs because of the high-speed operation of analog I/O (all devices)
  - Adds NULL check and error code to functions AioQueryDeviceName and
    AioGetDeviceType(all devices)
  - Solves the problem that error occurs when channel 0 is specified for
    AioEnableAo and AioDisableAo (DAI16-4C(PCI))
  - Solves the problem that multi-channel output is abnormal (DAI16-4C(PCI))
  - Solves the problem that "Normality completion" is returned even if
    10820 error occurs(E-Series)
  - Corrects the driver in order to return error when function AioStartAi
    is executed without resetting the memory after buffer overflow error
    occurs(all devices)
  - Solves the problem that AD conversion error exceptionally occurs
    in function AioSingleAi (AD16-16U(PCI)EH)
  - Solves the problem that the ranges other than +/-10V, 0 to 10V and
    4mA to 20mA can not be set (ADI12-16(PCI))
  - Solves the problem that D/A conversion error exceptionally occurs in
    both function AioSingleAo and function AioMultiAo(DA12-16(PCI),
    DA12-8(PCI), DA12-4(PCI))
  - Solves the problem that the used handle is not opened when
    AioStartAi is performed (E-Series)
  - Solves the problem that graph drawing of both utility AiSpec and
    utility AoSpec does not support multi-channels(AD12-16U(PCI)EH, AD16-16U(PCI)EH)
  - Solves the problem that the old data is acquired in function AioSingleAi
    (ADI16-4C(PCI))
  - Solves the problem that +/-2.5V can not be set in function AioSetAiRange
    (AD12-16U(PCI)EH)

  Ver1.03->Ver1.04 2002.06.18 (Ver.Aug.2002)
  --------------------------------
  - Makes modifications in order that the failure in retrieving
    the sampling count is more difficult to come off (E-Series)
  - Solves the problem that the sampling clock error occurs
    at the 65535th time of event if you perform the operation
    in sample AiLong(E-Series)
  - Solves the problem that the converted data cannot be acquired
    normally from expansion channels when channels have been expanded
    (E-Series)
  - Solves the problem that W9x cannot start up as the card is plugged
    when you use cards on a note PC(AD12-8(PM))
  - Solves the problem that the raising of sampling clock causes
    the memory violation(AD12-8(PM))
  - Solves the problem that the incorrect converted data are acquired
    when the sampling clock is speeded to 10usec or so(AD12-8(PM))
  - Solves the problem that the sampling clock cannot be changed
    when external start trigger is used(DA12-16(PCI), DA12-8(PCI), DA12-4(PCI))

  Ver1.02->Ver1.03 2002.02.01 (supplied on Web, 2002.02.15)
  --------------------------------
  - Adds driver update method to help
  - Adds tutorial for simple digital I/O to help
  - The JP setting and pin assignment is illustrated in
    Driver Specifications-Specifications based on devices of help(Japanese only)
  - Solves the problem that, if the sample AiLong is used on W9x,
    the event doesn't occur when "Event that the specified number
    of data are stored" occurs and the window is moved
  - Solves the problem that the system hangs in sample MultiAo(AD12-8(PM))
  - Solves the problem that the data is incorrect in sample MultiAi
    (AD12-8(PM))
  - Solves the problem that the practical conversion speed is abnormal
    and data is incorrect in sample AiEx(AD12-8(PM))
  - Solves the problem that the status "Device is running" doesn't
    become OFF if the sampling times is set to 1
  - Corrects the sample programs
  - Takes out the description mistakes in help

  Ver1.01->Ver1.02 2002.01.15
  --------------------------------
  - Solves the problem that the driver cannot be used on W2000
    if you login as a user
  - Solves the problem that 0 is returned instead of 21441
  - Solves the problem that "Store up to the specified number
    of data" status doesn't become OFF even if retrieving data
    is performed (E-Series)
  - Solves the problem that, under the state of "Wait the start trigger",
    the error 21480 occurs when AioStopAi is performed (E-Series)
  - Corrects the sample programs
  - Takes out the description mistakes in help

  Ver1.00->Ver1.01 2001.12.16
  --------------------------------
  - Solves the problem that the repeat operation cannot be performed normally
    (E-Series)
  - Makes modifications in order that "Event that repeat end" is not fired
    when the repeat operation completely finished (E-Series)
  - Makes modifications in order that the clock error set by driver is
    reset by AioResetAiStatus or AioStartAi (E-Series)
  - Solves the problem that not only clock error occurs, but also conversion
    termination event occurs when the conversion speed is too fast, the driver
    cannot process them in time (E-Series)

  Ver1.00 2001.12.01 (Ver.Jan.2002)
  --------------------------------
  - First release

