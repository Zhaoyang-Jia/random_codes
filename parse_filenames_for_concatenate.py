import os

file_directory = '/nucleus/projects/globus_endpoint/monje_fastqs'
output_filename_path = '/nucleus/projects/monje/filenames.txt'
section_info = []
header_names = set()

for filename in os.listdir(file_directory):
    if filename.endswith('.fastq.gz'):
        parts = filename.split('_')
        header_names.add(parts[0])

for header in header_names:
    r1l1 = "None"
    r1l2 = "None"
    r2l1 = "None"
    r2l2 = "None"
    sample_ID = 'None'
    for filename in os.listdir(file_directory):
        if filename.endswith('.fastq.gz'):
            parts = filename.split('_')
            if parts[0] == header:
                sample_ID = parts[0] + '_' + parts[1]
                if parts[2] == 'L001' and parts[3] == 'R1':
                    r1l1 = filename
                elif parts[2] == 'L002' and parts[3] == 'R1':
                    r1l2 = filename
                elif parts[2] == 'L001' and parts[3] == 'R2':
                    r2l1 = filename
                elif parts[2] == 'L002' and parts[3] == 'R2':
                    r2l2 = filename
    section_info.append(tuple([header, r1l1, r1l2, sample_ID + "_R1.fastq.gz"]))
    section_info.append(tuple([header, r2l1, r2l2, sample_ID + "_R2.fastq.gz"]))

with open(output_filename_path, 'w') as fp_write:
    for info in section_info:
        fp_write.write('{}\t{}\t{}\t{}\n'.format(info[0], info[1], info[2], info[3]))
