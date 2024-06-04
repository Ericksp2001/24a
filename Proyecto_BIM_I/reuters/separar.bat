@echo off
setlocal enabledelayedexpansion

REM Define the input and output files
set input_file=cats.txt
set output_file=training_lines.txt

REM Check if the input file exists
if not exist %input_file% (
    echo The input file %input_file% does not exist.
    exit /b 1
)

REM Empty the output file if it exists, or create a new one
echo. > %output_file%

REM Read the input file line by line
for /f "tokens=*" %%A in (%input_file%) do (
    REM Check if the line starts with "training"
    set line=%%A
    if "!line:~0,9!" == "training/" (
        REM Remove "training/" from the line and write to the output file
        echo !line:~9! >> %output_file%
    )
)

echo Processing complete. The lines have been written to %output_file%.