$pythonUrl = "https://www.python.org/ftp/python/3.10.0/python-3.10.0-amd64.exe"
$installer = "python_installer.exe"
Invoke-WebRequest -Uri $pythonUrl -OutFile $installer
Start-Process $installer -ArgumentList "/quiet InstallAllUsers=1 PrependPath=1" -Wait
Remove-Item $installer