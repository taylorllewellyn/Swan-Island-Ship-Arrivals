#! /bin/bash

curl -s https://colrip.com/dispatch-info/dispatch-status/ | sed 's/<tr><td>/\n/g' |grep -E "$(date +"%b %d")|$(date -d "+1 day" +"%b %d")|$(date -d "+2 day" +"%b %d")|$(date -d "+3 day" +"%b %d")|$(date -d "+4 day" +"%b %d")|$(date -d "+5 day" +"%b %d")|$(date -d "+6 day" +"%b %d")|$(date -d "+7 day" +"%b %d")" | grep -v '(Away)' | sed 's/<\/td><td>/\t/g' | sed 's/<\/td><\/tr>/ /g' | column -t -s $'\t' | grep -w "301\|302\|303\|304\|305\|306\|307\|308\|309\|310\|311\|312\|313\|314\|315\|DD6" | sed '1iVESSEL\tFROM\tTO\tDATE\tTUG\tLENGTH' | txt2html |mail --content-type=text/html --exec 'set nonullbody' -s "Columbia River Pilots Daily Report" hayden.llewellyn@gmail.com


