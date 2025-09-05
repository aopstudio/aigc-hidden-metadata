# brew install exempi
# pip install python-xmp-toolkit

import os
# 设置 DYLD_LIBRARY_PATH，让 Python 能找到 libexempi.dylib。如果不写这句会报错找不到exempi
os.environ["DYLD_LIBRARY_PATH"] = "/opt/homebrew/lib"   # 注意要根据自己的操作系统来设定，这里是mac系统的

from libxmp import XMPFiles, XMPMeta
from libxmp.consts import XMP_NS_DC

def add_image_mark(file_path):
    AIGC_NS_URI = "http://www.tc260.org.cn/ns/AIGC/1.0/"
    AIGC_NS_PREFIX = "TC260"
    XMPMeta.register_namespace(AIGC_NS_URI, AIGC_NS_PREFIX)

    xmpfile = XMPFiles(file_path=file_path, open_forupdate=True)
    try:
        xmp = xmpfile.get_xmp() or XMPMeta()
        xmp.set_property(XMP_NS_DC, "title", "example title")
        xmp.set_property(AIGC_NS_URI, "AIGC",
                         '{"Label":"value1","ContentProducer":"value2","ProduceID":"value3",'
                         '"ReservedCode1":"value4","ContentPropagator":"value5",'
                         '"PropagateID":"value6","ReservedCode2":"value7"}')
        xmpfile.put_xmp(xmp)
        print(f"成功写入扩展 XMP 到 {file_path}")
    except Exception as e:
        print(f"写入失败：{str(e)}")
    finally:
        xmpfile.close_file()
if __name__ == '__main__':
    add_image_mark("sample.jpg")


# 检查写入的元数据
# exempi -x sample.jpg