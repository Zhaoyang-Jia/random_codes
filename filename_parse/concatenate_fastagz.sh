metadata_file="/media/zhaoyang-new/Expansion/Zhaoyang_Analysis/WenJing/Jing_CRISPR-Screen/code/origin_filenames.txt"
input_fasta_folder="/media/zhaoyang-new/Expansion/Data/WenJing/Jing_CRISPR-Screen/230919_A01535_0395_BH3HL7DRX3/"
output_fasta_folder="/media/zhaoyang-new/Expansion/Zhaoyang_Analysis/WenJing/Jing_CRISPR-Screen/Concatenated_FASTA/"

IFS=$'\t'

while read -r id file1_key file2_key output_file_key; do
        cat ${input_fasta_folder}/${file1_key} ${input_fasta_folder}/${file2_key} > ${output_fasta_folder}/${output_file_key} &
done < "$metadata_file"