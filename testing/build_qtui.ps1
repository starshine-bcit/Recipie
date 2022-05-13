Write-Host 'Attempting to compile .py'
if (Test-Path 'qtui.py') {
    Write-Host 'old Qtui.py found, removing...'
    Remove-Item 'qtui.py'
}
& pyuic6 -x -o .\modules\qtui.py .\testing\recipie_test\mainwindow.ui
Write-Host 'qtui.py successfully written'
