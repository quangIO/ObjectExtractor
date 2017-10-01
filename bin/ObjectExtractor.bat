@echo OFF
REM="""
setlocal
set PythonExe=""
set PythonExeFlags=

for %%i in (cmd bat exe) do (
    for %%j in (python.%%i) do (
        call :SetPythonExe "%%~$PATH:j"
    )
)
for /f "tokens=2 delims==" %%i in ('assoc .py') do (
    for /f "tokens=2 delims==" %%j in ('ftype %%i') do (
        for /f "tokens=1" %%k in ("%%j") do (
            call :SetPythonExe %%k
        )
    )
)
%PythonExe% -x %PythonExeFlags% "%~f0" %*
exit /B %ERRORLEVEL%
goto :EOF

:SetPythonExe
if not ["%~1"]==[""] (
    if [%PythonExe%]==[""] (
        set PythonExe="%~1"
    )
)
goto :EOF
"""



#!/usr/bin/env python
from object_extractor import Extractor
import sys
import os

def main():
    print(os.getcwd() + '\\' + sys.argv[1])
    return Extractor.extract(os.getcwd() + '\\' + sys.argv[1])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('Usage: ObjectExtractor filename.png')
        sys.exit(1)
    print(str(main()) + ' objects found')