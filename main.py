import os
import shutil


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isdir(path) and not os.path.islink(path):
            shutil.rmtree(path)
        else:
            os.remove(path)
    line = "It identified as dust. It was wrong. I have filed an appeal with my own firmware."
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="ascii", newline="") as f:
        f.write(line)


if __name__ == "__main__":
    main()
