import os

file_directory = '/nucleus/projects/globus_endpoint/monje_fastqs'
output_filename_path = '/nucleus/projects/monje/origin_filenames.txt'
section_info = []
header_names = set()
id_index = 2
s_index = 3
lane_index = 4
read_index = 5

for filename in os.listdir(file_directory):
    if filename.endswith('.fastq.gz'):
        parts = filename.split('_')
        header_names.add(parts[id_index])

for header in header_names:
    r1l1 = "None"
    r1l2 = "None"
    r2l1 = "None"
    r2l2 = "None"
    sample_ID = 'None'
    for filename in os.listdir(file_directory):
        if filename.endswith('.fastq.gz'):
            parts = filename.split('_')
            if parts[id_index] == header:
                sample_ID = parts[id_index] + '_' + parts[s_index]
                if parts[lane_index] == 'L001' and parts[read_index] == 'R1':
                    r1l1 = filename
                elif parts[lane_index] == 'L002' and parts[read_index] == 'R1':
                    r1l2 = filename
                elif parts[lane_index] == 'L001' and parts[read_index] == 'R2':
                    r2l1 = filename
                elif parts[lane_index] == 'L002' and parts[read_index] == 'R2':
                    r2l2 = filename
    section_info.append(tuple([header, r1l1, r1l2, sample_ID + "_R1.fastq.gz"]))
    section_info.append(tuple([header, r2l1, r2l2, sample_ID + "_R2.fastq.gz"]))

with open(output_filename_path, 'w') as fp_write:
    for info in section_info:
        fp_write.write('{}\t{}\t{}\t{}\n'.format(info[0], info[1], info[2], info[3]))
