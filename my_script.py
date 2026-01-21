import tkinter as tk
from tkinter import messagebox
import webbrowser


class VIPVideoParser:
    def __init__(self, root):
        self.root = root
        self.root.title("VIP 视频解析助手张建智QQ3111683964")
        self.root.geometry("800x400")
        self.create_widgets()

    def create_widgets(self):
        # 标签
        tk.Label(self.root, text="请输入视频 URL：").pack(pady=10)

        # 输入框
        self.url_entry = tk.Entry(self.root, width=50)
        self.url_entry.pack(pady=5)

        # 解析接口选择标签
        tk.Label(self.root, text="请选择解析接口：").pack(pady=10)

        # 解析接口选项
        self.parser_options = {
            "接口 1": "https://jx.xmflv.com/?url=",
            "接口 2": "https://jx.playerjy.com/?url=",
            "接口 3": "https://player.maqq.cn/?url=",
        }

        # 默认选择的接口
        self.selected_parser = tk.StringVar(self.root)
        self.selected_parser.set("接口 1")

        # 下拉菜单
        parser_menu = tk.OptionMenu(self.root, self.selected_parser, *self.parser_options.keys())
        parser_menu.pack(pady=5)

        # 解析按钮
        parse_button = tk.Button(self.root, text="解析播放", command=self.parse_video)
        parse_button.pack(pady=10)

        # 关于按钮
        about_button = tk.Button(self.root, text="关于", command=self.show_about)
        about_button.pack(pady=5)

    def parse_video(self):
        video_url = self.url_entry.get()
        if not video_url:
            messagebox.showwarning("警告", "请输入视频 URL！")
            return

        # 获取用户选择的解析接口
        selected_parser_name = self.selected_parser.get()
        parser_api = self.parser_options[selected_parser_name]
        full_url = parser_api + video_url

        # 打开默认浏览器播放视频
        webbrowser.open(full_url)

    def show_about(self):
        messagebox.showinfo("关于", "VIP 视频解析助手\n版本：1.0\n作者：张建智QQ3111683964")


if __name__ == "__main__":
    root = tk.Tk()
    app = VIPVideoParser(root)
    root.mainloop()