filename = ARGV.first
txt = open(filename)
puts "Here's your file #{filename}:"
print txt.read
txt.close
