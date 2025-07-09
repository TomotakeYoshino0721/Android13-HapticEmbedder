这是一个能通过提取音频元数据使手机线性马达震动发声的工具脚本（类似骨传导耳机）
使用方法
 单文件处理
python haptic.py music.ogg
 批量处理当前目录
python haptic.py --batch
 指定输出文件名
python haptic.py input.ogg output.ogg
需要安装的依赖
 pip install mutagen
    一定要先把音频转成48khz 网站https://www.ezyzip.com/cn-mp3-48kHz.html#
然后再转换成.ogg格式文件！！！

By YuzakiPTeam@2025
第一次这种程序 有问题请您反馈和谅解
感谢大家的支持
暂不支持小米设备（缺少相关API）
目前通过测试且效果较好的机型 一加13
项目中附带两个音频文件 其中AF为载入过元数据的样本音频 BF为没有载入过元数据的样本音频
其他机型请自行测试 所导致的问题本人概不负责
环境，安装等请自行调试
