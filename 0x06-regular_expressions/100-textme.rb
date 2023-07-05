#!/usr/bin/env ruby
matches = ARGV[0].scan(/\[from:([A-Za-z]+|\+?\d{11})\]\s*\[to:([A-Za-z]+|\+?\d{11})\]\s*\[flags:(.+?)\]/)
if !matches.empty?
  matches.each do |match|
    puts "#{match[0]},#{match[1]},#{match[2]}"
  end
end
