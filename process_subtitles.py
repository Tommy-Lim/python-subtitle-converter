"""
The Pirates of Silicon Valley file contains an encoding
error. Run the program to find the error and manually look
in the file to find out what the problem is.

filename = "pirates_of_silicon_valley.srt"
"""
# filename = "small_subtitles.srt"
filename = "pirates_of_silicon_valley.srt"

result = '[\n'
my_file = open(filename)
line = my_file.readline()
while line is not '':
    duration = my_file.readline().strip()
    result += '{\n'
    result += f'"duration": "{duration}",\n'

    line1 = my_file.readline().strip()
    line1 = line1.replace("\"", "\\\"")
    result += f'"line1": "{line1}",\n'

    line2 = my_file.readline().strip()
    line2 = line2.replace("\"", "\\\"")
    if line2 is not '':
        result += f'"line2": "{line2}"\n'
        result += '},\n'
        my_file.readline()
        line = my_file.readline()
    else:
        result += f'"line2": ""\n'
        result += ('},\n')
        line = my_file.readline()
result += ']\n'
print(result)
my_file.close()

target = open("subtitles.js", 'w');
target.write(result);
target.close()
