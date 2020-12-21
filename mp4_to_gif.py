import moviepy.editor as mpy

# 视频文件的本地路径
content = mpy.VideoFileClip("D:\\1.mp4")
# 剪辑0分0秒到0分9秒的片段。resize为修改清晰度
content = content.fl_time(lambda t:  1.5*t, apply_to=['mask', 'audio'])  # 对视频进行调速
change = content.subclip((0, 0), (0, 6)).resize(0.1).set_fps(10)
# 保存为gif图到python的默认路径
change.write_gif("D:\\1.gif")
