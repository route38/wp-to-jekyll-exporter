#!/usr/bin/env python3

import untangle
import slugify

with open("wordpress.wxr", "r") as fh:
  document = untangle.parse(fh)

posts = [post for post in document.rss.channel.item]

for post in posts:
  title_text = post.title.cdata
  title_text_parts = [part.strip() for part in title_text.split(":", 2)]
  date = post.wp_post_date.cdata.split(" ")[0]
  content = post.content_encoded.cdata

  if len(title_text_parts) > 1:
    title_text = title_text_parts[1]

  title = slugify.slugify(title_text)

  fn = f"{date}-{title}.md"
  preamble = f"""---
layout: post
title: "{title_text}"
---"""
  
  with open(fn, "w") as outfile:
    outfile.write(preamble)
    outfile.write("\n")
    outfile.write(content)

