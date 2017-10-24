#!/usr/bin/env bash
if [[ $# -ne 1 ]] ; then
    echo "Usage: ${0} http://example.com"
    exit 0
fi
echo "wget --mirror --convert-links --adjust-extension --page-requisites --no-parent ${1}"
wget --mirror --convert-links --adjust-extension --page-requisites --no-parent "${1}"
