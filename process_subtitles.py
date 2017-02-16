"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.

filename = "pirates_of_silicon_valley.srt"
"""
# filename = "small_subtitles.srt"
filename = "pirates_of_silicon_valley.srt"
result = '['
my_file = open(filename)
line = my_file.readline()
while line is not '':
    duration = my_file.readline().strip()
    result += '{'
    result += f'"duration": "{duration}",'
    line1 = my_file.readline().strip()
    result += f'"line1": "{line1}",'
    line2 = my_file.readline().strip()
    if line2 is not '':
        result += f'"line2": "{line2}"'
        result += '},'
        my_file.readline()
        line = my_file.readline()
    else:
        result += f'"line2": ""'
        result += ('},')
        line = my_file.readline()
result += ']'
print(result)

target = open("subtitles.js", 'w');
target.write(result);
target.close()
