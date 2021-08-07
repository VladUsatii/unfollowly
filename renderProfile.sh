#!/bin/bash
mv $1 unfollowly/static/data
rm -rf $1
result=$(find ./unfollowly/static/data/$1 -name "*.jpg")
mv $result unfollowly/static/pp.jpg
