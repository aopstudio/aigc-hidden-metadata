# pip install PyPDF2

import json
from PyPDF2 import PdfReader, PdfWriter

def add_pdf_tag(input_pdf, output_pdf, metadata_dict):
    """
    在 PDF 的 Document Information Dictionary 中写入自定义 /AIGC 字段
    :param input_pdf: 输入 PDF 文件路径
    :param output_pdf: 输出 PDF 文件路径
    :param metadata_dict: Python dict，内容会被写入 /AIGC
    """

    # 将 dict 转为 JSON 字符串
    aigc_json = json.dumps(metadata_dict, ensure_ascii=False)

    reader = PdfReader(input_pdf)
    writer = PdfWriter()

    # 复制所有页面
    for page in reader.pages:
        writer.add_page(page)

    # 获取原有信息字典
    info = reader.metadata or {}

    # 新增 /AIGC 字段
    info.update({"/AIGC": aigc_json})

    # 写入新的 PDF
    writer.add_metadata(info)
    with open(output_pdf, "wb") as f:
        writer.write(f)
    print(f"AIGC metadata written to {output_pdf}")

# 示例使用
metadata = {
    "Label": "value1",
    "ContentProducer": "value2",
    "ProduceID": "value3",
    "ReservedCode1": "value4",
    "ContentPropagator": "value5",
    "PropagateID": "value6",
    "ReservedCode2": "value7"
}

if __name__ == "__main__":
    add_pdf_tag("input.pdf", "output.pdf", metadata)

# 检查写入的元数据
f'''
直接用文本编辑器以原始编码形式打开pdf文件，可以看到
<<
/Producer
/Author
/CreationDate 
/ModDate
/Title 
/AIGC ...
>>
'''