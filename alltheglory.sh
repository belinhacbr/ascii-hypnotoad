
convert hypnotoad.gif -transparent "#fefefe" -gravity Center -crop 300x200-16+16 -resize 50% hypnotoad-t.gif
convert hypnotoad-t.gif frames/hypnotoad.jpg
rm hypnotoad-t.gif
for i in frames/hypnotoad*.jpg; do
  jp2a $i --colors > $i.ansi
  rm $i
done
