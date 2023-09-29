import os

file_directory = '/media/zhaoyang-new/Expansion/Zhaoyang_Analysis/WenJing/Jing_CRISPR-Screen/Concatenated_FASTA/'
output_filename_path = '/media/zhaoyang-new/Expansion/Zhaoyang_Analysis/WenJing/Jing_CRISPR-Screen/code/concatenated_filenames.txt'
section_info = []
header_names = set()
id_index = 0
S_index =

for filename in os.listdir(file_directory):
    if filename.endswith('.fastq.gz'):
        parts = filename.split('_')
        header_names.add(parts[0])

for header in header_names:
    f1 = "None"
    f2 = "None"
    sample_ID = 'None'
    for filename in os.listdir(file_directory):
        if filename.endswith('.fastq.gz'):
            parts = filename.split('_')
            if parts[0] == header:
                sample_ID = parts[0] + '_' + parts[1]
                if parts[2].split('.')[0] == "R1":
                    f1 = filename
                elif parts[2].split('.')[0] == "R2":
                    f2 = filename
    section_info.append(tuple([sample_ID, f1, f2]))

with open(output_filename_path, 'w') as fp_write:
    for info in section_info:
        fp_write.write('{}\t{}\t{}\n'.format(info[0], info[1], info[2]))
