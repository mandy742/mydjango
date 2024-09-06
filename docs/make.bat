@ECHO OFF

pushd %~dp0

REM Command file for Sphinx documentation

REM Check if SPHINXBUILD environment variable is set, if not, set it to 'sphinx-build'
if "%SPHINXBUILD%" == "" (
	set SPHINXBUILD=sphinx-build
)
REM Set the source and build directories
set SOURCEDIR=.
set BUILDDIR=_build

REM Check if sphinx-build command is available
%SPHINXBUILD% >NUL 2>NUL
if errorlevel 9009 (
	echo.
	echo.The 'sphinx-build' command was not found. Make sure you have Sphinx
	echo.installed, then set the SPHINXBUILD environment variable to point
	echo.to the full path of the 'sphinx-build' executable. Alternatively you
	echo.may add the Sphinx directory to PATH.
	echo.
	echo.If you don't have Sphinx installed, grab it from
	echo.https://www.sphinx-doc.org/
	exit /b 1
)
REM If no arguments are provided, show help
if "%1" == "" goto help

%SPHINXBUILD% -M %1 %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%
goto end

REM Show help message
:help
%SPHINXBUILD% -M help %SOURCEDIR% %BUILDDIR% %SPHINXOPTS% %O%

:end
popd
