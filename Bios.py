import os
from Bio import SeqIO
def is_valid_cds(cds):
    if len(cds) <= 300:
        return False
    if not (cds.startswith("ATG") and (cds.endswith("TAG") or cds.endswith("TGA") or cds.endswith("TAA"))):
        return False
    if len(cds) % 3 != 0:
        return False
    # 检查中间是否有终止密码子或错误碱基
    for i in range(0, len(cds) - 3, 3):
        codon = cds[i:i+3]
        if codon in ["TAG", "TGA", "TAA"] or not all(base in "ATGC" for base in codon):
            return False
    return True
def filter_fasta_files(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
    
    for filename in os.listdir(input_folder):
        if filename.endswith(".fasta"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)
             
            valid_cds_records = []
            for record in SeqIO.parse(input_path, "fasta"):
                cds = str(record.seq).upper()
                if is_valid_cds(cds):
                    valid_cds_records.append(record)
             
            SeqIO.write(valid_cds_records, output_path, "fasta")
            print(f"Filtered {len(valid_cds_records)} valid CDS sequences to {output_path}")
# 请根据你的实际情况修改这些路径
input_folder = "C:/Users/Administrator/Desktop/cds-before"  # 输入文件夹的路径
output_folder = "C:/Users/Administrator/Desktop/cds-after"  # 输出文件夹的路径
filter_fasta_files(input_folder, output_folder)
