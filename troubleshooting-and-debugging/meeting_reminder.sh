#!/bin/bash

meeting_info=$(Zenity --forms \
	--title 'Meeting' --text 'Reminder information' \
	--add-calendar 'Date' --add-entry 'Title' \
	--add-entry 'Emails' \
	2>/dev/null)
if [[ -n "$meeting_info" ]]; then
	echo "Successfully sent the reminder email."
fi
