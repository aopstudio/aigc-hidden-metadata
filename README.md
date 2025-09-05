# AIGC Hidden Metadata

用 Python 给人工智能生成内容（AIGC）添加 **隐式标识** 的工具与示例代码。  
本项目实现了国家标准 **《人工智能生成合成内容标识方法》（GB45438—2025）** 中提到的文件隐式标识方法，涵盖图片、音频、视频和 PDF 等常见文件格式。

## 功能特性

- [x] 图片文件（JPG/PNG）：支持 **exempi** 和 **exiv2** 两种方案  
- [x] 音频文件（MP3）：基于 `ffmpeg` 添加隐式标识  
- [x] 视频文件（MP4）：基于 `ffmpeg` 添加隐式标识  
- [x] 文本文件（PDF）：基于 `PyPDF2` 写入自定义 metadata  
- [ ] 其他文件类型支持（欢迎 PR 🙌）

## 环境准备

依赖主要分为两类：系统工具 + Python 库。

### 系统工具
```bash
brew install ffmpeg
brew install exempi
brew install exiv2
````

### Python 库

```bash
pip install python-xmp-toolkit pyexiv2 ffmpeg-python PyPDF2
```

## 使用示例

### 图片（exiv2 方案）

```python
python image_exiv2.py
```

### 音频

```python
python audio_ffmpeg.py
```

### 视频

```python
python video_ffmpeg.py
```

### PDF

```python
python pdf_metadata.py
```

## 效果验证

* 图片：`exiv2 -pX sample.jpg`
* 音频/视频：`ffprobe -i output.mp3` / `ffprobe -i output.mp4`
* PDF：用文本编辑器打开可见 `/AIGC` 字段

## 背景说明

2025年9月1日起，《人工智能生成合成内容标识办法》正式实行，AI 生成合成内容必须添加显式或隐式标识。
隐式标识通过修改文件元数据来记录生成与传播信息，本项目旨在为开发者提供可直接运行的 Python 代码示例，帮助大家快速落地相关规范。

## 许可证

MIT License
