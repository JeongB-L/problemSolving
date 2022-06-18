import csv

if '__main__' == __name__:
    data = open('example.csv',encoding="utf-8")
    #   read the csv data
    csv_data = csv.reader(data)
    #   unicodedecode error occurs often. the file contains @ symbol for emails
    data_lines = list(csv_data)
    print(data_lines[0])
    print(len(data_lines))
    print('\n')
    for line in data_lines[:5]:
        print(line)
        print('\n')
    all_emails = []
    full_names = []
    for line in data_lines[1 : 15]:
        all_emails.append(line[3])
    for line in data_lines[1 : 15]:
        full_names.append(line[1] + ' ' + line[3])

    #   now make the output
    file_to_output = open('to_save_file.csv', mode='w', newline='')
    #   delimiter is a separator between each content
    csv_writer = csv.writer(file_to_output, delimiter=',')
    csv_writer.writerow(['a', 'b', 'c'])
    csv_writer.writerows([['alpha', 'beta','gamma'], ['oi', 've', 'france']])

    file_to_output.close()
    #   mode=a means to append, not overwrite
    f = open('to_save_file.csv', mode='a', newline='')
    csv_writer = csv.writer(f)
    csv_writer.writerow(['1', '2', '2424234234234'])
