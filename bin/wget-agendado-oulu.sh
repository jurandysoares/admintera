#!/bin/sh
AGENDA="/tmp/agenda"
echo -e "Laboratório: "
read LAB
echo -e "PC: "
read PC
echo "*/5 *  *   *   *     wget -o /dev/null oulu.ifrn.local/lab/${LAB}/${PC}/" > $AGENDA
crontab $AGENDA
crontab -l
echo "Confere o agendamento?"
