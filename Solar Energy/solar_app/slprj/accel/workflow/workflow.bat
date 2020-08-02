@echo off
set MATLAB=C:\Program Files\MATLAB\MATLAB Production Server\R2015a
"%MATLAB%\bin\win64\gmake" -f workflow.mk  ISPROTECTINGMODEL=NOTPROTECTING
