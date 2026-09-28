"""一个最简脚本，用来确认本地 Python 环境正常。"""

from datetime import datetime


def greet(name: str = "茉莉") -> str:
    return f"你好，{name}！你的 GitHub 环境已经跑通了。"


if __name__ == "__main__":
    print(greet())
    print(f"当前时间：{datetime.now():%Y-%m-%d %H:%M:%S}")
