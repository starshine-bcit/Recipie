Write-Host 'Attempting to compile .py'
& pyuic6 -x -o qtuitest.py .\recipie_test\mainwindow.ui
Write-Host 'qtuitest.py successfully written'