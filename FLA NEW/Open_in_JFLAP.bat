@echo off
title Open Spam DFA in JFLAP
echo Launching JFLAP with Spam DFA...
cd /d "%~dp0jflap"
start "" javaw -jar "JFLAP7.1.jar" "spam_dfa.jff"
exit
