@echo off
title Discord RPC
set /p i=Install [I] or Run [R]

if %i% ==R (node index.js) else (npm install)

PAUSE
