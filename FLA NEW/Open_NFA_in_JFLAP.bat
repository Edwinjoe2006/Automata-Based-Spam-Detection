@echo off
title Open Spam NFA in JFLAP
echo Launching JFLAP with Spam NFA...
cd /d "%~dp0jflap"
start "" javaw -jar "JFLAP7.1.jar" "spam_nfa.jff"
exit
