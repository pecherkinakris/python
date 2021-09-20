from sys import argv
script_name, output, rate, premium = argv

print((int(output) * int(rate)) + int(premium))