"""
fix_frontmatter.py — 修复 wiki/summaries/ 下所有 frontmatter 解析问题
"""
import pathlib
import yaml
import re

summaries = pathlib.Path('wiki/summaries')
fixed = 0
skipped = 0

for f in summaries.glob('*.md'):
    content = f.read_text(encoding='utf-8')

    # 修复1：去掉开头空行
    stripped = content.lstrip('\n\r ')
    if stripped != content:
        content = stripped
        f.write_text(content, encoding='utf-8')

    # 跳过没有 frontmatter 的文件（纯图片等）
    if not content.startswith('---'):
        skipped += 1
        continue

    end = content.find('---', 3)
    if end == -1:
        skipped += 1
        continue

    # 检查是否已经正常
    try:
        yaml.safe_load(content[3:end])
        continue  # 正常，跳过
    except Exception:
        pass

    # 修复：逐行处理 frontmatter
    fm_text = content[3:end]
    lines = fm_text.split('\n')
    new_lines = []
    for line in lines:
        if ':' not in line:
            new_lines.append(line)
            continue
        key = line.split(':', 1)[0]
        val = line.split(':', 1)[1].strip()

        # 去掉外层引号
        if val.startswith('"') and val.endswith('"'):
            val = val[1:-1]
        elif val.startswith("'") and val.endswith("'"):
            val = val[1:-1]

        # 将内部的中文引号（\u201c \u201d）替换为空，或转义
        val = val.replace('\u201c', '').replace('\u201d', '')
        val = val.replace('\u2018', '').replace('\u2019', '')
        # 将内部的直双引号转义
        val = val.replace('"', '')

        new_lines.append(f'{key}: "{val}"')

    new_fm = '\n'.join(new_lines)
    new_content = '---' + new_fm + content[end:]

    # 验证修复后是否能解析
    try:
        yaml.safe_load(new_fm)
        f.write_text(new_content, encoding='utf-8')
        fixed += 1
    except Exception as e:
        print(f'[仍有问题] {f.name}: {e}')

print(f'修复: {fixed} 个 | 跳过(无frontmatter): {skipped} 个')
