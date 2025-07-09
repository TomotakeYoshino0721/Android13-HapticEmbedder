import sys
import os
import struct
import math
from mutagen.oggvorbis import OggVorbis

def inject_haptic_metadata(input_file, output_file=None, threshold=0.3):
    if output_file is None:
        output_file = input_file.replace('.ogg', '_haptic.ogg')
    
    with open(input_file, 'rb') as src, open(output_file, 'wb') as dst:
        dst.write(src.read())
    
    audio = OggVorbis(output_file)
    
    audio["ANDROID_HAPTIC"] = "1"
    audio["HAPTIC_VERSION"] = "1.0"
    
    audio["HAPTIC_MODE"] = "AUTO"  
    
    file_size = os.path.getsize(input_file)
    energy_level = min(100, int(math.log(file_size / 1024) * 10))
    audio["HAPTIC_ENERGY"] = str(energy_level)
    
    audio.save()
    
    print(f" 成功注入震动元数据: {output_file}")
    print(f"   - 文件大小: {file_size/1024:.1f}KB")
    print(f"   - 能量级别: {energy_level}/100")
    print(f"   - 播放提示: 系统将自动分析音频生成震动")

def batch_inject(files):
    for file in files:
        if file.endswith('.ogg'):
            inject_haptic_metadata(file)
            print(f"已处理: {file}")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("音频震动元数据注入工具")
        print("用法: python haptic.py [文件1.ogg] [文件2.ogg] ...")
        print("或: python haptic.py --batch (处理当前目录所有OGG)")
        sys.exit(1)
    
    if sys.argv[1] == "--batch":
        import glob
        batch_inject(glob.glob("*.ogg"))
    else:
        for file in sys.argv[1:]:
            inject_haptic_metadata(file)