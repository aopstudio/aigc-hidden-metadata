# 安装依赖
# brew install exiv2  # mac系统，其他系统请自行调整
# pip install pyexiv2

import pyexiv2
import json

def add_image_tag(file_path):
    AIGC_NS_URI = "http://www.tc260.org.cn/ns/AIGC/1.0/"
    AIGC_NS_PREFIX = "TC260"

    aigc_value = {
        "Label": "value1",
        "ContentProducer": "value2",
        "ProduceID": "value3",
        "ReservedCode1": "value4",
        "ContentPropagator": "value5",
        "PropagateID": "value6",
        "ReservedCode2": "value7",
    }

    # 打开文件
    img = pyexiv2.Image(file_path)

    pyexiv2.registerNs(AIGC_NS_URI, AIGC_NS_PREFIX)

    # 设置 XMP 属性，键名形如：Xmp.TC260.AIGC
    img.modify_xmp({
        f"Xmp.{AIGC_NS_PREFIX}.AIGC": json.dumps(aigc_value, ensure_ascii=False)
    })

    img.close()
    print(f"成功写入扩展XMP 到 {file_path}")


if __name__ == "__main__":
    add_image_tag("exiv_sample.jpg")

"""
在终端检查写入的元数据命令为：
```sh
exiv2 -pX sample.jpg
```

在我个人的尝试中，使用exiv2并不会像exempi那样python找不到系统库的情况，因此也无需设置环境变量，只要通过brew安装好即可
"""