# core_spx V - 9.3

gcc main.c -o shell_web.exe -L. -lwebview -mwindows
start command - ./shell_web inst 400 400 "3000"

pyinstaller --onefile --windowed --add-data "web;web" main.py
start command - ./main 600 600 4000 hello

lib
go build -o FindFreePort.dll -buildmode=c-shared main.go

dotnet publish -c Release -r win-x64 --self-contained true /p:PublishSingleFile=true /p:PublishTrimmed=true