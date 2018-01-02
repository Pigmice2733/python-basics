@echo off

setlocal

cd tests
set PYTHONPATH=..\src
py -3 -m pytest -v

endlocal