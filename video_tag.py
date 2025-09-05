# brew install ffmpeg
# pip install ffmpeg-python

import ffmpeg

input_file = "input.mp4"
output_file = "output.mp4"

def add_video_tag(input_file, output_file):
    metadata = {
        "AIGC": '{"Label":"value1","ContentProducer":"value2","ProduceID":"value3",'
                '"ReservedCode1":"value4","ContentPropagator":"value5",'
                '"PropagateID":"value6","ReservedCode2":"value7"}'
    }

    (   
        ffmpeg
        .input(input_file)
        .output(
            output_file,
            metadata=f"AIGC={metadata['AIGC']}",  # 设置 metadata
            movflags="use_metadata_tags",
            c="copy"
        )
        .run(overwrite_output=True)
    )

if __name__ == "__main__":
    add_video_tag(input_file, output_file)

# 检查新的元数据是否写入成功
# ffprobe -i output.mp4